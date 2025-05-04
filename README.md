---
title: "Mistral Model Serving API"
emoji: 🦙
colorFrom: indigo
colorTo: pink
sdk: docker
sdk_version: "3.1.2"
app_file: gptsvc/main.py
pinned: false
---

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

# Run the code in minikube

To install minikube, follow these [steps](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download)

## start minikube 

```bash
minikube start
# point to minikube docker
eval $(minikube docker-env)
```

## build the docker image

```bash
docker build -t gptsvc:v1 .
kubectl config set-context --current --namespace app
```



