import { CommonModule } from '@angular/common';
import { Component, computed, effect, ElementRef, inject, signal, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActiveUser, ChatGroup, ChatService } from './chat.service';

interface Conversation {
  id: string;
  name: string;
  avatar: string;
  subtitle: string;
  preview: string;
  type: 'direct' | 'group';
}

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
  protected readonly searchTerm = signal('');
  protected readonly groupName = signal('');
  protected readonly creatingGroup = signal(false);
  protected readonly selectedGroupMembers = signal<string[]>([]);
  protected readonly joined = signal(false);
  protected readonly activeUsers = computed(() => {
    const currentId = this.chat.currentUser()?.id;
    return this.chat.activeUsers().filter(user => user.id !== currentId);
  });
  protected readonly directContacts = computed<Conversation[]>(() => {
    return this.activeUsers().map(user => ({
      id: this.createDirectRoomId(user.id),
      name: user.name,
      avatar: this.createAvatar(user.name),
      subtitle: 'online',
      preview: 'Private one-to-one chat',
      type: 'direct' as const
    })).filter(contact => this.matchesSearch(contact));
  });
  protected readonly groupContacts = computed<Conversation[]>(() => {
    return this.chat.groups().map(group => ({
      id: group.id,
      name: group.name,
      avatar: this.createAvatar(group.name),
      subtitle: `${group.members.length} members`,
      preview: group.members.map(member => member.name).join(', '),
      type: 'group' as const
    })).filter(contact => this.matchesSearch(contact));
  });
  protected readonly conversations = computed(() => [...this.directContacts(), ...this.groupContacts()]);
  protected readonly activeContact = computed(() => {
    return this.conversations().find(contact => contact.id === this.chat.activeRoomId()) ?? null;
  });
  protected readonly canCreateGroup = computed(() => this.groupName().trim().length > 0 && this.selectedGroupMembers().length >= 2);
  protected readonly canSend = computed(() => this.draft().trim().length > 0 && this.joined() && !!this.activeContact());

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

  protected selectContact(contact: Conversation): void {
    this.draft.set('');
    this.chat.selectRoom(contact.id);
  }

  protected closeConversation(): void {
    this.draft.set('');
    this.chat.selectRoom('');
  }

  protected toggleGroupMember(userId: string, checked: boolean): void {
    this.selectedGroupMembers.update(current => {
      if (checked) {
        return current.includes(userId) ? current : [...current, userId];
      }

      return current.filter(id => id !== userId);
    });
  }

  protected createGroup(): void {
    const name = this.groupName().trim();
    const memberIds = this.selectedGroupMembers();

    if (!name || memberIds.length < 2) {
      return;
    }

    this.chat.createGroup(name, memberIds);
    this.groupName.set('');
    this.selectedGroupMembers.set([]);
    this.creatingGroup.set(false);
  }

  protected startGroupCreation(): void {
    this.creatingGroup.set(true);
  }

  protected cancelGroupCreation(): void {
    this.creatingGroup.set(false);
    this.groupName.set('');
    this.selectedGroupMembers.set([]);
  }

  protected isSelectedForGroup(user: ActiveUser): boolean {
    return this.selectedGroupMembers().includes(user.id);
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

  private createAvatar(value: string): string {
    return value
      .split(/\s+/)
      .filter(Boolean)
      .slice(0, 2)
      .map(part => part[0].toUpperCase())
      .join('');
  }

  private createDirectRoomId(otherUserId: string): string {
    const currentUserId = this.chat.currentUser()?.id ?? '';
    return `dm:${[currentUserId, otherUserId].sort().join(':')}`;
  }

  private matchesSearch(contact: Conversation): boolean {
    const term = this.searchTerm().trim().toLowerCase();

    if (!term) {
      return true;
    }

    return `${contact.name} ${contact.subtitle} ${contact.preview}`.toLowerCase().includes(term);
  }
}
