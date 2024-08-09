FROM python:latest
RUN apt-get update
RUN apt-get install -y ffmpeg libsm6 libxext6
RUN pip install opencv-contrib-python
RUN pip install typer
RUN mkdir /upscale 
COPY ./upscale.py /upscale/
COPY ./LapSRN_x2.pb /upscale/