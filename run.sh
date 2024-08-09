#!/bin/bash
file="$1" 
echo "$file"

fileLocal="$(pwd)/$file"
fileContainer="/in/$file"
outFolderLocal="$(pwd)/out/"
outFolderContainer='/out'

echo "lokale Datei: $fileLocal"
echo "Datei im Container: $fileContainer"
echo "lokaler Outputfolder: $outFolderLocal"
echo "Outputfolder im Container: $outFolderContainer"

docker run \
-e file_to_convert="$fileContainer" \
--mount type=bind,source="$fileLocal",target="$fileContainer" \
--mount type=bind,source="$outFolderLocal",target="$outFolderContainer" \
"opencv:latest" python3 upscale.py