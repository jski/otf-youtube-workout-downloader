# OTF workout local downloader
This tool can be used to download the videos from the Orangetheory official YouTube page in place during the nationwide shutdown of studios. By doing this, you can keep the videos even if they are deleted by OTF at the end of the shutdown, or if you want to move them to a device which has no internet connection.

## Prerequisites
For this tool you will need either **Python 3** (tested working on 3.8, but other versions are probably fine too), or **Docker**. Docker is a little easier as I'm also publishing the image to Dockerhub, but you can also build from source included here.

## Usage
- For running straight from Dockerhub image (easiest):
    1. `docker run -v $PWD/otf-videos:/app/otf-videos jski/otf-youtube-workout-downloader:latest`

- For building from source and using Docker:
    1. `docker-compose build`
    1. `docker-compose up`

- For running from local python:
    1. (Optional but recommended) Setup a virtual environment for this project in this folder.
    1. `pip install -r requirements.txt`
    1. `python download-otf-videos.py`

All three methods will put the files in a folder relative to your local path called /otf-videos. Running it multiple times will not redownload files, it will only download new ones you don't already have. I went with mp4 format as I imagine it is the most compatible with devices people would like to use to play them.

I have tested this on Windows 10 (Powershell Core 7) and MacOS. If you have any issues, feel free to let me know in the Issues tab above. Thanks!