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

## build docker image
```bash
docker build -t gptsvc:v1 .
```

## run docker image
```bash
docker run -p 8000:8000 --read-only gptsvc:v1
```

## access the URL
```bash
❯ curl http://0.0.0.0:8000/hello
{"message":"Hello World!!!"}
```