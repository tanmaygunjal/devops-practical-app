from http.server import BaseHTTPRequestHandler, HTTPServer

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello DevOps Practical App")

server = HTTPServer(("0.0.0.0", 8000), App)

print("Server running on port 8000...")
server.serve_forever()