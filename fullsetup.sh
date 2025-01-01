#!/bin/bash
sudo apt-get update
sudo apt-get install -y ffmpeg portaudio19-dev alsa-utils mpg123
#sudo chmod u+s /usr/bin/vlc-wrapper deprecated
sudo python3 -m venv venv
source venv/bin/activate
sudo ./venv/bin/pip install -r requirements.txt
deactivate