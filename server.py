from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

VIEWER_DIR = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?")[0]
        local = VIEWER_DIR / clean.lstrip("/")
        if local.is_file():
            return str(local)
        return clean


print("http://localhost:8766/index.html")
HTTPServer(("", 8766), Handler).serve_forever()
