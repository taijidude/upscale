file="$1" 
echo "$file"

docker run \
-e file_to_convert="$file" \
--mount type=bind,source="$(pwd)/$file",target="/in/$file" \
--mount type=bind,source="$(pwd)/out/",target="/out" \
"opencv:latest" python ./upscale.py $file