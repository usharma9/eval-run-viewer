> [!WARNING]
> This is an entirely vibe-coded tool made for personal use.

# Eval Run Viewer

View eval run JSON output files as a readable report with rendered markdown and expandable tool calls.

## Quick start

1. Edit `config.js` — set `evalOutputDir` to the absolute path of your local `.eval_runs/branch/raw_outputs/` directory:
   ```js
   evalOutputDir: '/path/to/chat-retrieval/.eval_runs/branch/raw_outputs/',
   ```

2. Start the server:
   ```sh
   python3 server.py
   ```

3. Open http://localhost:8766/index.html

To view a different file, pass the filename as a query param:
```
http://localhost:8766/index.html?input=8fa4025a-3693-4f09-a798-8f4abeabac0c_trial_1.json
```

Ctrl+C to stop the server.

## Screenshots

Output
![output.png](example_screenshots/output.png)

Tool calls (query and response)
![tool_calls.png](example_screenshots/tool_calls.png)
