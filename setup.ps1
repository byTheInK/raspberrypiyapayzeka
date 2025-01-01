choco install -y ffmpeg vlc python313
echo "Gerekli yazılımlar indirildi."
Start-Sleep -Seconds 2

python -m venv venv
echo "Sanal ortam oluşturuldu."

.\venv\Scripts\Activate.ps1
echo "Paketler yükleniyor..."
Start-Sleep -Seconds 1

pip3 install -r requirements.txt
echo "Paketler yüklendi."

echo "Kurulum tamamlandı."
deactivate