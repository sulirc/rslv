#!/bin/bash

ROOT_DIR=$(pwd)
CLIRSV_DIR="$ROOT_DIR/cliresolve/__main__.py"

function cli_rslv() {
  eval "$CLIRSV_DIR $@"
}

cli_rslv "$@"