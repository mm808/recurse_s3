#!/bin/bash

if [ -z "$1" ]
then
  echo "you must provide VERSION variable"
  exit 1
fi

docker run -it --rm --name python-dev-container \
    --volume ~/SourceCode/recurse_s3/src:/src \
    python-dev-container:$1