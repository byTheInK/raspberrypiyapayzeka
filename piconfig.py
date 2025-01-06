SES_KAYIT_KAYIT_SURESI: int = 6 # Saniye biçiminde bir tam sayı giriniz VARSAYILAN = 6
SES_KAZANC_BOYUTU: int = 10 # Sesin ne kadar yükseleceğini belirler VARSAYILAN = 10
SES_FREKANS_DEGERI: int = 44100 # Sesin frekansını belirler VARSAYILAN DEĞER = 44100
BASLANGICTA_HAFIZAYI_SIL: bool = False # Kod başladığında hafızayı siler veya silmez(False=hayır,True=evet) VARSAYILAN = False
HAFIZAYI_AKILDA_TUTMA_SINIRI: bool = 2000 # Aklında en son kaç mesajı tutabileceğini ayarlar VARSAYILAN = 20
HATA_AYIKLAMA: bool = False # Hata ayıklama modunu açar veya kapatır VARSAYILAN = False
SABIT_DEGERLER: dict = {"Language":"Türkçe"} # Buraya yapay zekanın asla unutmaması gereken değerleri yazınız

# yedek.json dosyasının üzerinde yazılır
# > # < ifadesi olduğu satırı yorum yapar yani koda etki etmez.
# BASLANGICTA_HAFIZAYI_SIL ifadesini açarsan OTHER klasöründe yedek.json dosyasının içerisinde verilerini tekrar bulabilirsin
# Hafızasında ne kadar fazla mesaj tutarsa o kadar yavaş yanıt verir ve alan kaplar
# Frekans değeriyle oynarsanız yapay zeka sesi anlamayabilir bu nedenle 44100 değerinde tutulması önerilir