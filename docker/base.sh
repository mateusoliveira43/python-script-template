#!/bin/bash

DOCKER_COMPOSE_BIN="docker-compose"
DOCKER_COMPOSE_FROM_DOCKER="docker compose"

if [ -x "$(command -v $DOCKER_COMPOSE_BIN)" ]; then
    DOCKER_COMPOSE=$DOCKER_COMPOSE_BIN
else
    DOCKER_COMPOSE=$DOCKER_COMPOSE_FROM_DOCKER
fi
