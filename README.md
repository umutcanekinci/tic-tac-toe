# TicTacToe

Bu projede, Python ile geliştirilmiş bir oyun bulunmaktadır. TicTacToe, sırayla boşlukları üçe üç ızgarada X veya O ile işaretleyen iki oyuncu için bir kağıt-kalem oyunudur. Bu projemde TicTacToe oyununun localde iki oyuncu ile oynanan bir dijital versiyonunu yapmak temel amacımdır.

Maalesef bu proje de yarım bıraktığım oyunlarım arasında yerini aldı. Menüsünü yaptım ancak oyunun kendisini de ileride bir gün bitiririm belki..

## Oyundan Görseller

![alt text](https://github.com/umutcanekinci/tic-tac-toe/blob/main/images/sample1.png?raw=true)
![alt text](https://github.com/umutcanekinci/tic-tac-toe/blob/main/images/sample2.png?raw=true)

## Başlangıç

### Gereksinimler

Projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız olacaktır:

- Python 3.x
- Gerekli kütüphaneler (aşağıda listelenmiştir)
    - pygame=2.5.2

### Kurulum

*Kurulum yapmadan derlenmiş edilmiş çalıştırılabilir uygulama ile devam etmek istiyorsanız kurulum aşaması atlayıp __main__.exe dosyasını çalıştırabilirsiniz.


Gerekli kütüphaneleri yüklemek için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
    ```sh
    git clone https://github.com/umutcanekinci/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. Sanal ortam oluşturun:
    ```sh
    python -m venv venv
    source venv/bin/activate # Windows kullanıyorsanız: venv\Scripts\activate
    ```

3. Gerekli paketleri yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

### Çalıştırma

Oyunu çalıştırmak için şu komutu kullanın:
```sh
python __main__.py
```

### Kullanım



#### Kontroller: 

Sıra size geldiğinde ilgili bölmeye tıklayıp X ya da O işareti ekleyin ve rakipten önce 3'lü yaparak oyunu kazanın.

### Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen şu adımları izleyin:

1. Bu depoyu fork'layın (sağ üstteki Fork butonuna tıklayın).

2. Fork'ladığınız depoyu yerel makinenize klonlayın:
```sh
git clone https://github.com/umutcanekinci/tic-tac-toe.git
cd tic-tac-toe
```

3. Yeni bir dal oluşturun (örn: feature/yenilik):
```sh
git checkout -b feature/yenilik
```

4. Değişikliklerinizi yapın ve commit edin:
```sh
git commit -am 'Yeni özellik ekledim'
```

5. Değişikliklerinizi dalınıza iterek GitHub'a gönderin:
```sh
git push origin feature/yenilik
```

6. Pull request oluşturun.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için LICENSE dosyasına bakabilirsiniz.

### İletişim

Sorularınız veya önerileriniz için umutcannekinci@gmail.com üzerinden iletişime geçebilirsiniz.
