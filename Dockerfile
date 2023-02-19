# base image is alphine
FROM alpine:latest

# update packages and install python3
RUN apk update \
    && apk add --no-cache python3 \
    && rm -rf /var/cache/apk/*
# copy the python code to container
COPY script.py /app/
#creating the output directory
RUN mkdir home/output
# Set the working directory
WORKDIR /app
#setting the entrypoint
ENTRYPOINT ["python3", "script.py"]

