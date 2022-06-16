# pycam
Server that shares a camera with clients over network.

## Running server

The server opens the webcam and starts to listen on a tcp port, waiting for connections.

```bash
python3 pycam_server.py
```

## Running clients

The client connects on the server and gets the frame. After it, it shows the frame on a window.

```bash
python3 pycam_client.py --ip=localhost
```

To exit the window, press ESC key.