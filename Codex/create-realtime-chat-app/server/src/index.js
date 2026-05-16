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
const messages = [];
const users = new Map();

app.use(cors({ origin: CLIENT_ORIGIN }));
app.use(express.json());

app.get('/health', (_request, response) => {
  response.json({
    status: 'ok',
    users: users.size,
    messages: messages.length
  });
});

const io = new Server(server, {
  cors: {
    origin: CLIENT_ORIGIN,
    methods: ['GET', 'POST']
  }
});

function createMessage({ user, text, type = 'chat' }) {
  return {
    id: randomUUID(),
    user,
    text,
    type,
    createdAt: new Date().toISOString()
  };
}

function addMessage(message) {
  messages.push(message);

  if (messages.length > MAX_HISTORY) {
    messages.shift();
  }
}

function emitUserCount() {
  io.emit('users:count', users.size);
}

io.on('connection', socket => {
  socket.emit('chat:history', messages);
  socket.emit('users:count', users.size);

  socket.on('user:join', rawName => {
    const name = String(rawName || '').trim().slice(0, 32) || 'Anonymous';
    users.set(socket.id, name);

    const message = createMessage({
      user: 'System',
      text: `${name} joined the chat`,
      type: 'system'
    });

    addMessage(message);
    io.emit('chat:message', message);
    emitUserCount();
  });

  socket.on('chat:message', rawText => {
    const text = String(rawText || '').trim().slice(0, 500);
    const user = users.get(socket.id);

    if (!user || !text) {
      return;
    }

    const message = createMessage({ user, text });
    addMessage(message);
    io.emit('chat:message', message);
  });

  socket.on('disconnect', () => {
    const user = users.get(socket.id);

    if (!user) {
      return;
    }

    users.delete(socket.id);

    const message = createMessage({
      user: 'System',
      text: `${user} left the chat`,
      type: 'system'
    });

    addMessage(message);
    socket.broadcast.emit('chat:message', message);
    emitUserCount();
  });
});

server.listen(PORT, () => {
  console.log(`Chat server listening on http://localhost:${PORT}`);
});
