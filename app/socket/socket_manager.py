import socketio

socket = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
connected_clients = set()


@socket.event
async def connect(socket_id, environ):
    print(f"Client connected: {socket_id}")
    connected_clients.add(socket_id)


@socket.event
async def disconnect(socket_id):
    print(f"Client disconnected: {socket_id}")
    connected_clients.discard(socket_id)
