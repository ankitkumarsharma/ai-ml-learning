import { CommonModule } from '@angular/common';
import { Component, computed, effect, ElementRef, inject, signal, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChatService } from './chat.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  protected readonly chat = inject(ChatService);
  protected readonly name = signal('');
  protected readonly draft = signal('');
  protected readonly joined = signal(false);
  protected readonly canSend = computed(() => this.draft().trim().length > 0 && this.joined());

  @ViewChild('messageList') private messageList?: ElementRef<HTMLDivElement>;

  constructor() {
    effect(() => {
      this.chat.messages();
      queueMicrotask(() => this.scrollToLatest());
    });
  }

  protected joinChat(): void {
    const name = this.name().trim();

    if (!name) {
      return;
    }

    this.chat.join(name);
    this.joined.set(true);
  }

  protected sendMessage(): void {
    const text = this.draft().trim();

    if (!text) {
      return;
    }

    this.chat.sendMessage(text);
    this.draft.set('');
  }

  protected formatTime(value: string): string {
    return new Intl.DateTimeFormat(undefined, {
      hour: 'numeric',
      minute: '2-digit'
    }).format(new Date(value));
  }

  private scrollToLatest(): void {
    const element = this.messageList?.nativeElement;

    if (element) {
      element.scrollTop = element.scrollHeight;
    }
  }
}
