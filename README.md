---
title: "Mistral Model Serving API"
emoji: 🦙
colorFrom: indigo
colorTo: pink
sdk: docker
sdk_version: "3.1.2"
app_file: gptsvc/main.py
app_port : 8000
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

kubectl create ns app
kubectl config set-context --current --namespace app
```

## create namespace and start the pod
```bash
cd deployment/minikube
kubectl apply -f pod.yaml
```

## access the app via proxy 
```bash
❯ kubectl proxy
Starting to serve on 127.0.0.1:8001

❯ curl http://localhost:8001/api/v1/namespaces/app/pods/gptsvc-pod/proxy/healthz
{"status":"ok"}
```
