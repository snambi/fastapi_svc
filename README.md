# FastAPI Inference Service

## Setup workspace

```bash
python -mvenv .venv
. ./.venv/bin/activate

pip install -r requirments.txt
pip install -r requirments-dev.txt
```


## Run from CLI

```bash
uvicorn gptsvc:main.app --reload 
```

## Clean up generated files
```bash
invoke clean
```

