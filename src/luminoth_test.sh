#!/bin/bash
pipenv shell

lumi checkpoint refresh
lumi checkpoint download accurate

FILES=images/*.jpg
for f in $FILES
do
  echo "Processing $f file..."
  runtime=`time lumi predict $f > $f.metadata`

  cat <<< "$runtime" > "$f.time"
  printf "%s" "$runtime" > "$f.time"
done
