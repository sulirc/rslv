#!/bin/bash

RSLV="rslv.sh"
sed -i '' "s~ENV_RSLV_DIR=.*~ENV_RSLV_DIR=$ENV_RSLV_DIR~" $RSLV