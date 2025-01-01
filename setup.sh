#!/bin/bash
sudo python3 -m venv venv
source venv/bin/activate
sudo ./venv/bin/pip install -r requirements.txt
deactivate