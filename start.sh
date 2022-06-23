 #! /bin/bash

COMMAND="docker compose -f docker-compose.yaml -f docker-compose-elk.yml -f extensions/apm-server/apm-server-compose.yml"

if [ $# -eq 1 ]; then
  if [ "$1" == "-build" ]; then
    echo "build docker compose"
    ${COMMAND} build
    exit 0
  elif [ "$1" == "-up" ]; then
    echo "up docker containers"
    ${COMMAND} up
  elif [ "$1" == "-down" ]; then
    echo "down docker containers"
    ${COMMAND} down
  else 
    echo "invalid parameter 1 : ${1}"
    echo "use parameter 1 : -build or -down or -up or -up -d"
  fi
elif [ $# -eq 2 ]; then
  if [ "$1" == "-up" -a "$2" == "-d" ]; then
    echo "start docker conainers background"
    ${COMMAND} up -d
  fi
else
  echo "required parameter 1 : -build or -down or -up or -up -d"
  exit 0
fi