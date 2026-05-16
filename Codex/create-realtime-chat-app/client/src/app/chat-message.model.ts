export interface ChatMessage {
  id: string;
  roomId: string;
  user: string;
  text: string;
  type: 'chat' | 'system';
  createdAt: string;
}
