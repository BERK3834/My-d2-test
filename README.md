 🧠 D2 Dikkat Testi (Tkinter ile)

Bu proje, **dikkat ve seçici odaklanma** becerilerini ölçmeyi amaçlayan klasik D2 testinin dijital bir simülasyonudur. `Tkinter` kütüphanesi kullanılarak Python ile geliştirilmiştir. Test, eğitim ve deneysel uygulama amaçlıdır; klinik tanı koyma veya psikolojik değerlendirme amacıyla kullanılmamalıdır.

---

## 📌 Amaç

Bu yazılım; bireylerin görsel seçici dikkatini ölçmeyi hedefleyen, D2 dikkat testine benzer bir ortam sağlar. Katılımcı, 14 satırlık bir dizi karakter içinde sadece hedef öğeleri (`d--`) bulup tıklamakla görevlidir.

---

## 🎮 Uygulama Kuralları

- Her satırda çeşitli semboller vardır.
- Amaç yalnızca **`d--`** şeklinde yazılmış olan karakterleri tıklamaktır.
- Her satır için **20 saniye süreniz vardır**.
- Doğru tıklamalar yeşil, yanlışlar kırmızı renkle gösterilir.
- Tüm satırlar tamamlandığında:
  - Doğru cevap sayısı
  - Yanlış cevap sayısı
  - Hata oranı
  - Başarı puanı hesaplanır.

---

## 🖥️ Arayüz Özellikleri

- **Tkinter GUI** tabanlı modern pencere yapısı
- **Otomatik zamanlayıcı** ile her satır için geri sayım
- **Scroll destekli canvas**, uzun satırlar için yatay kaydırma
- Test sonuçlarının görsel sunumu ve yeniden başlama seçeneği

---

## 🧪 Teknik Detaylar

- Her satırda rastgele 47 karakter bulunur.
- Bu karakterlerin 4 ila 7 tanesi gerçek hedeftir (`d--`).
- Diğerleri rastgele olarak `"b-"`, `"p"`, `"d"`, `"p--"`, `"d-"` gibi dikkat dağıtıcı karakterlerden seçilir.
- Skorlama:
  - **+10 puan** doğru seçim başına
  - **–5 puan** yanlış seçim başına
- Hata oranı: `(yanlış / toplam tıklama) * 100`

---

## 🚀 Uygulamayı Çalıştırma

### Gereksinimler

- Python 3.x

Tkinter, Python ile birlikte geldiğinden ayrıca yüklemeniz gerekmez. Yine de eksikse:

```bash
pip install tk
Başlatma
bash
Kopyala
Düzenle
python d2_test.py
📂 Dosya Yapısı
bash
Kopyala
Düzenle
d2_test/
│
├── d2_test.py            # Ana test uygulaması
├── README.md             # Açıklama ve kullanım belgesi (bu dosya)
📊 Örnek Çıktı (Test Sonu)
makefile
Kopyala
Düzenle
Test Tamamlandı!
Doğru: 61 | Yanlış: 9
Hata Oranı: %12.86 | Başarı Puanı: 565
⚠️ Uyarı
Bu proje gerçek bir psikolojik test değildir. Klinik veya akademik değerlendirmede kullanılamaz. Sadece programlama eğitimi ve bilişsel süreçleri simüle etmek için geliştirilmiştir.

👨‍💻 Geliştirici Notu
Bu uygulama, özellikle psikoloji ve bilişsel bilim alanlarında çalışan geliştiriciler için örnek teşkil edebilir. Test yapısının zaman yönetimi, dikkat dağıtıcı ögeler ve kullanıcı etkileşimi bakımından modellenmesi önemlidir. Kod, kolayca farklı kurallara veya hedef türlerine göre genişletilebilir.




📘 English Description Below
🧠 D2 Attention Test (Tkinter-Based Simulation)
This project is a digital simulation of the classic D2 Test of Attention, designed to assess selective attention and focus abilities. It is built using Python's Tkinter library and intended for educational and experimental purposes only — not for clinical or diagnostic use.

📌 Purpose
This software provides an environment similar to the D2 test, where users are asked to locate and click on target characters (d--) within 14 rows of mixed symbols.

🎮 Test Rules
Each row contains various characters.

Only symbols written as d-- are considered correct targets.

You have 20 seconds for each row.

Correct clicks are marked green; incorrect ones in red.

After all rows are completed:

Correct answer count

Incorrect answer count

Error rate

Performance score are displayed.

🖥️ Interface Features
Modern GUI using Tkinter

Built-in countdown timer for each row

Scrollable canvas for navigating wide rows

Final score display with restart option

🧪 Technical Details
Each row contains 47 randomly placed characters.

4 to 7 of these are valid targets (d--).

Distractors are randomly chosen from variants like "b-", "p", "--p", "d-", etc.

Scoring:

+10 points for each correct click

–5 points for each incorrect click

Error Rate Formula: (false positives / total responses) * 100

🚀 Running the Application
Requirements
Python 3.x

Tkinter is included with Python by default. If missing:

bash
Kopyala
Düzenle
pip install tk
Start
bash
Kopyala
Düzenle
python d2_test.py
📂 File Structure
bash
Kopyala
Düzenle
d2_test/
│
├── d2_test.py            # Main test application
├── README.md             # This readme file
📊 Example Output (After Test Completion)
yaml
Kopyala
Düzenle
Test Completed!
Correct: 61 | Incorrect: 9
Error Rate: 12.86% | Performance Score: 565
⚠️ Disclaimer
This application is not a real psychological test and should not be used for clinical, diagnostic, or academic assessment purposes. It is created solely for educational and simulation use.

👨‍💻 Developer Note
This project can serve as a helpful example for developers working in psychology, cognitive science, or human-computer interaction. It demonstrates time management, distraction mechanisms, and user interaction within cognitive testing. The system is modular and can be adapted to different scoring rules or visual patterns.
