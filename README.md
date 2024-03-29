# pycam
Python application that shares a camera with clients over the network.

## Running server

The server opens the webcam and starts listening on a tcp port, waiting for connections.

```bash
python3 pycam_server.py
```

The server support multiple client connections.



## Running clients

The client connects on the server and gets the frame. After it, it shows the frame on a window.

```bash
python3 pycam_client.py --ip=localhost
```

To exit the window, press ESC key. Multiple clients can be started.


## Getting help
Both server and client have `-h` and `--help` parameters.

```bash
python3 pycam_server --help
```

```bash
python3 pycam_client --help
```
