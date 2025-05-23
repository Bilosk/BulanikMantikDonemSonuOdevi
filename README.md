# 🔥❄️ Akıllı Isıtma ve Soğutma Kontrol Sistemi

## 🧠 Proje Özeti

Bu proje, oda içi sıcaklık koşullarını optimize etmek amacıyla geliştirilmiş, **bulanık mantık tabanlı** bir kontrol sistemidir. Kullanıcıdan alınan 5 farklı çevresel ve kişisel veriye göre, **ısıtma ve soğutma oranlarını otomatik olarak hesaplar**.

Geliştirilen sistem, geleneksel termostatlara kıyasla daha **esnek ve sezgisel** kararlar verir. Arayüzü sayesinde kullanıcı dostu bir şekilde kullanılabilir.

---

## 🎯 Amaç

Modern yaşam alanlarında enerji verimliliğini korurken kullanıcı konforunu maksimize etmek. Bunun için:

- Ortam koşullarını dikkate alan
- Kullanıcı tercihlerini içeren
- Dinamik bir sistem geliştirilmiştir.

---

## 🔧 Kullanılan Teknolojiler

| Teknoloji       | Açıklama                                 |
|-----------------|------------------------------------------|
| Python 3.10+     | Programlama dili                        |
| scikit-fuzzy    | Bulanık mantık kontrol sistemi için      |
| matplotlib      | Grafiksel çıktı gösterimi                |
| Tkinter         | GUI (grafik kullanıcı arayüzü) için      |
| numpy / scipy   | Sayısal hesaplamalar için                |
| networkx        | scikit-fuzzy içinde görsel mantık işlemleri için |

---

## 🧮 Girdi Değişkenleri

| Değişken            | Aralık         | Açıklama                                  |
|---------------------|----------------|-------------------------------------------|
| 🏠 Oda Sıcaklığı     | 10 – 35 °C     | Ortam içi sıcaklık                        |
| 🌡️ Dış Sıcaklık      | –10 – 40 °C    | Dış hava sıcaklığı                        |
| 🎚️ Konfor Tercihi   | 1 – 10         | 1 = serin seven, 10 = sıcak seven         |
| 🕒 Günün Saati       | 0 – 24         | 0 = gece, 12 = öğle, 18 = akşam vb.       |
| ⚡ Enerji Maliyeti   | 0.1 – 1.0 ₺    | Anlık elektrik birim fiyatı (₺/kWh)       |

---

## 🧾 Çıktı Değişkenleri

| Çıktı             | Aralık      | Açıklama                  |
|------------------|-------------|---------------------------|
| 🔥 Isıtma Gücü     | 0 – 100 %   | Isıtma sistemine gönderilecek güç seviyesi |
| ❄️ Soğutma Gücü    | 0 – 100 %   | Soğutma sistemine gönderilecek güç seviyesi |

---

## 🧠 Bulanık Mantık Yaklaşımı

Proje, klasik if–else mantığı yerine **bulanık kurallar (fuzzy rules)** kullanır. Örneğin:

> Eğer oda sıcaklığı “soğuk” VE dış sıcaklık “çok soğuk” VE kullanıcı “sıcak sever” ise → **Isıtmayı yüksek yap**

Toplamda **10 adet çok kriterli kural** kullanılmıştır. Girdiler, **üçgen üyelik fonksiyonları (trimf)** ile modellenmiş ve `Mamdani` çıkarım sistemi tercih edilmiştir.

---

## 🖥️ Arayüz (GUI)

GUI, **Tkinter** ile geliştirilmiştir ve şu özelliklere sahiptir:

- Girdiler için kaydırıcılar (scale)
- Tek tuşla “Hesapla” işlemi
- Grafiksel çıktı: Matplotlib ile bar grafik
- Anlık ısıtma ve soğutma oranları gösterimi

![Ekran Görüntüsü](ekran_goruntusu.png)

---

## 🚀 Kurulum Talimatları

1. Python 3.10+ yüklü olduğundan emin olun.
2. Projeyi klonlayın:

```bash
git clone https://github.com/kullaniciadi/fuzzy-climate-control.git
cd fuzzy-climate-control
