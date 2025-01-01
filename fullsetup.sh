#!/bin/bash
sudo apt-get update
echo "Sistem güncellendi."
sleep 2

sudo apt-get install -y ffmpeg portaudio19-dev alsa-utils vlc python3-full
echo "Gerekli yazılımlar indirildi."
sleep 1

sudo chmod u+s /usr/bin/vlc-wrapper
echo "VLC ayarlandı."
sleep 2

sudo python3 -m venv venv
echo "Sanal ortam oluşturuldu."
sleep 2

source venv/bin/activate
echo "Paketler yükleniyor..."
sleep 1

sudo ./venv/bin/pip install -r requirements.txt
echo "Paketler yüklendi."
sleep 3
echo "Kurulum tamamlandı."
deactivate