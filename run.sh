file="$1" 

echo "$file"
docker build -t "opencv:latest" .

docker run -it \
-e file_to_convert="$file" \
--mount type=bind,source="$(pwd)/$file",target="/$file" \
--mount type=bind,source="$(pwd)/out/",target="/out" \
"opencv:latest" bash