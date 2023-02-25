# EKODE (0.0.1)

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

## Örnek çıktı
