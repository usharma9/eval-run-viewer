#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

VIEWER_DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?")[0]
        local = os.path.join(VIEWER_DIR, clean.lstrip("/"))
        if os.path.isfile(local):
            return local
        return clean


print(f"http://localhost:8766/index.html")
HTTPServer(("", 8766), Handler).serve_forever()
