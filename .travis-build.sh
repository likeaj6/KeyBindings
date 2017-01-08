#!/usr/bin/env bash


PLATFORM=$(uname)

if [ "$PLATFORM" != "Darwin" ]
then
    echo "ERROR: This script is macOS only."
fi

OUT=$(plutil -lint ./DefaultKeyBinding.dict)

if [ $? -ne 0 ]
then
    echo "ERROR: $OUT"
else
    echo "OK"
fi
