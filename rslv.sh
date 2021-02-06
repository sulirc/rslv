#!/bin/bash
set -e

ROOT_DIR=$(pwd)
MODULE="cliresolve"
CLIRSV_DIR="$ROOT_DIR/$MODULE"

# Get silent env, default to 0
SILENT="${SILENT:-0}"

# Colors
BC="\n\033[0;32m"
NC="\033[0m\n"

function pprint() {
    local LOG="CLSV => $@ [$(date)]"

    if [[ $SILENT -eq 0 ]]; then
        echo -e $BC$LOG$NC
    elif [[ $SILENT -eq 1 ]]; then
        echo $LOG >>rslv.runtime.log
    fi
}

function cli_rslv() {
    pprint "$CLIRSV_DIR"
    eval "python3 -m $MODULE $@"
}

cli_rslv "$@"
