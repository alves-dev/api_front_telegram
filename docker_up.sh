#!/bin/bash

docker container rm -f python_api_front_telegram
docker rmi -f api_front_telegram:last

docker build -t api_front_telegram:last .
docker run -d --restart always -p 7111:7111 --name python_api_front_telegram api_front_telegram:last
