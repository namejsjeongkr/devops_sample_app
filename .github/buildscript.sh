#!/bin/bash
#$1 : ecr repository url
echo $2

SERVICE=( "sample-app" )
for SERVICE in ${SERVICE[@]}; do
    docker tag ${SERVICE}:latest $1/${SERVICE}:$2
    docker push $1/${SERVICE}:$2
done
