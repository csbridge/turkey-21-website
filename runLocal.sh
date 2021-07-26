#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
	echo "Terminating..."
	kill -9 %1
}

python3 compile.py
python3 -m http.server --directory docs &
python3 -m webbrowser http://localhost:8000 > /dev/null
watchmedo auto-restart --directory templates --directory config --recursive python3 compile.py