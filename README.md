> [!WARNING]
> This is an entirely vibe-coded tool so beware of the SLOP

# Eval Run Viewer

View eval run JSON output files as a readable report with rendered markdown and expandable tool calls.

## Usage

1. Edit `config.js` — set `evalOutputDir` to the absolute path of your local `.eval_runs/branch/raw_outputs/` directory
   ```js
   evalOutputDir: '/Users/uttam/Documents/Work/chat-retrieval/.eval_runs/branch/raw_outputs/'
   ```

2. Start the server. [Install uv](https://docs.astral.sh/uv/#installation) if you don't have it already.
   ```sh
   uv run server.py
   ```

3. Open http://localhost:8766

The latest run will be loaded. You can also pick a file from the dropdown at the top (newest first) to view it — the list
refreshes every 5 seconds and contains the 15 latest files.
You can still deep-link with URL query param `?input=<filename>`.

Ctrl+C to stop the server.

## Screenshots

Output
![output.png](example_screenshots/output.png)

Tool calls (query and response)
![tool_calls.png](example_screenshots/tool_calls.png)
