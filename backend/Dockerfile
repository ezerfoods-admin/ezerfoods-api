# Use slim-buster docker image for Python 3.10
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /backend

# Add environment variables to prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Add environment variables to prevent python from buffering stdout and stderr.
ENV PYTHONBUFFERED 1

# Install system dependencies
RUN apt-get update \
  && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip
# Copy requirements FILE
COPY ./requirements.txt /backend/requirements.txt
# Install dependencies in requirements file
RUN pip install -r requirements.txt
# Copy app into backend folder
COPY . /backend
