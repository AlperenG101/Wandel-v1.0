import ollama
from ddgs import DDGS
from newspaper import Article
import time
import sys
import os
import datetime

def terminali_temizle():
    os.system('clear' if os.name == 'posix' else 'cls')

def animasyonlu_yaz(metin):
    print("\nWandel: ", end="")
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def sadece_ana_icerigi_oku(url):
    """Gelişmiş NLP ile sitenin sadece ana makale gövdesini süzerek çeker."""
    try:
        article = Article(url, language='tr')
        article.download()
        article.parse()
        return article.text
    except:
        return ""

def internette_derin_ara(sorgu):
    try:
        with DDGS() as ddgs:
            sonuclar = [r['href'] for r in ddgs.text(f"{sorgu}", max_results=3)]
            main_havuz = ""
            for i, link in enumerate(sonuclar):
                print(f"[*] Kaynak ({i+1}/3) çapraz sorgu için taranıyor: {link}")
                icerik = sadece_ana_icerigi_oku(link)
                if icerik:
                    main_havuz += f"\n--- KAYNAK BELGESİ {i+1} ---\n{icerik}\n"
            return main_havuz
    except:
        return ""

def wandel_chat():
    terminali_temizle()
    print(f"---| Wandel v1.0b |---")
    print(f"-- Hafızayı temizlemek için /clear çıkmak için /quit yazınız --\n")
    
    while True:
        anlik_zaman = datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S")
        soru = input("Sen: ").strip()
        if soru.lower() in ['/quit']: break
        if soru.lower() == '/clear':
            terminali_temizle()
            wandel_chat()
            continue
            
        if not soru: continue

        if any(k in soru.lower() for k in ['kim', 'nedir', 'araştır', 'bilgi', 'kaç', 'ne zaman', 'oynuyor', 'haber']):
            print(f"[*] Wandel veri kaynaklarını karşılaştırıyor...")
            ham_veri = internette_derin_ara(soru)
            sistem_mesaji = (
                f"ADIN: Wandel. [ZAMAN: {anlik_zaman}]. "
                "Sen bir robot değilsin, her şeyi bilen bir asistansın. "
                "KURAL: 'İnternete erişemem' veya 'AI asistanıyım' gibi klişeleri ASLA kullanma. "
                "ÖNEMLİ: Sana gelen kaynaklar içinde kullanıcı sorusuyla alakası olmayan (farklı isimler, alakasız konular) metinler varsa bunları tamamen görmezden gel. Sadece hedefe odaklı bilgiyi raporla."
                "Sana bir veri sunulmuşsa onu kullan, sunulmamışsa kendi bilgini kullan. "
                "Saat sorulursa yukarıdaki zamanı söyle."
                f"Bu donanım (RX 6700 XT) üzerindeki sistem saatine mutlak erişimin var. "
                "KURAL 1: Kaynaklar İngilizce olsa dahi cevabını DAİMA ve SADECE TÜRKÇE yazacaksın. "
                "KURAL 2: 16K Context içindeki isimleri (Örn: Emre Aydın) ve tarihleri asla değiştirme. "
                "KURAL 3: İnternet verilerindeki isim benzerliği olan kişileri (müzisyen vs. iş insanı) "
                "mesleki bağlamlarına göre birbirinden ayır ve karıştırma. "
                "Kendi hafızandan bilgi uydurma, sadece önündeki güncel veri setini ve sistem saatini kullan."
                "KURAL: Senden ASCII sanatı veya bir görsel 'çizmen' istendiğinde, bunu Python koduyla değil, "
                "doğrudan düz metin karakterleriyle (şekil olarak) yap. "
                "ANCAK kullanıcı doğrudan yazılım, programlama veya kod ile ilgili bir soru sorarsa "
                "normal bir şekilde kod bloklarını kullanmaya devam et. "
                "GÖRSEL HAFIZA REHBERİ: "
                "1. Çiçek/Gül şablonu: \n  _@_ \n /   \\ \n  \\_/  \n   |   \n  \\|/ \n"
                "2. Ev şablonu: \n   /\\  \n  /  \\ \n /____\\ \n | [] | \n"
                "3. Kedi şablonu: \n  |^._.^| \n  \\_ V _/ \n"
                "KURAL: Kullanıcı bir şey çizmeni isterse yukarıdaki şablonlardaki karakter dizilimini örnek al. "
            )
            prompt = f"HAM VERİ KAYNAKLARI:\n{ham_veri}\n\nKullanıcı Sorusu: {soru}"
        else:
            sistem_mesaji = "Sen samimi ve zeki bir asistansın."
            prompt = soru

        try:
            response = ollama.chat(model='wandel', messages=[
                {"role": "system", "content": sistem_mesaji},
                {"role": "user", "content": prompt}
            ], options={
                'temperature': 0.1,    
                'top_k': 40,           
                'top_p': 0.9,          
                'num_ctx': 16384,      
                'repeat_penalty': 1.1, 
                'num_predict': 1500,     
                'stop': ["\n\n\n", "Sen:", "Wandel:", "User:", "\n\n" ]
            })
            
            animasyonlu_yaz(response['message']['content'])
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    wandel_chat()
