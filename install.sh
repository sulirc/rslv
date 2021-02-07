#!/bin/bash
set -e

RSLV="rslv"
ROOT_DIR=$HOME

# Use HOME to download rslv
cd $ROOT_DIR

# Delete rslv if exists.
rm -rf $RSLV

# Download new rslv
git clone https://github.com/sulirc/rslv.git
cd rslv

# Use makefile to setup env
make install

# Print version
rslv -h
