# Docker Notes

## Dockerfile

This is used to build the docker image.

1. Base image is python3.8
2. Add the requirement file and main.py to the image
3. Install dependencies on image
4. Establish a start command

Run this command:
`docker build -t chappiebot:latest .`
NOTE: "chappiebot:latest" is just a name : version for the image

## Docker-compose

This is takes image and spins up a service

1. Version is what features you have with docker-compose
2. we create a service called chappiebot
3. Give it a name
4. Select an image (the one we built)
5. Restart and environment variables

Run this command:
`docker-compose up -d`
NOTE: -d flag will be detached

## Using docker-compose only

First build:
`docker-compose build`

Then launch:
`docker-compose up -d`
