#!/bin/bash
set -e

# use make setenv to update ENV_RSLV_DIR
ENV_RSLV_DIR=
MODULE="cli"
SYSTEM_PYTHON3=$(which python3)

function cli_rslv() {
    eval "PYTHONPATH=$ENV_RSLV_DIR $SYSTEM_PYTHON3 -m $MODULE" "$@"
}

cli_rslv "$@"
