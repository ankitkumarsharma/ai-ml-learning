import express from 'express';
import http from 'node:http';
import { randomUUID } from 'node:crypto';
import cors from 'cors';
import { Server } from 'socket.io';

const PORT = process.env.PORT || 3000;
const CLIENT_ORIGIN = process.env.CLIENT_ORIGIN || 'http://localhost:4200';
const MAX_HISTORY = 50;

const app = express();
const server = http.createServer(app);
const histories = new Map();
const users = new Map();
const activeRooms = new Map();
const userGroups = new Map();
const groups = new Map();

app.use(cors({ origin: CLIENT_ORIGIN }));
app.use(express.json());

app.get('/health', (_request, response) => {
  response.json({
    status: 'ok',
    users: users.size,
    rooms: histories.size
  });
});

const io = new Server(server, {
  cors: {
    origin: CLIENT_ORIGIN,
    methods: ['GET', 'POST']
  }
});

function getHistory(roomId) {
  if (!histories.has(roomId)) {
    histories.set(roomId, []);
  }

  return histories.get(roomId);
}

function createMessage({ roomId, user, text, type = 'chat' }) {
  return {
    id: randomUUID(),
    roomId,
    user,
    text,
    type,
    createdAt: new Date().toISOString()
  };
}

function addMessage(roomId, message) {
  const history = getHistory(roomId);
  history.push(message);

  if (history.length > MAX_HISTORY) {
    history.shift();
  }
}

function emitUserCount() {
  io.emit('users:count', users.size);
}

function getActiveUsers() {
  return [...users.entries()].map(([id, name]) => ({ id, name }));
}

function emitUsersList() {
  io.emit('users:list', getActiveUsers());
}

function getGroupsForUser(userId) {
  return userGroups.get(userId) ?? [];
}

function getRecipientsForRoom(roomId) {
  if (roomId.startsWith('dm:')) {
    return roomId.slice(3).split(':').filter(id => users.has(id));
  }

  const group = groups.get(roomId);

  if (group) {
    return group.members.map(member => member.id).filter(id => users.has(id));
  }

  return [];
}

io.on('connection', socket => {
  socket.emit('users:count', users.size);
  socket.emit('users:list', getActiveUsers());

  socket.on('user:join', rawName => {
    const name = String(rawName || '').trim().slice(0, 32) || 'Anonymous';
    users.set(socket.id, name);
    socket.emit('user:me', { id: socket.id, name });
    socket.emit('groups:list', getGroupsForUser(socket.id));
    emitUserCount();
    emitUsersList();
  });

  socket.on('group:create', payload => {
    const creator = users.get(socket.id);
    const name = String(payload?.name || '').trim().slice(0, 40);
    const requestedMembers = Array.isArray(payload?.memberIds) ? payload.memberIds : [];
    const memberIds = [...new Set([socket.id, ...requestedMembers.filter(id => users.has(id))])];

    if (!creator || !name || memberIds.length < 3) {
      return;
    }

    const group = {
      id: `group-${randomUUID()}`,
      name,
      members: memberIds.map(id => ({ id, name: users.get(id) })),
      createdBy: { id: socket.id, name: creator }
    };

    groups.set(group.id, group);

    for (const memberId of memberIds) {
      const groups = getGroupsForUser(memberId);
      groups.push(group);
      userGroups.set(memberId, groups);
      io.to(memberId).emit('group:created', group);
    }
  });

  socket.on('conversation:join', rawRoomId => {
    const roomId = String(rawRoomId || 'general').trim().slice(0, 140) || 'general';
    const previousRoomId = activeRooms.get(socket.id);

    if (previousRoomId) {
      socket.leave(previousRoomId);
    }

    activeRooms.set(socket.id, roomId);
    socket.join(roomId);
    socket.emit('chat:history', {
      roomId,
      messages: getHistory(roomId)
    });
  });

  socket.on('chat:message', payload => {
    const roomId = String(payload?.roomId || activeRooms.get(socket.id) || 'general').trim().slice(0, 140);
    const text = String(payload?.text || '').trim().slice(0, 500);
    const user = users.get(socket.id);

    if (!user || !text) {
      return;
    }

    const message = createMessage({ roomId, user, text });
    addMessage(roomId, message);

    const recipients = getRecipientsForRoom(roomId);

    if (recipients.length > 0) {
      for (const recipientId of recipients) {
        io.to(recipientId).emit('chat:message', message);
      }

      return;
    }

    io.to(roomId).emit('chat:message', message);
  });

  socket.on('disconnect', () => {
    users.delete(socket.id);
    activeRooms.delete(socket.id);
    userGroups.delete(socket.id);
    emitUserCount();
    emitUsersList();
  });
});

server.listen(PORT, () => {
  console.log(`Chat server listening on http://localhost:${PORT}`);
});
