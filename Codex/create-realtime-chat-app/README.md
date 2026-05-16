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

Start both the API server and Angular dev server for development:

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

## Run On One Port

Build the Angular app and start the Node server:

```bash
npm run build
npm start
```

Open:

```text
http://localhost:3000
```

The Node server serves the Angular build and Socket.IO from the same port. This is the recommended setup for Render.

## Render Deploy

Use these commands:

```text
Build Command: npm install && npm run build
Start Command: npm start
```

Vercel static hosting is not recommended for this version because Socket.IO needs a persistent Node server.

## Project Structure

```text
client/   Angular application
server/   Express + Socket.IO backend
```
