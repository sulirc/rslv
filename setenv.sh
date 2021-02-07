#!/bin/bash

RSLV="rslv.sh"
CLIRSLV=".rslv.sh"

cp $RSLV $CLIRSLV
chmod u+x $CLIRSLV
sed -i '' "s~ENV_RSLV_DIR=.*~ENV_RSLV_DIR=$ENV_RSLV_DIR~" $CLIRSLV
