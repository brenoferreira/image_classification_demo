#!/bin/bash
pipenv shell

FILES=images/*.jpg
for f in $FILES
do
  echo "Processing $f file..."
  runtime=`time lumi predict $f > $f.metadata`

  cat <<< "$runtime" > "$f.time"
  printf "%s" "$runtime" > "$f.time"
done
