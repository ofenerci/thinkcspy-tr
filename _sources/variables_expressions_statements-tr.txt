Değişkenler, ifadeler ve deyimler (komutlar)
============================================

.. index:: değer, veri tipleri, karakter dizisi, tamsayı, kayan nokta,
   sınıf, tür
.. index:: 
    single:: 3 tırnaklı karakter dizisi

.. _values_n_types:

Değerler ve veri tipleri
------------------------

**Değer** programın işlediği temel şeylerden ---harf ve rakam gibi--- biridir.
Şimdiye kadar gördüğümüz ``4`` ( `` 2 + 2`` işleminin sonucu) ve ``"Merhaba,
Dünya!"``.

Bu değerler  sınıf veya veri tipe denen farklı tiplere aittir: ``4`` bir tamsayıdır ve "Merhaba Dünya!"
ise bir  "karakter dizisi"dir, çünkü karekterlerden oluşan bir dizidir. Siz (
ve Python yorumlayıcısı) karakter dizilerini ayırtedebilir, çünkü tırnak
işaretleri arasında yazılmıştır.

Eğer bir değerin tipinden emin değilseniz, Python'un **type** fonksiyonu size
söyleyebilir.

   .. sourcecode:: python3

     >>> type("Merhaba, Dünya!")
     <class 'str'>
     >>> type(17)
     <class 'int'>

Süpriz olmayacak şekilde, karakter dizisi **str** sınıfına ve tamsayılar ise
**int** sınıfına aittir. Daha az açık olan ise, ondalık basamağa sahip olan
sayılar **float** sınıfına aittir, çünkü bu sayılar *kayan noktalı* (floating
point) biçiminde temsil edilmektedir. Şimdilik *sınıf* (class) ve *type* (tür) kelimelerini birbirinin yerine kullanabilirsiniz. Sınıfın ne olduğunu  daha iyi anlamak için ileriki bölümlerde geri döneceğiz.

    .. sourcecode:: python3

         >>> type(3.2)
         <class 'float'>
    
Peki ``"17"`` ve ``"3.2"`` şeklindeki ifadelerin tipleri nedir? Sayı gibi
gözükmektedirler, fakat bunlar karakter dizileri gibi tırnak işaretleri
içindedir. 

    .. sourcecode:: python3

        >>> type("17")
        <class 'str'>
        >>> type("3.2")
        <class 'str'>

Onlar karakter dizileridir!

Python'da karakter dizileri ya tek tırnak (``'``) arasına, çift tırnak
arasına (``"``) veya üçlü tırnak arasına (``'''`` veya ``"""``) alınabilir. 

    .. sourcecode:: pycon
        
        >>> type('Bu bir karakter dizisidir.')
        <class 'str'>
        >>> type("Bu da öyle.")
        <class 'str'>
        >>> type("""Bu da.""")
        <class 'str'>
        >>> type('''ve hatta bu da...''')
        <class 'str'>
 
Tek tırnaklı karakter dizileri ``"Emre'nin sakalı"`` örneğinde olduğu gibi
çift tırnak içine alınabilir. ``' Şovalyeler "hayır" diyor.'`` örneğinde
olduğu gibi çift tırnaklı karakter dizileri tek  tırnak içine alınabilir 

Üç tane tekli tırnak veya çift tırnak içine alınan karakter dizileri üçlü
tırnak olarak isimlendirilir. Bunlar tek veya çiftli tırnak içerebilir:

    .. sourcecode:: python3
        
        >>> print('''"Hayır olamaz", diye haykırdı, "Ahmet'in bisikleti kırıldı!"''')
        "Hayır olamaz", diye haykırdı, "Ahmet'in bisikleti kırıldı!"
        >>>

Üçlü tırnaklı karakter dizileri birkaç satıra yayılabilir:

    .. sourcecode:: python3
        
        >>> message = """Bu mesaj
        ... birkaç satıra
        ... yayılacak."""
        >>> print(message)
        Bu mesaj
        birkaç satıra
        yayılacak.
        >>>

Karakter dizisinin tek, çift; ya da üçlü tek veya üçlü çift tırnak işareti
arasına alınması Python'u rahatsız etmez. Python sizin komutunuzu ya da
programınızı ayrıştırdığında bütün durumları aynı olarak kabul eder ve
karakter dizisini çevreleyen tırnaklar değerin bir parçası değildir. Fakat
yorumlayacı karakter dizisini göstermek isterse, hangi tırnak işaretinin bu
amaçla kullanıldığına karar vermesi gerekir.

    .. sourcecode:: pycon

        >>> 'Bu bir karakter dizisidir.'
        'Bu bir karakter dizisidir.'
        >>> """Bu da öyle"""
        'Bu da öyle.'

Python dilinde çalışanlar genelde karakter dizilerini tekli tırnak içine
almayı seçerler. Eğer karakter diziniz daha önce tekli tırnak içine
alınmışsa, bu durumda ne olacağını düşünürsünüz?

