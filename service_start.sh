#!/bin/bash
set -e

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source $SCRIPTDIR/.venv/bin/activate
uvicorn main:app --reload --host=0.0.0.0 --port=7777 --workers 2