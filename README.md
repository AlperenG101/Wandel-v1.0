🌌 Wandel AI v1.0<br>
Wandel, yerel makinenizde çalışan, internet erişimine sahip ve gelişmiş içerik analizi yapabilen hibrit bir yapay zeka asistanıdır. Ollama altyapısını kullanarak verilerinizi gizli tutar ve DuckDuckGo üzerinden güncel dünya verilerine ulaşır.

🚀 Kurulum Rehberi<br>
1. Sistem Hazırlığı (Tüm Ekran Kartları İçin)<br>
Wandel'in ekran kartınızdan (GPU) tam verim alabilmesi için önce Ollama'yı sisteminize kurmalısınız:<br>

Windows/Mac/Linux: ollama.com adresinden işletim sisteminize uygun sürümü indirin ve kurun.<br>

GPU Desteği: Ollama; NVIDIA (CUDA), AMD (ROCm) ve Apple Silicon (Metal) birimlerini otomatik tanır. Eğer ekran kartınız yoksa otomatik olarak İşlemci (CPU) modunda çalışacaktır.<br>

2. Python Bağımlılıkları<br>
Terminali açın ve gerekli kütüphaneleri yükleyin:<br>

Bash<br>
pip install ollama duckduckgo-search newspaper3k<br><br>
3. Wandel Modelini Oluşturma<br>
Wandel'in özel komut setini ve karakterini yüklemek için şu adımları izleyin:<br>

Proje klasöründe Modelfile adında bir dosya oluşturun.<br>

İçine şu satırı yazın: FROM llama3 (veya tercih ettiğiniz başka bir model örn: mistral).<br>

Terminalde şu komutu çalıştırarak Wandel'i sisteme kaydedin:<br>

Bash<br>
ollama create wandel -f Modelfile<br><br>
💻 Kullanım Talimatları<br>
Projeyi başlatmak için terminale şu komutu yazın:<br><br>

Bash<br>
python wandel.py<br><br>
Komutlar ve Özellikler:<br>
Soru Sorma: Doğrudan merak ettiğiniz şeyi yazın. Eğer sorunuzda "kim, nedir, haber, araştır" gibi anahtar kelimeler geçerse, Wandel otomatik olarak internete bağlanır.<br><br>

/clear: Sohbet geçmişini ve terminal ekranını temizler.<br>

/quit: Uygulamadan güvenli bir şekilde çıkar.<br>

Görsel Çizim: Wandel'den bir "kedi", "ev" veya "çiçek" çizmesini isterseniz, size özel ASCII karakterleriyle görsel oluşturur.<br>

🛠️ Donanım Uyumluluğu ve Performans<br>
Wandel, her türlü donanımda çalışacak şekilde optimize edilmiştir:<br>

NVIDIA Kullanıcıları: En iyi performans için güncel CUDA sürücülerinin yüklü olduğundan emin olun.<br>

AMD Kullanıcıları: Proje varsayılan olarak yüksek performanslı AMD kartları (Örn: RX 6700 XT) ile tam uyumludur.<br>

Düşük Sistemler/Sadece CPU: Eğer ekran kartınız zayıfsa, Modelfile içinde FROM llama3 yerine daha hafif olan FROM phi3 veya FROM tinydolphin kullanarak hızı artırabilirsiniz.<br><br>

📜 Lisans ve Geliştirici<br>
Bu proje Alperen tarafından geliştirilmiştir. Eğitim ve kişisel kullanım için açık kaynaklıdır.<br>

UYARI!: YAPAY ZEKANIN EKRAN KARTI ÜZERİNDE DÜZGÜN ÇALIŞMASI İÇİN MİNİMUM 12 GB EKRAN KARTI OLMASI GEREKLİDİR! 12 GB VRAM altındaki kartlarda modelin num_ctx değerini düşürmeniz gereklidir (wandel.py dosyasındaki num_ctx değeri).
