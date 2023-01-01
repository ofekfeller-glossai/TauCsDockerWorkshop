FROM python:3.8.12-slim

RUN pip install pathlib
RUN pip install moviepy


# Copy all code from this directory into the docker's /home/code directory
COPY . /home/code

# This is the Docker image's default entrypoint
ENTRYPOINT ["python3", "/home/code/main.py"]