#!/bin/sh

CONFIGURATION="Release"
[ $# -ge 1 ] && CONFIGURATION=$1

echo "Run tests in ./out/$CONFIGURATION"
for program in $(ls ./out/$CONFIGURATION/*_unittest.bin); do
    echo "== $program =="
    $program
done

