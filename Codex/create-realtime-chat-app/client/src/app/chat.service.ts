import { Injectable, signal } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { ChatMessage } from './chat-message.model';

const SERVER_URL = window.location.port === '4200' ? 'http://localhost:3000' : window.location.origin;

export interface ActiveUser {
  id: string;
  name: string;
}

export interface ChatGroup {
  id: string;
  name: string;
  members: ActiveUser[];
  createdBy: ActiveUser;
}

@Injectable({ providedIn: 'root' })
export class ChatService {
  readonly messages = signal<ChatMessage[]>([]);
  readonly onlineUsers = signal(0);
  readonly connected = signal(false);
  readonly activeRoomId = signal('');
  readonly currentUser = signal<ActiveUser | null>(null);
  readonly activeUsers = signal<ActiveUser[]>([]);
  readonly groups = signal<ChatGroup[]>([]);
  readonly unreadCounts = signal<Record<string, number>>({});

  private socket: Socket;
  private joinedName = '';

  constructor() {
    this.socket = io(SERVER_URL, {
      autoConnect: false,
      transports: ['websocket', 'polling']
    });

    this.socket.on('connect', () => this.connected.set(true));
    this.socket.on('disconnect', () => this.connected.set(false));
    this.socket.on('users:count', count => this.onlineUsers.set(Number(count) || 0));
    this.socket.on('user:me', user => this.currentUser.set(user));
    this.socket.on('users:list', users => this.activeUsers.set(users ?? []));
    this.socket.on('groups:list', groups => this.groups.set(groups ?? []));
    this.socket.on('group:created', group => {
      this.groups.update(current => current.some(item => item.id === group.id) ? current : [group, ...current]);
    });
    this.socket.on('chat:history', payload => {
      if (payload?.roomId === this.activeRoomId()) {
        this.messages.set(payload.messages ?? []);
      }
    });
    this.socket.on('chat:message', message => {
      if (message?.roomId === this.activeRoomId()) {
        this.messages.update(current => [...current, message]);
        this.clearUnread(message.roomId);
        return;
      }

      if (message?.roomId) {
        this.unreadCounts.update(current => ({
          ...current,
          [message.roomId]: (current[message.roomId] ?? 0) + 1
        }));
      }
    });
  }

  join(name: string): void {
    if (!this.socket.connected) {
      this.socket.connect();
    }

    this.joinedName = name;
    this.socket.emit('user:join', name);

    if (this.activeRoomId()) {
      this.selectRoom(this.activeRoomId());
    }
  }

  sendMessage(text: string): void {
    this.socket.emit('chat:message', {
      roomId: this.activeRoomId(),
      text
    });
  }

  selectRoom(roomId: string): void {
    this.activeRoomId.set(roomId);
    this.messages.set([]);

    if (!roomId) {
      return;
    }

    this.clearUnread(roomId);

    if (this.socket.connected && this.joinedName) {
      this.socket.emit('conversation:join', roomId);
    }
  }

  createGroup(name: string, memberIds: string[]): void {
    this.socket.emit('group:create', { name, memberIds });
  }

  unreadCount(roomId: string): number {
    return this.unreadCounts()[roomId] ?? 0;
  }

  private clearUnread(roomId: string): void {
    this.unreadCounts.update(current => {
      if (!current[roomId]) {
        return current;
      }

      const next = { ...current };
      delete next[roomId];
      return next;
    });
  }
}
