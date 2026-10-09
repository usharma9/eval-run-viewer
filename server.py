import json
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

VIEWER_DIR = Path(__file__).resolve().parent


def eval_output_dir():
    config = (VIEWER_DIR / "config.js").read_text()
    match = re.search(r"evalOutputDir:\s*'([^']+)'", config)
    return Path(match.group(1))


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?")[0]
        local = VIEWER_DIR / clean.lstrip("/")
        if local.is_file():
            return str(local)
        return clean

    def do_GET(self):
        if urlparse(self.path).path == "/api/files":
            self.send_file_list()
            return
        super().do_GET()

    def send_file_list(self):
        files = sorted(
            eval_output_dir().glob("*.json"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )
        body = json.dumps(
            [{"name": f.name, "mtime": f.stat().st_mtime} for f in files]
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("http://localhost:8766/index.html")
    HTTPServer(("", 8766), Handler).serve_forever()
