FROM python:3.8.2-alpine3.11
LABEL MAINTAINER="jskii <blackdanieljames@gmail.com>"

ENV CONTAINERIZED=True
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
ADD download-otf-videos.py /app/download-otf-videos.py

ENTRYPOINT ["python3", "download-otf-videos.py"]