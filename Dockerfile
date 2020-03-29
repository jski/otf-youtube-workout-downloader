# Whole cloth lifted from https://github.com/GoogleContainerTools/distroless/blob/a7156f6ff9d15892e726dd2368cb2383d40f9d04/examples/python3-requirements/Dockerfile
FROM debian:buster-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM gcr.io/distroless/python3-debian10
LABEL MAINTAINER="jskii <blackdanieljames@gmail.com>"
COPY --from=build-venv /venv /venv
COPY download-otf-videos.py /app/download-otf-videos.py
WORKDIR /app
ENTRYPOINT ["/venv/bin/python3", "download-otf-videos.py"]