Büyük bir tamsayı yazdığınızda, üçlü rakam grupları arasına, ``42,000``
örneğinde olduğu gibi virgül kullanmak isteyebilirsiniz. Bu Python için
geçerli bir tamsayı gösterimi değildir; fakat başka bir şey ifade eden geçerli
ifadedir:

    .. sourcecode:: python3
        
        >>> 42000
        42000
        >>> 42,000
        (42, 0)

Bu beklediğimiz birşey değil! Python bunu iki öğe içeren bir liste şeklinde
yorumlar. Bu konuya daha sonra değineceğiz. Fakat şimdilik, tamsayılarınız ne
kadar büyük olursa olsun aralarına virgül veya boşluk koymayınız. Daha önceki
bölümde söylediğimiz şeyleri yeniden gözden geçiriniz: Biçimsel diller
esnetilmeyen kurallara sahiptir; notasyonları (gösterimleri) kesindir ve küçük
bir değişiklik bile sizin amaçladığınız şeyden farklı birşey anlam ifade
edebilir. 

.. index:: değişken, atama, atama cümlesi, durum diyagramı

Değişkenler
-----------

Programlama dilinin en güçlü özelliklerinden birisi **değişkenleri**
değiştirebilme (adından anlaşılacağı gibi) yeteneğidir. Bir değişken bir
değeri tutan bir isimdir. 

**Atama cümlesi** yeni bir değişken yaratır ve değerlerini atar:

    .. sourcecode:: python3
        
        >>> mesaj = "Naber, doktor?"
        >>> n = 17
        >>> pi = 3.14159

Bu örnek üç atama gerçekleştirmektedir. Birinci atama ``"Naber, doktor?"``
karakter dizisini, ``mesaj`` isimli değişkene atar. İkincisi ise, ``17``
tamsayısını ``n``'e atar. Üçüncüsü ise ``3.14159`` kayan noktalı sayan
değerini ``pi`` değişkenine atar. 

**Atama işleci**, ``=``  eşittir işaretiyle ``==``  karıştırılmamalıdır. Atama
işleci, işlecin sol tarafındaki ismi işlecin sağ tarafındaki değere atar.
Eğer aşağıdaki ifadeyi yazdığınızda hata mesajıyla karşılaşırsınız:


    .. sourcecode:: pycon
        
        >>> 17 = n
        File "<interactive input>", line 1
        SyntaxError: can't assign to literal

    .. tip::
       Kodu okurken veya yazarken "n, 17'ye atanmıştır" veya " n, 17 değerini
       alır" şeklinde kendinize söyleyin. 

Değişkenleri kağıt üzerinde göstermenin genel bir yolu değişken isminden bir
ok çıkarıp değerini işaret etmektir. Bu çeşit gösterime **durum diyagramı**
denir, çünkü herbir değişkeninin durumunu o anda gösterir ( değişkenin ruh
halin olarak da düşünebilirsiniz.) Aşağıdaki diyagram atama komutu sonuçlarını
gösterir. 

    .. image:: illustrations/state.png
       :alt: State snapshot

Eğer yorumlayıcıdan değişkeni hesaplamasını istersek, bu değişkene o anda
bağlanmış değeri üretecektir:

    .. sourcecode:: python3
        
        >>> mesaj
        'Naber, doktor?'
        >>> n
        17
        >>> pi
        3.14159

