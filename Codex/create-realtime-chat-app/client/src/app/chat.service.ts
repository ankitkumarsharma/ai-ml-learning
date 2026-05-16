import { Injectable, signal } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { ChatMessage } from './chat-message.model';

const SERVER_URL = 'http://localhost:3000';

@Injectable({ providedIn: 'root' })
export class ChatService {
  readonly messages = signal<ChatMessage[]>([]);
  readonly onlineUsers = signal(0);
  readonly connected = signal(false);

  private socket: Socket;

  constructor() {
    this.socket = io(SERVER_URL, {
      autoConnect: false,
      transports: ['websocket', 'polling']
    });

    this.socket.on('connect', () => this.connected.set(true));
    this.socket.on('disconnect', () => this.connected.set(false));
    this.socket.on('users:count', count => this.onlineUsers.set(Number(count) || 0));
    this.socket.on('chat:history', messages => this.messages.set(messages ?? []));
    this.socket.on('chat:message', message => {
      this.messages.update(current => [...current, message]);
    });
  }

  join(name: string): void {
    if (!this.socket.connected) {
      this.socket.connect();
    }

    this.socket.emit('user:join', name);
  }

  sendMessage(text: string): void {
    this.socket.emit('chat:message', text);
  }
}
