import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, payload)
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json(200, payload)
        else:
            self._send_text(404, "Endpoint not found")

    def _send_text(self, code, message):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def log_message(self, format, *args):
        pass


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