Futbol oyunundaki skor gibi şeyleri hatırlamak için değişkenleri programın içinde kullanırız. Fakat değişkenler bir *değişkendir.* Bunun anlamı: bunlar zamanla değişirler, futbol oyunundaki skor tabelasındaki değer gibi. Bir değişkene bir değer atayabilir ve daha sonra başka değer de verebilirsiniz. (*Bu matematikten farklıdır. Matematikte, eğer `x`'e 3 değerini verirseniz, bu değer hesaplamalarınız sırasında başka bir değer dönüşmüyecektir!*)
    .. sourcecode:: python3
        
        >>> day = "Thursday"
        >>> day
        'Thursday'
        >>> day = "Friday"
        >>> day
        'Friday'
        >>> day = 21
        >>> day
        21

Dikkat ederseniz ``bugun``'ün değerini üç kere değiştirdik ve üçüncü değer
atamamızda farklı bir değer tipine ait değer verdik (ilk iki atamamız karakter
dizisi iken, son atamamız tamsayı ataması oldu.) 

Programlamanın büyük bir kısmı bilgisayarın şeyleri hatırlamasıdır. Örneğin, *
Telefonunuza gelen aramalara cevap verememe  sayısını* ele alalım. Eğer
telefonunuza yeni bir arama gelir ve siz de bu aramaya cevap veremezseniz, bu
değişken yeni bir değer alacak ve değişecektir. 

.. index:: anahtar kelimeler, altçizgi karakteri

Değişken isimleri ve anahtar kelimeler
--------------------------------------

**Değişken isimleri** istenildiği kadar uzun olabilir. Hem harf hem de rakam
içerebilir, ancak mutlaka bir harfle veya altçizgi ``_`` ile başlamaları
gerekir. Her ne kadar büyük harf kullanmak geçerli olsa da, geleneksel olarak
kullanmıyoruz. Unutulmaması gereken ``Emre`` ve ``emre`` farklı
değişkenlerdir. 

Altçizgi karakteri (``_``) bir isimde yeralabilir. Genellikle birden fazla
harf içeren ``benim_ismim`` veya ``çinde_çayın_fiyatı`` gibi kelimelerde
kullanılmaktadır. 

Bazı durumlarda altçizgi ile başlayan isimlerin özel bir anlamı vardır. Bu
yüzden Python'u yeni öğrenmeye başlayanların isimlere harf ile başlaması
güvenli bir seçenektir. 

Eğer bir değişkene geçerli olmayan bir değişken verirseniz, bir sözdizimi
hatasıyla karşılaşırsanız.

    .. sourcecode:: python3
        
        >>> 76insan = "Çok Kalabalik"
        SyntaxError: invalid syntax
        >>> more$ = 1000000
        SyntaxError: invalid syntax
        >>> class = "Bilgisayar Dersi"
        SyntaxError: invalid syntax

``76insan`` geçersizdir çünkü harft ile başlamamaktadır. ``more$`` geçersizdir
çünkü geçerli olmayan ``$`` karakteri içermektedir. Fakat ``class`` ile yanlış
olan ne?

``class`` isminin Python'un **anahtar kelimeleriden** biri olması nedeniyle bu
ismi değişken olarak kullanamıyoruz. Anahtar kelimeler genellikle dilin
sözdizim kuralını ve yapısını tanımlar ve değişken isimleri olarak
kullanılamazlar. 

Python otuza yakın anahtar kelimeye sahiptir ( Python'un sürekli gelişmesi
sonucu bazı kelimeler eklenmekte veya çıkarılmaktadır.) 

======== ======== ======== ======== ======== ========
and      as       assert   break    class    continue
def      del      elif     else     except   exec
finally  for      from     global   if       import
in       is       lambda   nonlocal not      or       
pass     raise    return   try      while    with
yield    True     False    None
======== ======== ======== ======== ======== ========

Bu listeyi erişebileceğiniz yerde tutabilirsiniz  Eğer yorumlayıcı
değişkenlerinizin birinden şikayet eder ve siz nedeninin bulamazsanız,
değişkeninizin bu listedikilerle kontrol ediniz. 

.. caution:: 
   Python'u yeni öğrenenler, "insanlara anlamlı gelen" değişkenlerin
   "bilgisayarlara da anlamlı" geleceğini sanabilirler. Örnek olarak bir
   değişkeninin ismini ``ortalama`` veya ``pi`` olarak isimlendirdiklerinde,
   bunların bir sihirbazlıkla ortalamayı hesaplıyacağını veya ``pi``'nin
   değerinin 3.14159 olabileceğini düşünebilirler. Bilgisayar kafanızda
   değişkene verdiğiniz anlamı bilmez. 

   Bazı öğretmenlerin yeni başlayanlara Python'u öğretirken  bilerek anlamlı değişken
   ismi seçmemelerinin nedeni iyi bir alışkanlık olmadığından değil, fakat
   öğrenenlerin ortalamayı hesaplaması için  mutlaka bir program yazması veya
   ``pi``'ye mutlaka bir değer aktarması gerektiğini pekiştirmeye çalışmaktır. 

.. index:: Deyim

Deyimler (Komutlar)
-------------------

Deyimler,  Python yorumlayıcısı tarafından çalıştırılabilecek bir komuttur
(yönergedir.)  Şimdiye kadar atama deyimini (``=``)  gördük.  Kısa bir süre sonra   ``while``, ``for``, ``if`` ve ``import`` deyimlerini göreceğiz ( Başka çeşitler de vardır.)  

Eğer bir deyimi komut satırına yazarsanız, python bunu yürütür. Bu deyimler
herhangi bir sonuç üretmez.

.. index:: İfadeler

İfadelerin hesaplanması
-----------------------

Bir ifade; değerlerden, değişkenlerden, işleçlerden ve fonksiyonlardan oluşan
yapıdır. Eğer bir ifadeyi komut satırına yazarsanız, yorumlayıcı bu ifadeyi
değerlendirir ve sonucu gösterir.

    .. sourcecode:: python3
        
        >>> 1 + 1
        2
        >>> len("hello")
        5

Bu örnekteki ``len`` yerleşik Python fonksiyonu olup, karakter dizisindeki
karakter sayısını döndürür. Daha önce biz ``print`` ve ``type``
fonksiyonlarını görmüştük. Bu da bizim üçüncü fonksiyonumuz. 

*Bir ifadenin değerlendirilmesi* bir değer üretir; bu nedenledir ki, ifadeler
atama deyiminin sağ tarafında gözükür. Bir değerin kendisi basit bir ifadedir.
Değişken de bir ifadedir. 

    .. sourcecode:: python3
        
        >>> 17
        17
        >>> y = 3.14
        >>> x = len("hello")
        >>> x
        5
        >>> y
        3.14

.. index:: İşleç, İşlenen, tamsayı bölme

İşleçler ve İşlenenler
----------------------

**İşleçler** toplama, çarpma ve bölme gibi hesaplamaları temsil eden özel
sembollerdir. İşleçler tarafından kullanılan değerler **işlenen** adını
almaktadır. 

Aşağıdakilerin hepsi geçerli Python ifadeleridir ( az çok ne anlama
geldiklerini çıkarabilirsiniz.):: 
    
    20+32   hour-1  hour*60+minute  minute/60   5**2    (5+9)(15-7)

``+``, ``-``, ``*`` sembolleri ve gruplama için parantez kullanımı,
matematikde ne anlam ifade ediyorsa Python'da da aynı anlamı ifade etmektedir.
Yıldız işaret ``*`` çarpmanın ve ``**`` üs almanın sembölleridir. 

    .. sourcecode:: python3
        
        >>> 2 ** 3
        8
        >>> 3 ** 2
        9
 
Bir işlenenin yerinde bir değişkenin ismi yer aldığında, işlem yapılmadan önce
bu değişken değeriyle değiştirilir. 

Toplama, çıkarma, çarpma ve üs alma işlemleri neyi bekliyorsanız onu yapan
işlemledir. 

Örnek: 645 dakikayı saate çevirelim:

    .. sourcecode:: python3
        
        >>> dakika = 645
        >>> saat = dakika / 60
        >>> saat
        10.75

Python 3'de bölme işlemcisi ``\`` her zaman kayan noktalı sonuç verir. Biz bu
değerin içinde kaç tane saat ve kaç dakika kaldığını bilmek istemiş oluruz. ( yani
sayının ondalık kısmını kesip atmaz. Python 2'de ise yalnızca tamsayı değeri
verir; eğer yukarıdaki ifadeyi Python 2'de hesaplasaydınız 10 değerini
bulacaktınız.) Python iki türlü bölme işlemcisini hizmetimize sunar.
Bunlardan birincisi yukarıdaki ``\`` *bölme işlemcisi*, diğeri de *tamsayı bölme
işlemcisi* olan ``//`` semboldür. Bunun sonucu her zaman tamsayıdır. Sanki
ondalık kısmı atıp, ondalık kısmın sol tarafındaki tamsayı değerini veriyormuş
gibi. Örnek olarak `6//4`'ün sonucu `1`\ dir, fakat `-6//4` sonucu sizi
şaşırtabilir!

    .. sourcecode:: python3
        
        >>> 7 / 4
        1.75
        >>> 7 // 4
        1
        >>> minutes = 645
        >>> hours = minutes // 60
        >>> hours
        10
 
Hangi bölme işlemcisini seçeceğinize dikkat ediniz. Eğer bölme işlemi
sonucunda ondalık sayıya da ihtiyacınız varsa (kayan noktalı sayı), bu bölme
işlemini doğru şekilde yapan `/` *bölme işlemcisini* kullanın. 

.. index:: tür değiştirici fonksiyon, int, float, str, kesme

Tür dönüştürme fonksiyonları
----------------------------

Bu kısımda daha başka üç Python fonksiyonuna göz atacağız. Bunlar: ``int``,
``float`` ve ``str`` fonksiyonlarıdır ve bu fonksiyonlar aldıkları
değişkenleri sırasıyla ``int``, ``float`` ve ``str`` türlerine dönüştürürler.
Bu fonksiyonlara **tür dönüştürücü** fonksiyonlar diyeceğiz. 

``int`` fonksiyonu kayan noktalı sayı veya karakter dizisi alır ve bunları
tamsayıya çevirir. Kayan noktalı sayılar için, ondalıklı kısım atılır. Biz bu
işlemi sayı doğrusunda *sıfıra doğru kesme* olarak isimlendireceğiz. Bunları
örnek üzerinde görelim:

    .. sourcecode:: python3
        
        >>> int(3.14)
        3
        >>> int(3.9999)             # Bu en yakın tamsayıya yuvarlamaz 
        3
        >>> int(3.0)
        3
        >>> int(-3.999)             # Dikkat ediniz ki sonuç sıfıra yakındır. 
        -3
        >>> int(minutes / 60)
        10
        >>> int("2345")             # Karakter dizisini ayrıştırarak tamsayıya
        çevirir.
        2345
        >>> int(17)                 # fonksiyon değişkeni tamsayı olsa da
        çalışır.
        17
        >>> int("23 bottles") 

Son komut bir sayı gibi gözükmüyor --- Ne gibi sonuç beklersiniz?
        
    .. sourcecode:: python3
    
        Traceback (most recent call last):
        File "<interactive input>", line 1, in <module>
        ValueError: invalid literal for int() with base 10: '23 bottles'

``float`` tür dönüştürücüsü tamsayıyı, kayan sayıyı veya sözdizimsel olarak
kurala uygun karakter dizisini kayan sayıya çevirir. 

    .. sourcecode:: python3
        
        >>> float(17)
        17.0
        >>> float("123.45")
        123.45

``str`` tür dönüştürücüsü ise aldığı değişkeni karakter dizisine çevirir:

    .. sourcecode:: python3  
    
        >>> str(17)
        '17'
        >>> str(123.45)
        '123.45'

.. index:: İşleçlerin sırası, öncelik kuralı

İşleçlerin sırası
-----------------

Bir ifadede birden fazla işleç varsa, bu işleçlerin hasaplama sırası  **öncelik kuralına** göre belirlenir. Matematikte işlemcilerin uyduğu öncelik sırasının aynısını Python'da kullanır. PÜÇBTÇ kısaltması bu kuralları hatırlamak için kullanabilecek bir kısaltmadır:

#. **P**\ arantezler en yüksek önceliğe sahiptir ve ifadenin hangi sırada
   değerlendirilmesine yönelik ayarlamaları yapmanızı sağlar. Parantez
   içindeki ifadeler daha önce değerlendirildiği için, ``2 * (3-1)``'in sonucu
   4, ``(1+1)**(5-2)``'in sonucu ise 8'dir. İfadeleri daha kolay okumak için
   parantezleri kullanabilirsiniz. ``(minute * 100) /60`` ifadesi daha kolay
   okunduğu gibi, sonucu da değiştirmemiş olursunuz. 

#. **Ü**\ s alma daha az önceliğe sahiptir, ``2**1+1`` ifadesinin cevabı
   3'tür 4 değil ve ``3*1**3`` cevabı da 3'tür 27 değil.

#. **Ç**\ arpma ve **B**\ ölme işleçleri aynı önceliğe sahiptir; **T**\ oplama
   ve **Ç**\ ıkarmadan (bunlar da aynı önceliğe sahiptir) daha yüksek
   önceliklidir. ``2*3-1`` ifadesi 4 yerine 5 ve ``5-2*2`` ifadesi 6 değil
   1'dir. 

#. Aynı önceliğe sahip olan işleçlerin değerlendirilmesinde soldan sağa kuralı
   izlenir. Buna cebir derslerinde sol ilişkili bağlantı denir. ``6-3+2``
   ifadesinde, çıkarma işlemi ilk yapılır ve 3 bulunur. Daha sonra 2'yi
   ekleyerek 5'i buluruz. Eğer işlemler sağdan sola doğru hesaplansaydı sonuç
   ``6-(3+2)`` olurdu, bu da 1'e eşittir (Yukarıdaki kısaltma sizi
   yanıltmasın. Bu kısaltma sanki çarpmanın, bölmeden daha öncekli olduğu; ya
   da toplamanın, çıkarmadan daha öncelikli olduğuna sizi yanıltabilir. Aynı
   önceliğe sahip işleçler arasında soldan sağa kuralı izlenir.)

   - Tarihsel garip olay yüzünden, üs alma işleci ``**`` soldan sağa kuralına
     uymaz. Üs işleçlerinin yer aldığı bir ifadede, üslerin işlem sırasını
     belirlemek için parentezlerin kullanımı karışıklığı ortadan kaldırır:

       .. sourcecode:: python3
        
          >>> 2 ** 3 ** 2     # En sağdaki ** işleç önceliğe sahiptir. 
          512
          >>> (2 ** 3) ** 2   # Parentezleri kullanarak istediğiniz sırada
          işlemleri yapabilirsiniz.
          64

