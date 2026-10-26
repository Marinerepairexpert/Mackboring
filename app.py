"""Small, dependency-free development web application."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            body = b"<!doctype html><html lang='en'><meta charset='utf-8'><title>Mackboring</title><h1>Mackboring</h1><p>The application is running.</p></html>"
            status, content_type = 200, "text/html; charset=utf-8"
        elif path == "/health":
            body = b'{"status":"ok"}\n'
            status, content_type = 200, "application/json"
        else:
            body = b"Not found\n"
            status, content_type = 404, "text/plain; charset=utf-8"
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer((args.host, args.port), Handler) as server:
        print(f"Mackboring listening on {args.host}:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
