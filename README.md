Bu yapay zeka Raspberry PI için tasarlanmıştır ve Google'ın Gemma modelini kullanır. Gemma ile iletişime geçmek için Groq kullanır. Eğer bu yapay zekayı internet olmadan kullanıyorsanız bölümüne bakın.

# Gerekli aygıtlar
- Mikrofon
- Hoparlör

# Gerekli yazılımlar (kurulum sırasında yüklenicek)
- Python
- Vlc
- Portaudio
- Alsa-Utils
- Ffmpeg

# Bash (Debian/Ubuntu)
Bash çoğu Linux dağıtımında kullanılan varsayılan komut sistemidir. Debian, Ubuntu, Arch hatta Slackware bile bu komut sistemini kullanır fakat bu kurulum sadece Debian ve Ubuntu için geçerlidir. Ayrıca Wsl sayesinde kullanabilirsiniz ama bu projeyi Wsl aracılığıyla kullanamazsınız çünkü Wsl, ses girişlerine şuanda izin vermiyor.

Kurulum:

İlk olarak bir API anahtarı alın. Bu anahtar sizin yapay zekayla iletişime geçmenizi sağlayacak. API değerinin belirli bir sınırı vardır fakat bu sizi pek de etkilemeyecektir. [Buradan](https://console.groq.com/keys) bir API anahtarı alabilirsiniz. Aşağıdaki kod ile sisteme bu API anahtarını geçirebilirsiniz.

```bash
echo "API_ANAHTARINIZ" > ~/.config/RaspberryPIYapayZeka # API_ANAHTARINIZ kısmına anahtarınızı yazın
```

```bash
sudo apt-get install -y git
cd ~
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source setup.sh
```

Güncelleme:
```bash
cd ~
sudo rm -rf RaspberryPIYapayZeka
sudo git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
source setup.sh
```

Calıştırma:
```bash
cd ~/RaspberryPIYapayZeka
source run.sh
```

# Powershell (Windows)
Powershell, Windows işletim sisteminin iki ana komut sisteminden birisidir. Powershell Linux'da da kullanılabilmesine rağmen pek kullanılmıyor.İlk olarak Python, Git ve Ffmpeg programlarını indirin. Sonra Powershell'i açın.

Kurulum:

İlk olarak bir API anahtarı alın. Bu anahtar sizin yapay zekayla iletişime geçmenizi sağlayacak. API değerinin belirli bir sınırı vardır fakat bu sizi pek de etkilemeyecektir. Buradan bir API anahtarı alabilirsiniz. Aşağıdaki kod ile sisteme bu API anahtarını geçirebilirsiniz.

```powershell
cd $env:LOCALAPPDATA
New-Item -Path ".\RaspberryPIYapayZeka" -ItemType "File"
Set-Content -Path ".\RaspberryPIYapayZeka" -Value "API_ANAHTARINIZ"
```

```bash
cd $env:APPDATA
git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
cd RaspberryPIYapayZeka
.\setup.ps1
```

Güncelleme:
```bash
cd $env:APPDATA
rm -Force ".\RaspberryPIYapayZeka"
git clone https://github.com/byTheInK/RaspberryPIYapayZeka.git
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
### Otomatik
```bash
cd ~/RaspberryPIYapayZeka
source ./OTHER/setstart
```

### Manuel
İlk olarak `crontab -e` yazın. Eğer burada bir "1-2-3-4-5-6-7" gibi seçeneklerin bulunduğu bir yazı gelirse burada `2`'yi seçin. Bir metin dosyası önünüze çıktıktan sonra burada en aşağıya, satırın başında `#` sembolü olmayan bir yere inin ve buraya `@reboot ~/RaspberryPIYapayZeka/OTHER/startup.sh` yazın. Bunu yazdıktan sonra `Control` ve `x` tuşlarına basın, `y` tuşuna basın ve devam edin.

## Powershell (Windows)
Powershell'de işlem çok basit. Sadece Powershell'i ayönetici olarak çalıştırın ve aşağıdaki kodu yapıştırın.
```powershell
cd $env:APPDATA
Move-Item -Path ".\RaspberryPIYapayZeka\OTHER\startup.ps1" -Destination $([Environment]::GetFolderPath('Startup'))
```