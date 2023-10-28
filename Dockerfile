FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install opencv-contrib-python
RUN apt-get install -y vim
RUN apt-get install -y ffmpeg libsm6 libxext6
COPY ./upscale.py /
# COPY *.png /
# COPY ./LapSRN_x8.pb /
# COPY ./LapSRN_x4.pb /
COPY ./LapSRN_x2.pb /