# Eval Run Viewer

Displays eval run JSON output files in a readable format.

## `config.js` file

- `evalOutputDir` — absolute path to the directory containing eval run JSON files. Set this to the `.eval_runs` folder in your local chat-retrieval repo. 
- `defaultEvalFilename` — the file loaded when no `?input=` query param is given. Not important if you will use the query param – it's just a default.

## Usage
Set `evalOutputDir` and `defaultEvalFilename`.


Run server
```sh
python3 server.py
```

Then open http://localhost:8766/index.html. Ctrl+C to stop.

## Viewing a different file

Either change `defaultEvalFilename` in `config.js`, or pass it as a query param:

```
http://localhost:8766/index.html?input=8fa4025a-3693-4f09-a798-8f4abeabac0c_trial_1.json
```
