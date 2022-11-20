# Docker tutorial

## Context

1. [Docker file overview](#1-dockerfile-overview)
2. [Docker compose configuration](#2-docker-compose-configuration)
3. [Build docker image](#3-build-docker-image)
4. [Run image file](#4-run-image-file)
5. [Check running contaiers](#5-check-running-contaiers)
6. [Stop a running container](#6-stop-a-running-container)
7. [Run service in a docker environment](#7-run-service-in-a-docker-environment)

## 1. Dockerfile overview

First we import official python image
```
FROM python:3
```

After that we set the working directory
```
WORKDIR /home/mpeter/Docker_Tutorial
```

Before we start the application, it is important to install the requirements.
So first we copy the file to the image base path
```
COPY requirements.txt ./
```
**The requirements.txt can be exported with the commad:* ```pip3 freeze > requirements.txt```

After that we will run pip installation process
```
RUN pip install --no-cache-dir -r requirements.txt
```

After the requirements are installed succesfully we copy the whole project to the image
```
COPY . .
```

After the image is ready we run our service
```
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

**docker-compose.yml is a file to configure more contaioners and container deps.*

## 2. Docker compose configuration

In the ```docker-compose.yml``` file we can configure more services/containers

The first row is always a yaml file version definition
```
version: '3'
```

After that under the ```service``` word we can configure the services, the order, ...
```
services:
```

In the example I start one service, which name can be anything, now it is ```docker_tutorial```
```
  docker_tutorial:
```

Under the ```docker_tutorial``` we will connect a volume (now if we edit anything in the path it will be affected to the run).
The port setting is a bridge between the world and the container. Inside the Flask runs on port 80 outside 5000
```
    build: .
    volumes:
      - .:/home/mpeter/Docker_Tutorial
    ports:
      - 5000:80
```

## 3. Build docker image

We can use names and tags ```name:tag```, but the tag is optional. (Default tag: ```latest```)
```
docker build --tag test:test .
```

Check the docker images
```
docker images
```

Create a new tag to an image
```
docker tag test:latest test:torlesre_var
```

Delete a tag from an image
```
docker rmi test:torlesre_var
```

Delete an image (IMAGE ID needed)
```
docker rmi 1b5e1d161915
```

## 4. Run image file

To run image file it is important to be accurate with the ```name:tag```definitions
```
docker run test:test
```
**to stop the contaioner press Ctrl+c*

If we would like to publish our container we have to use ```--publish``` or ```-p``` like ```[host port]:[container port]```
```
docker run --publish 8000:5000 --name test_server_01 test:test
```

**With ```--detach``` or ```-d``` flag we can run the container in the background!*

## 5. Check running contaiers

With this command we can check running containers
```
docker ps
```

## 6. Stop a running container

With the name or ID of a container we can stop it (The name is automatically generated if you do not define it)
```
docker stop wonderful_kalam
```

## 7. Run service in a docker environment

```
docker-compose up
```

Stop docker environment
```
docker compose down
```