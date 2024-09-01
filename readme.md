## build an image
docker build -t image_name .

## create a container
docker create -it --name container_name image_name

## start a container
docker start container_name

## stop a container
docker stop container_name

## use bash
docker exec -it container_name bash

## create and start
docker run -dit --name container_name image_name