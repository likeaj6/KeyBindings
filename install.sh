#!/usr/bin/env bash

ROOT="$HOME"
FILE_PATH="$ROOT/Library/KeyBindings"
RAW_FILE="https://raw.githubusercontent.com/zer4tul/KeyBindings/master/DefaultKeyBinding.dict"

mkdir -p "$FILE_PATH"

curl $RAW_FILE -o "$FILE_PATH/DefaultKeyBinding.dict"

if [[ $(plutil -lint "$FILE_PATH/DefaultKeyBinding.dict") ]]
then
  plutil -convert xml1 $FILE_PATH/DefaultKeyBinding.dict
fi
