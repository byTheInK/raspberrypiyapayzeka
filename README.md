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

Kurulum:
```bash
sudo apt-get install -y git
cd /home
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source setup.sh
```

Güncelleme:
```bash
cd /home
sudo rm -rf RaspberryPIYapayZeka
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source setup.sh
```

Calıştırma:
```bash
cd /home/RaspberryPIYapayZeka
source run.sh
```

# Powershell (Windows)
Powershell, Windows işletim sisteminin iki ana komut sisteminden birisidir. Powershell Linux'da da kullanılabilmesine rağmen pek kullanılmıyor.

Kurulum:

İlk olarak Python, Git ve Ffmpeg programlarını indirin. Sonra Powershell'i açın.

```bash
cd $env:APPDATA
git clone RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
.\setup.ps1
```

Güncelleme:
```bash
cd $env:APPDATA
rm -Force ".\RaspberryPIYapayZeka"
git clone RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
.\setup.ps1
```

Calıştırma:
```bash
cd $env:APPDATA
cd RaspberryPIYapayZeka
.\run.ps1
```

# Sistem başlatıldığında çalıştırma

## Bash (Linux)
İlk olarak `crontab -e` yazın. Eğer burada bir "1-2-3-4-5-6-7" gibi seçeneklerin bulunduğu bir yazı gelirse burada `2`'yi seçin. Bir metin dosyası önünüze çıktıktan sonra burada en aşağıya, satırın başında `#` sembolü olmayan bir yere inin ve buraya `@reboot /home/RaspberryPIYapayZeka/OTHER/startup.sh` yazın. Bunu yazdıktan sonra `Control` ve `x` tuşlarına basın, `y` tuşuna basın ve devam edin.

## Powershell (Windows)
Powershell'de işlem çok basit. Sadece Powershell'i ayönetici olarak çalıştırın ve aşağıdaki kodu yapıştırın.
```powershell
cd $env:APPDATA
Move-Item -Path ".\RaspberryPIYapayZeka\OTHER\startup.ps1" -Destination $([Environment]::GetFolderPath('Startup'))
```