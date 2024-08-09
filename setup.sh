#!/bin/bash
sudo apt-get update && 
sudo apt-get install -y ffmpeg libsm6 libxext6 &&
pip install opencv-contrib-python && 
pip install pillow
pip install typer