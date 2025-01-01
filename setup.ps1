python -m venv Venv
echo "Sanal ortam oluşturuldu."

.\Venv\Scripts\Activate.ps1
echo "Paketler yükleniyor..."
Start-Sleep -Seconds 1

.\Venv\Scripts\pip install -r requirements.txt
echo "Paketler yüklendi."

echo "Kurulum tamamlandı."
deactivate