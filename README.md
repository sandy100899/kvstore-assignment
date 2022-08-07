# This application contains the following API endpoints

1. POST /set
2. GET /get/:key
3. GET /search?prefix=&suffix=


# Steps to run the application on local

Run the below command in terminal to install all the dependencies present in requirements.txt file


```bash
pip3 install -r requirements.txt
```

Go inside the app directory

Export the environment variables REDIS_HOST and REDIS _PORT before actually running the application

Run following command in terminal to set the environment variables

```bash
export REDIS_HOST=localhost
export REDIS_PORT=6379
```

Run the below command inside the app directory to run the unit tests

```bash
pytest
```

Run the command below to start the backend server

```bash
uvicorn main:app
```

Go to http://localhost:8000/docs for accessing the swagger docs of the backend server


# Steps to run the application on kubernetes

Run the below command to build the docker image of backend server

```bash
docker build --no-cache -t kvstore . 
```

Run the below commands inside the deployments folder to deploy the kubernetes resources in the kubernetes cluster

```bash
kubectl apply -f kvstore.yml
kubectl apply -f redis.yml
kubectl apply -f ingress.yml
```

Go to http://my-app.com/server/docs for accessing the swagger docs of the backend server or you can also directly send curl requests to http://my-app.com/server
