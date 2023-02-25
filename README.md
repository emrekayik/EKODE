# EKODE (0.0.2)

## Amaç

Metin girdisi alınarak, her harfin ASCII koduna göre belirlenen renklerle oluşturulan bir kareler kümesi oluşturmak. Bu sayede metni şifrelemek ve anlamsız gibi görülen kare kümelerinde metin saklamak.

## Kullanılan Teknolojiler

- Python 3.10.8
- Pillow (Python Imaging Library)

## Çalışma Prensibi

1. Kullanıcıdan metin girdisi alınır.
2. Metin, harf harf ayıklanarak ASCII koduna dönüştürülür.
3. Her harfin ASCII koduna karşılık geler bir renk tonu oluşturulur. Bu renk tonu HSL renk modeli kullanılarak hesaplanır.
4. Her harf için bir kare oluşturulur ve karenin o rengi, o harfin ASCII koduna karşılık gelen renk tonuna göre belirlenir. 
5. Kareler, yan yana şekilde sıralanır.

## ASCII koduna karşılık renk nasıl bulunur:

Harflerin her biri ASCII koduna dönüşüyor ve bize sayısal bir değer veriyor. Mesela "E" harfini ele alalım. "E" harfinin ASCII kodu 69'dur. Bu kodu matematiksel işleme tabii tutuyorum ve ASCII kodunu HSL renk sistemini kullandım. Çünkü HSL renk sisteminde sadece Hue (ton) ayarı yaparak farklı renkler üretebiliyorum. [HSL renk sistemi hakkında bilgi için tıklayın.](https://en.wikipedia.org/wiki/Hue)\
\
Şimdi asıl problem ASCII aralığımı 0-360 arasına dağıtmaktı. Bunun için araştırma yaptım ve lineer dönüşüm ile karşılaştım. Lineer dönüşümü kullanarak 48-90 arasındaki ASCII kodlarını 0-360 arasına dağıttım.\
Lightness (parlaklık) ve Saturation (doygunluk) değerlerini sabit tutarak, Hue (ton) değerini değiştirerek farklı renkler üretiyorum.
Hue için aşağıdaki matematik işlemini(lineer dönüşüm) kullanıyorum:
$$\mathbf{hue} = (\frac{360}{43}) \times (\text{ASCII KODU}-48)$$
```css
hsl(hue, 100%, 50%)
```
sonrasında bu kodla gelen renklerle kareleri dolduruyorum.\

Çözümlemek için ise fonksiyonun tersini aldım.

## Kullanım

1. Python ve Pillow kütüphanesi kurulduğuna emin olun.

```bash
pip install -r requirements.txt
```

2. Projeyi bilgisayarınıza indirin.

```bash
git clone https://github.com/emrekayik/EKODE.git
```

3. Terminali açın ve proje dizininize gidin.

4. Aşağıdaki komut ile çalıştırarak projeyi deneyin:

```bash
python main.py
```

5. Program başladıktan sonra "output.png" adlı bir resim dosyası oluşturulur.

## Yapılacaklar:

- [ ] Tüm ASCII karakterleri için çalışmasını sağlamak
- [ ] Nesne tabanlı yazmak
- [ ] Çıktı metnini birleştirmek

## Kaynaklarım:
- [Wikipedia Hue](https://en.wikipedia.org/wiki/Hue)
- [Colorsys](https://docs.python.org/3/library/colorsys.html)
- [Pillow Documents](https://pillow.readthedocs.io/en/stable/reference/index.html)
- [rapidtables.com rgb-to-hsl](https://www.rapidtables.com/convert/color/rgb-to-hsl.html)

## Örnek çıktı
![Çıktı](./output.png)
['E', 'M', 'R', 'E']