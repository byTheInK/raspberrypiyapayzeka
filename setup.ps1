python -m venv Venv
echo "Sanal ortam oluşturuldu."

.\Venv\Scripts\Activate.ps1
echo "Paketler yükleniyor..."
Start-Sleep -Seconds 1

pip3 install -r requirements.txt
echo "Paketler yüklendi."

echo "Kurulum tamamlandı."
deactivate