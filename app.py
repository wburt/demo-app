import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("PORT", 8080))
MESSAGE_CONTENT = os.getenv("DEMO_MESSAGE", "Hello Demo Seekers!")

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>OpenShift Demo</title>
    <style>
        body {{ font-family: sans-serif; text-align: center; margin-top: 50px; }}
        h1 {{ color: #333; }}
        p {{ color: #666; }}
    </style>
</head>
<body>
    <h1>OpenShift Demo Deployment</h1>
    <p>Message from environment variable: <strong>{MESSAGE_CONTENT}</strong></p>
    <p>This page is served by a Python HTTP server.</p>
</body>
</html>
""".encode("utf-8"))

if __name__ == "__main__":
    with HTTPServer(("", PORT), CustomHandler) as httpd:
        print(f"serving at port {PORT}")
        httpd.serve_forever()