export interface ChatMessage {
  id: string;
  user: string;
  text: string;
  type: 'chat' | 'system';
  createdAt: string;
}
