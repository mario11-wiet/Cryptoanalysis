#!/bin/bash

handle_error() {
    echo "ERROR: An error occurred during script execution." >&2
    exit 1
}

trap 'handle_error' ERR

python3 -m venv env || handle_error

source env/bin/activate || handle_error

pip install -r requirements.txt || handle_error

python run.py || handle_error
