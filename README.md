🌌 Wandel AI v1.0
Wandel, yerel makinenizde çalışan, internet erişimine sahip ve gelişmiş içerik analizi yapabilen hibrit bir yapay zeka asistanıdır. Ollama altyapısını kullanarak verilerinizi gizli tutar ve DuckDuckGo üzerinden güncel dünya verilerine ulaşır.

🚀 Kurulum Rehberi
1. Sistem Hazırlığı (Tüm Ekran Kartları İçin)
Wandel'in ekran kartınızdan (GPU) tam verim alabilmesi için önce Ollama'yı sisteminize kurmalısınız:

Windows/Mac/Linux: ollama.com adresinden işletim sisteminize uygun sürümü indirin ve kurun.

GPU Desteği: Ollama; NVIDIA (CUDA), AMD (ROCm) ve Apple Silicon (Metal) birimlerini otomatik tanır. Eğer ekran kartınız yoksa otomatik olarak İşlemci (CPU) modunda çalışacaktır.

2. Python Bağımlılıkları
Terminali açın ve gerekli kütüphaneleri yükleyin:

Bash
pip install ollama duckduckgo-search newspaper3k
3. Wandel Modelini Oluşturma
Wandel'in özel komut setini ve karakterini yüklemek için şu adımları izleyin:

Proje klasöründe Modelfile adında bir dosya oluşturun.

İçine şu satırı yazın: FROM llama3 (veya tercih ettiğiniz başka bir model örn: mistral).

Terminalde şu komutu çalıştırarak Wandel'i sisteme kaydedin:

Bash
ollama create wandel -f Modelfile
💻 Kullanım Talimatları
Projeyi başlatmak için terminale şu komutu yazın:

Bash
python wandel.py
Komutlar ve Özellikler:
Soru Sorma: Doğrudan merak ettiğiniz şeyi yazın. Eğer sorunuzda "kim, nedir, haber, araştır" gibi anahtar kelimeler geçerse, Wandel otomatik olarak internete bağlanır.

/clear: Sohbet geçmişini ve terminal ekranını temizler.

/quit: Uygulamadan güvenli bir şekilde çıkar.

Görsel Çizim: Wandel'den bir "kedi", "ev" veya "çiçek" çizmesini isterseniz, size özel ASCII karakterleriyle görsel oluşturur.

🛠️ Donanım Uyumluluğu ve Performans
Wandel, her türlü donanımda çalışacak şekilde optimize edilmiştir:

NVIDIA Kullanıcıları: En iyi performans için güncel CUDA sürücülerinin yüklü olduğundan emin olun.

AMD Kullanıcıları: Proje varsayılan olarak yüksek performanslı AMD kartları (Örn: RX 6700 XT) ile tam uyumludur.

Düşük Sistemler/Sadece CPU: Eğer ekran kartınız zayıfsa, Modelfile içinde FROM llama3 yerine daha hafif olan FROM phi3 veya FROM tinydolphin kullanarak hızı artırabilirsiniz.

📜 Lisans ve Geliştirici
Bu proje Alperen tarafından geliştirilmiştir. Eğitim ve kişisel kullanım için açık kaynaklıdır.

UYARI!: YAPAY ZEKANIN EKRAN KARTI ÜZERİNDE DÜZGÜN ÇALIŞMASI İÇİN MİNİMUM 12 GB EKRAN KARTI OLMASI GEREKLİDİR! 12 GB VRAM altındaki kartlarda modelin num_ctx değerini düşürmeniz gereklidir (wandel.py dosyasındaki num_ctx değeri).
