#!/bin/bash
set -e

# use make setenv to update ENV_RSLV_DIR
ENV_RSLV_DIR=
MODULE="cliresolve"
CLIRSV_DIR="$ROOT_DIR/$MODULE"
SYSTEM_PYTHON3=$(which python3)

# Get silent env, default to 1
SILENT="${SILENT:-1}"

# Colors
BC="\n\033[0;32m"
NC="\033[0m\n"

function pprint() {
    local LOG
    local ARGS

    ARGS="$*"
    LOG="RSLV => $ARGS [$(date)]"

    if [[ $SILENT -eq 0 ]]; then
        echo -e "$BC$LOG$NC"
    elif [[ $SILENT -eq 1 ]]; then
        echo "$LOG" >>"$ENV_RSLV_DIR/.rslv.runtime.log"
    fi
}

function cli_rslv() {
    pprint "$CLIRSV_DIR"
    eval "PYTHONPATH=$ENV_RSLV_DIR $SYSTEM_PYTHON3 -m $MODULE" "$@"
}

cli_rslv "$@"
