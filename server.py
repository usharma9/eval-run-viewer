import tomllib
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

VIEWER_DIR = Path(__file__).resolve().parent
FILE_LIST_MAX_ITEMS = 15


def load_config():
    with open(VIEWER_DIR / "config.toml", "rb") as f:
        return tomllib.load(f)


config = load_config()

app = FastAPI()


@app.get("/")
def index():
    return FileResponse(VIEWER_DIR / "index.html")


@app.get("/api/config")
def get_config():
    return {
        "defaultEvalFilename": config["default_eval_filename"],
        "inputCostPerMillionTokens": config["cost_per_million_tokens"]["input"],
        "outputCostPerMillionTokens": config["cost_per_million_tokens"]["output"],
    }


@app.get("/api/files")
def list_files():
    eval_output_dir = Path(config["eval_output_dir"])
    latest_files = sorted(
        eval_output_dir.glob("*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )
    return [
        {"name": f.name, "mtime": f.stat().st_mtime}
        for f in latest_files[:FILE_LIST_MAX_ITEMS]
    ]


@app.get("/api/run/{filename}")
def get_run(filename: str):
    path = Path(config["eval_output_dir"]) / filename
    if not path.is_file() or not path.name.endswith(".json"):
        return JSONResponse({"error": "not found"}, status_code=404)
    return FileResponse(path)


app.mount("/", StaticFiles(directory=VIEWER_DIR), name="static")

if __name__ == "__main__":
    uvicorn.run(app, port=8766)
