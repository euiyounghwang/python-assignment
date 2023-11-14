#!/bin/bash
set -e

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source $SCRIPTDIR/.venv/bin/activate
poetry run python ./tools/lookup_keys_script.py