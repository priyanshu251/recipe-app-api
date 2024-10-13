FROM python:3.9-alpine3.13 
# name of image- python, name of tag- 3.9-alpine3.13. This simply means that we are using python version 3.9 on alpine version 3.13. alpine is a lightweight linux distribution(version of linux) which is used to create lightweight images.

LABEL maintainer="priyanshu251"
ENV PYTHONUNBUFFERED 1
# tells python to run in unbuffered mode and allows to print directly in he console without buffering.

COPY ./requirements.txt /tmp/requirements.txt
# copy the requirements.txt file from the local machine to the docker image. This is done to install the dependencies mentioned in the requirements.txt file.
COPY ./app /app
# copy the app folder(django app) from the local machine to the docker image.
WORKDIR /app
# this is the directory where the docker commands will be executed.
EXPOSE 8000
# expose the port 8000. This is done to allow the container to communicate with the outside world. Allows us to access the port on the container thats running from our image from the host machine.

#writing run commands to install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user

# ye sab dobara baad me smjh lena 