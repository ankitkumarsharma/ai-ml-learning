# Angular + Node Realtime Chat

A small realtime chat application using Angular, Node.js, Express, and Socket.IO.

## Features

- Join chat with a display name
- Realtime messages across connected browsers
- User join/leave notifications
- Online user count
- Recent in-memory message history
- Responsive chat UI

## Run Locally

Install dependencies:

```bash
npm install
```

Start both the API server and Angular dev server:

```bash
npm run dev
```

Open the Angular app:

```text
http://localhost:4200
```

The Socket.IO server runs on:

```text
http://localhost:3000
```

## Project Structure

```text
client/   Angular application
server/   Express + Socket.IO backend
```