Yukarıdaki işlemler gibi kısa ifadeleri keşfetmek ve deney yapmak için Python
emir istemcisi çok faydalıdır.

.. index:: karakter dizisi işlemleri, birleştirme

Karakter dizisi üzerindeki işlemler
-----------------------------------

Genel olarak, karakter dizileri üzerinde matematiksel işlemler
uygulayamazsınız; karakter dizileri sayı gibi gözükse bile! Aşağıdaki ifadeler
geçersizdir ( mesaj'ın karakter dizisine ait bir tür olduğunu varsayalım.) 

    .. sourcecode:: python3
        
        >>> mesaj - 1        # Hata 
        >>> "Merhaba" / 123  # Hata
        >>> mesaj * "Hello"  # Hata
        >>> "15" + 2         # Hata

Ancak ``+`` işleci karakter dizileriyle çalışmaktadır. Fakat karakter dizileri
için ``+``'nın anlamı toplamayı değil, **birleştirmeyi** ifade etmektedir.
Bunun anlamı iki karakter dizisini uç uca bağlamaktır. Örneğin:

    .. sourcecode:: python3
        :linenos:
        
        meyve = "muz"
        iyi_pişirilmis = " fındık ekmeği"
        print(meyve + iyi_pisirilmis)

Programın çıktısı ``muz  fındık ekmeği`` olacaktır. Fındıktan önceki boşluk
karakter dizisinin bir parçasıdır ve birleştirilmiş karakter dizileri arasında
boşluk yaratmak için gereklidir.

``*`` işleci de karakter dizileri üzerinde çalışır. Tekrarlama işlemini
gerçekleştirir. Örneğin, ``Neşe*3``'ün değeri ``NeşeNeşeNeşe`` sonucunu
verecektir. İşlenenlerden biri karakter dizisi, diğeri de tamsayı olmalıdır.

Diğer bir taraftan, ``+`` ve ``*`` işleçlerinin yukarıdaki yorumu, toplama ve
çarpma işleçlerinin amacı düşünüldüğünde bir anlam ifade etmektedir.
``4*3``'ün ``4+4+4``'e eşit olması gibi, ``Neşe*3`` ifadesinin
``Neşe+Neşe+Neşe``' ifadesiyle aynı olmasını bekleriz. Ancak, karakter
dizileri birleştirme ve tekrarlama ile tamsayılar arasındaki toplama ve çarpma
arasında önemli bir fark vardır. Toplama ve çarpma işleminin sahip olduğu
ancak karakter dizisi birleştirme ve tekrarlama işleminin sahip olmadığı bir
özellik düşünebiliyor musunuz?

.. index:: girdi, girdi penceresi

Girdi
-----

Klavyeden girdi alabilmek için Python içerisinde tanımlı iki fonksiyon vardır: 

    .. sourcecode:: python3
        :linenos:
        
        n = input(" Lütfen isminizi giriniz: ")

Eğer bu betiği PyScripter içinde çalıştırırsanız, aşağıdaki bir küçük pencere
açılacak ve sizden girdiyi bekleyecektir:

    .. image:: illustrations/enter_name_dialog.png
       :alt: input dialog

Program kullanıcısı bir isim girip, `OK` tuşuna bastığında, girilen metin
``input`` fonksiyonu tarafından döndürülür ve ``n`` değişkenine atanır. 

Eğer kullanıcıya yaşını sorsaydınız ve kullanıcıda 17 cevabını girseydi, siz
sonuçta ``"17"`` olan karakter dizisini alacaktınız. Bir programcı olarak
sizin işiniz, daha önce gördüğümüz ``int`` veya ``float`` tür çevirici
fonksıyonlarını kullanarak bu karakter dizisini tamsayı veya kayan sayı türüne
çevirmektir. 

.. index:: fonksiyonların kompozisyonu, fonksiyon kompozisyon

Kompozisyon
-----------

Şimdiye kadar bir programın öğelerini --- değişkenler, ifadeler ve deyimler
--- ayrı ayrı inceledik, bunları nasıl birleştireceğimizden bahsetmedik.

Programlama dillerinin en kullanışlı özelliklerinden biri, küçük yapısal
blokları birleştirilebilmesine ve  bu parçaları **kompozisyon**\ lamasına (birleştirebilme)  izin vermesidir. 

Örneğin, kullanıcıdan nasıl girdi alacağımızı; karakter dizisini
nasıl kayan noktalı sayıya çevireceğimizi; nasıl karmaşık bir ifade
yazacağımızı; ve değişkenleri nasıl ekrana yazdıracağımız biliyoruz. Bütün bu
işlemleri 4 adımlık bir programın içine koyalım. Programımız, kullanıcıya
çemberin yarıçapını kullanıcıya sorsun ve dairenin alanını   hesaplasın. 

.. math:: 
    \text{Alan} = \pi r^2

Öncelikle, bu dört adımı teker teker yapacağız:

    .. sourcecode:: python3
        :linenos:
       
        cevap = input("Dairenin yarıçapı nedir? ")
        r = float(cevap)
        alan = 3.14159 * r**2
        print("Dairenin alanı =", alan)

Yukarıdaki kodun ilk iki satırını tek bir satıra  ve son iki satırı
da tek bir satıra birleştirelim. 
    
    .. sourcecode:: python3
       :linenos:
       
       r = float( input("Dairenin yarıçapı nedir? ") )
       print("Dairenin alanı =  ", 3.14159 * r**2)

Eğer biraz el çabukluğu yapmak isterseniz, yukarıdaki bütün ifadeleri bir
ifade içinde yazabilirsiniz.

    .. sourcecode:: python3
       :linenos:
       
       print("Dairenin alanı =  ", 3.14159*float(input("Dairenin yarıçapı nedir?"))**2)

İnsanlar böyle tümleşik kodu anlıyamıyabilir, ancak birçok program satırını
nasıl tek bir satıra indirebileceğimizi gösterir. 

Bir program kodunu veya parçasını daha küçük parçalara ayırıp ayırmamada şüphe
içinde iseniz, bunu insanların anlayabileceği kadar basit hale getirmeye
çalışın. Benim tercihim dört ayrı adımda yazdığımız ilk durum olacaktır.

.. index:: 
    single:: modüler işlemcisi
    singlie:: işlemci; modüler

Modüler işlemcisi
-----------------

**Modüler işlemci** tamsayılar veya tamsayılar ifadeleri üzerinde çalışır. İlk
sayının ikinci sayıya bölünmesiyle kalanı verir. Python'da, modüler işlemcisi
yüzdelik işareti ``%`` ile gösterilir. Sözdizimi diğer işlemciler gibidir.
Çarpma işlemcisi ile aynı önceliğe sahiptir.


    .. sourcecode:: python3
        
        >>> q = 7 // 3     # Bu bir tamsayı bölme işlemcisidir.
        >>> print(q)
        2
        >>> r  = 7 % 3
        >>> print(r)
        1

Böylece 7'nin 3'e bölümündenden, bölümün 2 ve kalanın da 1 olduğu görülür. 

Modüler işlemcisi görüldüğünden çok daha faydalılır. Örneğin, bir sayının
diğer bir sayıya bölünebilir olup olmadığını kontrol edebilirsiniz. Eğer
``x%y``'nin cevabı sıfır ise, ``x``, ``y`` tarafından bölünebilir. 

Aynı zamanda, bir sayının en sağındaki rakam veya rakamları elde etmek içinde
kullanabilirsiniz. Örneğin, ``x % 10`` ifadesi ``x``'in en sağındaki rakamı
(10'luk tabanda) elde ederiz. Benzer olarak, ``x%100`` ifadesi son iki rakamı
verir. 

Ayrıca çevirme işlemleri yapmada da oldukça faydalıdır. Örneğin saniyenin; saate,
dakikaya ve saniye çevrilmesi işlemi gibi. Kullanıcıdan, saniye olarak değer
girmesini isteyen bir program yazalım. Biz bu saniyeyi, saat, dakika ve kalan
saniyeye çevireceğiz.

    .. sourcecode:: python3
        :linenos:

        toplam_san = int(input("Kaç saniye?"))
        saat = toplam_san // 3600      
        hala_kalan_san = toplam_san % 3600
        dakika =  hala_kalan_san // 60 
        son_kalan_san = hala_kalan_san  % 60
        
        print("Saat=", saat, "  dakika=", dakika,  
                                 "saniye=",hala_kalan_san)

Sözlük
------

.. glossary::  
    
    atama komutu
        Bir değeri,  bir isme (değişkene) atayan komuttur. ``=`` atama komutunun
        solunda isim vardır. Atama komutunun sağında ise, Python tarafından
        değerlendirilip, isme atanacak bir ifade vardır. Atama işlecinin  
        sağ ve sol tarafları arasındaki fark 
        programcılar için kafa karıştırıcı olabilir. Aşağıdaki örnekte:


            .. sourcecode:: python3
        
                 n = n + 1

        ``=``'nın her iki tarafındaki ``n`` değişkeni farklı görevler
        üstlenir. Sağ tarafta bir değerdir  ve Python yorumlayıcısı tarafından
        sol taraftaki isme atanmadan önce değerlendirilecek ifadenin kısmını
        oluşturur.

    atama işleci
        ``=`` Python'un atama işlecidir. Bunu matemikte kullanılan ve
        değerleri birbirleriyle karşılaştıran *eşittir* işleci ile
        karşılaştırın. 

    kompozisyon
        Basit ifadeleri ve komutları, karmaşık hesaplamaları temsil etmek için
        bir araya getirip birleşik ifadeler ve komutlar oluşturma özelliğidir.

    birleştirme
        İki dizi katarının uç uca eklemedir.

    veri tipi
        Değerler kümesidir. Bir değerin tipi, bir ifade içinde nasıl
        kullanılabileceğini belirler. Şu ana kadar tamsayılar ( ``int``), kayan
        noktalı sayılar (``float``) ve dizi katarları (``str``) tiplerini
        gördük.

    hasaplama
        Bir ifadeyi basitleştirmek ve tek bir değer üretmek için sırasıyla
        işlemleri gerçekleştirmektir. 

    ifade
        Tek bir sonuç değerini temsil eden değişken, işleç ve değerlerin bir
        birleşimidir. 

    float (kayan noktalı sayı)
        Kayan noktalı sayıları saklayan Python veri tipleridir. Kayan noktalı
        sayılar bilgisayarda iki parça olarak saklanır: bir *taban* ve *üst*.
        Bunlar normal şekilde görüntülendiğinde, ondalık sayılar gibi gözükürler.
        Float sayılar kullandığınızda yuvarlama hatalarına dikkat etmeniz
        gerekirmektedir ve yaklaşık değer barındırırlar.

    tamsayı bölme işleci
        ``//`` işleci  bir sayıyı diğer bir sayıya böler ve sonucu tamsayı
        olarak verir. Eğer bölme işleminin sonucu tamsayı değilse, bu sonuçtan
        küçük en yakın tamsayıyı sonuç olarak atar. 

    int (tam sayı)
        Pozitif veya negatif tamsayıyı ifade eden Python veri tipi.

    anahtar kelime
        Derleyici tarafından programı ayrıştırmak için kullanılan Python'a
        özgü kelimeler. Örneğin ``if``, ``def`` ve ``while`` kelimelerin
        değişken olarak kullanamazsınız. 

    mödüler işleci
        Yüzdelik (``%``) işareti ile ifade edilen ve iki sayının birbirine
        bölümünde kalanı veren işleç.

    işlenen
        İşleç'in üzerine etkidiği değerlerden biri. 

    öncelik sarısı
        Birden fazla işleç ve işlenin bulunduğu bir ifadede hesaplama sırasını
        belirten kurallar kümesi.

    durum diyagramı 
        programın bir anındaki eğişkenlerin ve referans ettikleri değerlerin
        grafiksel gösterimidir.

    komut (deyim) 
        Python yorumlayıcı tarafından yürütülebilecek yönergedir. Şimdiye kadar
        atama komutunu gördük, fakat yakında ``import`` ve ``for`` komutlarını
        göreceğiz. 

    str (Karakter dizisi)
        Karakter dizisini (string) tutan Python veri tipidir. 

    değer
        Bir değişkende veya hesaplanan bir ifadede sakla bir sayı veya karakter dizisi ( veya daha sonra isimlendirilecek başka şeyler) 

    değişken
        Bir değeri temsil eden isimdir.

    değişken ismi
        Bir değişkene verilen isimdir. Pyton'daki değişken isimleri bir harf (a..z, A...Z ve _) veya bir rakam (0..9) ile başlayabilir. Tercih edilen programlama pratiğinde, değişken ismi öyle seçilmeli ki; kullanım amaçları açık olsun, program içinde kendi kendini belgelendirsin.

Alıştırmalar
------------

#. " Hep iş ve hiç oyun oynamamak kişiyi sıkıcı yapar." cümlesindeki her bir
   kelimeyi farklı bir değişkende saklayın; sonra ``print`` deyimi yardımıyla
   bu cümleyi tek bir satırda yazdırın. 

#. ``6 * 1 - 2`` ifadesine parentez ekleyerek, değerini 4'ten -6'ya
   değiştirin.

#. Daha önce üzerinde çalıştığınız bir programa yorum ekleyerek tekrar
   çalıştırın ve sonucu gözlemleyin. 

#. Python yorumcusunu başlatın ve ``ahmet + 4`` ifadesini girin. Bu size bir
   hata verecektir:

       .. sourcecode:: python3
        
            NameError: name 'ahmet' is not defined

    ``ahmet`` ismine bir değer atayın, böylece ``ahmet+4`` 10 değerini
    üretebilsin.

#. Bileşik faiz hesabı yapılırken kullanılan denklem 

        .. math::
            
            A = P\big(1+r/n\big)^{nt} \\
        
        - P = ilk yatırım
        - r = yıllık cari (nominal)  faiz oranı ( ondalıklı girilecek. Örnek: yıllık  %10 faiz getiriyorsa, 0.1
          girilir.) 
          olarak giriniz.) 
        - n = faizin yılda kaç kere ana paraya eklendiği (Örnek: eğer banka
          size 3 aylık faiz miktarını veriyorsa, bu değer 4 olacak. ) 
        - t = yıl miktarı

   ile verilir. 

   10000 TL'lik ana parayı `P` değişkenine; 12 değerini `n` değişkenine; %8 faiz oranını
   `r` değişkenine atayınız. Kullanıcıdan yatırımın kaç
   sene bankada tutulacağını komut satırından soranve bunu `t`'ye atayan
   Python programı yazın. `t` yıl sonra bankadaki birikiminizi hesaplayın.

#. Aşağıdaki sayısal ifadeleri kafanızdan hesaplayınız ve sonra Python
   yorumlayıcısı kullanarak sonuçlarınızı karşılaştırınız:


    #. ``>>> 5 % 2``
    #. ``>>> 9 % 5``
    #. ``>>> 15 % 12``
    #. ``>>> 12 % 15``
    #. ``>>> 6 % 6``
    #. ``>>> 0 % 7``
    #. ``>>> 7 % 0``

    Son örnek doğru çıktı mı? Niçin? Eğer son örnek hariç diğer butün örnekleri
    doğru tahmın etmişseniz, şimdi ilerliyebilirsiniz. Eğer doğru tahmin edememiş
    iseniz, kendi kendinize yeni örnekler üretin. Kendinizi rahat hisseden
    kadar Mödüler işlemcisi üzerine çalışıp, nasıl çalıştığını anlayın.

#. Saate bakıyorsunuz ve öğleden sonra 2 olduğunu görüyorsunuz. Alarımınızı 51
   saat sonrasına kuruyorsunuz. Hangi saatte alarımınız çalışır? (İpucu:
   Parmaklarınızla sayma yapabilirsiniz, fakat bu bizim amacımız değil. Eğer
   hala parmaklarınızla hesap yapmaya yöneliyorsunuz, 51'i 5100'e çevirin.)

#. Yukarıdaki programı çözecek genel bir Python programı yazın. Kullanıcıya
   saat cinsinden şimdiki zamanı  ve kaç saat beklenmesini soran bir program
   yazınız. Programınız, alarm çaldığında saatin kaç olduğunu gösteren bir
   çıkış vermelidir. 
   
   
    
        
        
 
   




