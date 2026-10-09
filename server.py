import re
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

VIEWER_DIR = Path(__file__).resolve().parent
FILE_LIST_MAX_ITEMS = 15

app = FastAPI()


def eval_output_dir():
    config = (VIEWER_DIR / "config.js").read_text()
    match = re.search(r"evalOutputDir:\s*'([^']+)'", config)
    return Path(match.group(1))


@app.get("/")
def index():
    return FileResponse(VIEWER_DIR / "index.html")


@app.get("/api/files")
def list_files():
    """
    Used by the file selection dropdown.
    """
    latest_files = sorted(
        eval_output_dir().glob("*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )
    return [
        {"name": f.name, "mtime": f.stat().st_mtime}
        for f in latest_files[:FILE_LIST_MAX_ITEMS]
    ]


@app.get("/api/run/{filename}")
def get_run(filename: str):
    path = eval_output_dir() / filename
    if not path.is_file() or not path.name.endswith(".json"):
        return JSONResponse({"error": "not found"}, status_code=404)
    return FileResponse(path)


app.mount("/", StaticFiles(directory=VIEWER_DIR), name="static")

if __name__ == "__main__":
    uvicorn.run(app, port=8766)
