#!/bin/bash
#set -x

HOST=${1:-localhost}
PORT=${2:-8888}
python3 -m http.server --bind $HOST $PORT

