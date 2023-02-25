#!/usr/bin/env python
# -*- coding: utf-8 -*-
# EKODE
"""
    EKODE
    EKODE, metni resim üzerinde saklamak için kullanılan bir algoritmadır.

    Geliştirici: Emre Kayık
    E-posta: emrekayik1905@gmail.com
    Sürüm: 0.0.2
    Durum: Geliştirme
    Lisans: MIT
    Kaynak:
        https://en.wikipedia.org/wiki/Hue
        https://docs.python.org/3/library/colorsys.html
        https://pillow.readthedocs.io/en/stable/reference/index.html
        
"""

from PIL import Image, ImageDraw
import colorsys

# Metni Şifreleyen Fonksiyon
def EKODE(text):
    # Metni büyük harfe çevirme ve boşlukları kaldırma
    text.replace(" ", "")

    # Metni ASCII kodlarına çevirme
    ascii = list(bytes(text, "ascii"))

    # Renkler için dizi tanımlama
    ascii_color = []

    # Resim boyutları ve her karenin boyutunu ayarlama
    square_size = 40
    width = square_size * len(ascii)
    height = square_size

    # Hsl renklerini ayarlama
    for i in ascii:
        # Lineer Dönüşüm, kullanarak 48-90 arasındaki ascii kodları için çalışmasını sağladım. Küçük karakterler için çalışmayacaktır.
        # Bu metodla her bir ascii kodu değeri 0-360 arası bir değer aldı. Hue için gerekli aralık yani
        h, s, l = (360 / 43) * (i - 48), 100, 50

        # ascii renkleri dizisine  her bir rengi gönderiyorum
        ascii_color.append("hsl({}, {}%, {}%)".format(h, s, l))

     # Resim nesnesini oluşturun ve Draw sınıfını kullanarak kareleri çizme
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    # Metindeki her bir karakter için bir kare çizme
    for i in range(len(text)):
        x0, y0 = i * square_size, 0
        x1, y1 = x0 + square_size, square_size
        # Kareleri çizme
        draw.rectangle((x0, y0, x1, y1), fill=ascii_color[i])

    # Resmi kaydetme
    image.save("output.png")

# Resmi Çözümleyen Fonksiyon
def EKODEdecrypt(image,text_length):
  # Resmi aç
  image = Image.open(image)
  # Çözümlenirken verilecek çıktı
  metinCiktisi = []
  for i in range(len(text_length)):
    # RGB to HSL
    # # Pikselin RGB kodunu alın
    r, g, b = image.getpixel((20+i*40,20))
    # RGB kodunu HSL koduna dönüştürün
    hue = rgb2hue(r, g, b)
    # Hue kodunu al
    # (360 / 43) * (i - 48) Tersini al
    deger = (43 * (hue / 360)) + 48
    metinCiktisi.append(chr(round(deger)))
  return metinCiktisi

def rgb2hue(r,g,b):
    # RGB kodunu 0-1 aralığına dönüştürün
    r_norm, g_norm, b_norm = r/255, g/255, b/255
    # RGB kodunu HSL koduna dönüştürün
    h, l, s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)
    # Hue değerini grad olarak yazdırın
    hue = round(h * 360)
    return hue


text = "EMRE"
EKODE(text)

print(EKODEdecrypt("output.png",text))

