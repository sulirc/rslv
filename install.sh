#!/bin/bash
set -e

RSLV="rslv"
ROOT_DIR=$HOME

# Use HOME to download rslv and delete rslv if exists.
cd "$ROOT_DIR" && rm -rf $RSLV

# Download new rslv
git clone https://github.com/sulirc/rslv.git
cd rslv

# Install dependencies
pip3 install -r requirements.txt

# Use makefile to setup env
make install

# Print version
rslv -v
