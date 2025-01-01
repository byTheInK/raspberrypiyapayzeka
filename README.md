Bu yapay zeka Raspberry PI için tasarlanmıştır ve Google'ın Gemma modelini kullanır.
Uyarı: API herkese açıktır fakat ileride değişebilir.

# Gerekli aygıtlar
- Mikrofon
- Hoparlör

# Gerekli yazılımlar
- Python
- Vlc
- Portaudio
- Alsa-Utils
- Ffmpeg

# Bash (Linux)
Bash çoğu Linux dağıtımında kullanılan varsayılan komut sistemidir. Debian, Ubuntu, Arch hatta Slackware bile bu komut sistemini kullanır. Ayrıca Wsl sayesinde kullanabilirsiniz ama bu projeyi Wsl aracılığıyla kullanamazsınız çünkü Wsl, ses girişlerine şuanda izin vermiyor.

## Otomatik kurulum
Otomatik kurulum, betik dosyalarıyla kurmanızı sağlar. Manuel kurulumdan çok daha anlaşılabilir ve kolaydır.

Kurulum:
```bash
sudo apt-get install -y git
cd /home
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source fullsetup.sh
```

Güncelleme:
```bash
cd /home
sudo rm -rf RaspberryPIYapayZeka
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source fullsetup.sh
```

Calıştırma:
```bash
cd /home/RaspberryPIYapayZeka
source linuxrun.sh
```

## Manuel kurulum
Kurulum:
```bash
cd /home
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
sudo apt-get update
sudo apt-get install -y ffmpeg portaudio19-dev alsa-utils vlc python3-full
sudo chmod u+s /usr/bin/vlc-wrapper
sudo python3 -m venv venv
source venv/bin/activate
sudo ./venv/bin/pip install -r requirements.txt
deactivate
```

Güncelleme:
```bash
sudo apt-get install -y git
sudo rm -rf /home/RaspberryPIYapayZeka
cd /home
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
sudo apt-get update
sudo apt-get install -y ffmpeg portaudio19-dev alsa-utils vlc python3-full
sudo chmod u+s /usr/bin/vlc-wrapper
sudo python3 -m venv venv
source venv/bin/activate
sudo ./venv/bin/pip install -r requirements.txt
deactivate
```

Calıştırma:
```bash
cd /home/RaspberryPIYapayZeka
source linuxrun.sh
```