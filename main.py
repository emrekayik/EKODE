from PIL import Image, ImageDraw, ImageColor
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

text = "EMRE"
EKODE(text)

