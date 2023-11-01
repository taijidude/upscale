FROM python:latest
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y ffmpeg libsm6 libxext6
RUN pip install opencv-contrib-python
RUN mkdir /out
RUN mkdir /in
COPY ./upscale.py /
COPY ./LapSRN_x2.pb /