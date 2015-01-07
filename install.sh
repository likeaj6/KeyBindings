#!/usr/bin/env bash

ROOT="$HOME"
TMP_DIR="/tmp/KeyBinding_$RANDOM"
FILE_PATH="$ROOT/Library/KeyBindings"

mkdir -p "$ROOT/Library/KeyBindings/"

curl https://raw.githubusercontent.com/zer4tul/KeyBindings/master/DefaultKeyBinding.dict -o "$FILE_PATH/DefaultKeyBinding.dict"

if [[ $(plutil -lint "$FILE_PATH/DefaultKeyBinding.dict") ]]
then
  plutil -convert xml1 $FILE_PATH/DefaultKeyBinding.dict
fi
