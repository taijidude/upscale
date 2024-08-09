# Upscale Images 

# Overview 

Sorry for this hastly wrote down readme. As i write this i try to backup my computer. 

This is a small Python and Docker Project to upscale images using opencv. 

You can find the article it is beased on here: 

https://learnopencv.com/super-resolution-in-opencv/

The core of the project is the following Python script: 

link:upscale.py[]

The python file get copied into the docker container during build. (This is intendet for Docker Desktop on Windows atm)

link:Dockerfile[]

The last important fill is the shell script that puts everything together. You have to call the script with the image file Name as a parameter. The script will rebuild the docker file. Map everything and than open up a bash shell in the container. 

link:run.sh[]

== Todos

* [ ] I still have to run the upscale script manually in the container. I need to fix this. 
* [ ] Is it the out folder automatically created? 
* [ ] Setup a seperate script to build the container. 