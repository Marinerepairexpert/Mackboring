# Mackboring

A minimal Python web application using only the standard library.

## Requirements

Python 3.10 or newer. No packages, credentials, or external services are needed.

## Run

From the repository directory:

```sh
python3 app.py
```

The server defaults to host `127.0.0.1` and port `8000`. Use `--host` and
`--port` to change them. Press Ctrl+C to stop.

## Check

With the server running, use another terminal:

```sh
curl --fail http://127.0.0.1:8000/
curl --fail http://127.0.0.1:8000/health
```

The home page displays “Mackboring” and the health endpoint returns
`{"status":"ok"}`. Unknown paths return HTTP 404.

This is a development starter; Python's built-in HTTP server is not intended
for production deployment.
