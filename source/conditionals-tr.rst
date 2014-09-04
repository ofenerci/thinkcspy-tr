..  Copyright (C)  Peter Wentworth, Jeffrey Elkner, Allen B. Downey and Chris Meyers.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with Invariant Sections being Foreword, Preface, and Contributor List, no
    Front-Cover Texts, and no Back-Cover Texts.  A copy of the license is
    included in the section entitled "GNU Free Documentation License".

|    

Koşul İfadeleri
===============

Koşul ifadelerinin kullanımı programları ilginç hale getirir. Programın
davranışını, bu sınamaların sonucuna göre değiştirebiliriz. Bu bölümün konusu
işte budur. 

.. index::
    single:: Boolean değer
    single:: değer; Boolean
    single:: Boolean ifadeler
    single:: ifade; Boolean
    single:: mantıksal işleçler
    single:: işleçler; mantıksal
    single:: işleçler; karşılaştırma
    single:: karşılaştırma işleci

Boolean değerler ve ifadeleri
-----------------------------

*Boolean*, doğru ya da yanlış değere sahiptir. Bu isim Boolean Cebrini yaratan
İngiliz matematikçi George Boole'dan dolayı verilmiştir. Bu cebir, bu değerleri
birleştirme ve bu değerler üzerinden mantık yürütmek için bazı kurallarla
ilgilidir. 

Python'da iki tür Boolean değer vardır: ``True (Doğru)`` ve ``False (Yalnış)``.
Python açısından bu değerler herzaman büyük harfl ile başlar. Python'un bu veri
tipine **bool** adı verilir. 

    .. sourcecode:: python3
      
        >>> type(True)
        <class 'bool'> 
        >>> type(true)
        Traceback (most recent call last):
          File "<interactive input>", line 1, in <module>
        NameError: name 'true' is not defined

**Boolean ifadesi**, sonuç olarak Boolean ifadesi üreten bir ifadedir. Örneğin,
``==`` işleci iki değeri karşılaştırıp, bir Boolean değer üretir:

    .. sourcecode:: python3 
        
        >>> 5 == (3 + 2)   # 3 + 2'nin değeri 5'e mi eşit?
        True
        >>> 5 == 6
        False
        >>> j = "hel"
        >>> j + "lo" == "hello"
        True

İlk cümlede, iki işlenenin eşittir, bu yüzden deyim ``True`` sonucunu üretir;
ikinci cümlede ise 5 ile 6 birbirine eşit değildir ve ``Falsa`` sonucu üretir. 

``==`` işleci, ``Boolean`` değer üreten  altı tane genel karşılaştırma işleçlerinden bir tanesidir. Diğerleri şunlardır:


    .. sourcecode:: python3
        
        x == y               # Eğer x, y'ye eşit ise True değeri üretir.
        x != y               # x, y'ye eşit değil ise True değeri üretir.
        x > y                # x, y'den büyük ise True değeri üretir.
        x < y                # x, y'den küçük iseTrue değeri üretir.
        x >= y               # x, y'den büyük veya eşit ise True değeri üretir.
        x <= y               # x, y'den küçük veya eşit ise True değeri üretir.

Her ne kadar bu işlemler size tanıdık gelse bile, Python tarafından kullanılan
simgeler, matematik simgelerinden farklıdır. Sıklıkla yapılan yapılan hata,
"çift eşit" (``==``) yerine, "tek eşit" (``=``) simgesi kullanmaktır. Ayrıca,
``=<`` ve ``=>`` simgeleri tanımlı değildir.

Daha önce gördüğümüz türler gibi, Boolean değerleri değişkenlere atanabilir,
ekrana basılabilir, vb. 

    .. sourcecode:: python3
     
        >>> yas = 20
        >>>  ehliyet_alabilir_miyim = yas >= 18
        >>> print(ehliyet_alabilir_miyim)
        True
        >>> type(ehliyet_alabilir_miyim) 
        <class 'bool'> 

.. index:: 
    single: mantıksal işleçler
    single: işleçler; mantıksal

Mantıksal işleçler
------------------

Üç adet **mantıksal işleç** vardır: ``and`` (ve), ``or`` (veya) ve ``not``
(değil). Bu basit Boolean deyimlerini kullanarak, daha karmaşık ``Boolean``
ifadeleri üretebiliriz. Bu işleçlerin anlamları, parantez içinde yazılmış olan
Türkçe anlamlarıyla benzerdir. Örneğin, ``x > 0 ve x < 10`` ifadesi, eğer " ``x``
ifadesi 0'dan büyük *ve* aynı zamanda ``x`` 10'dan küçük olduğunda" doğrudur.

``n % 2 == 0 or n%3 == 0`` ifadesi iki koşuldan biri doğru olduğunda (veya'dan dolayı) doğrudur. Bunun anlamı ``n`` 2 ile bölünebilir *veya* 3 ile bölünebildiğinde doğrudur ( ``n`` hem iki hem de üç ile bölübelirse ``Boolean`` değerinin ne olacağını düşününüz? Bu ifade ``True`` veya ``Yalnış`` bir değer mi üretecek? Bunu Python yorumcusunda çalıştırın.) 

Son olarak, ``not`` işleçi bir Boolean değerinin zıttını (negatifi) üretmede
kullanılır. Böylece ``not ( x > y)``'nin değeri,  ``True`` eğer ``(x > y)``
değeri ``False`` olduğunda doğru olacaktır. Başka bir söyleyişle,  u ifade ``x``, ``y``'ye eşit veya küçük olduğunda doğru olacaktır.

``or`` işlecinin solundaki ifadesi ilk olarak hesaplanacaktır: Eğer sonuç
``True`` ise, Pyton sağ taraftaki ifadeleri hesaplamaz (hesaplamısına gerek
yoktur.) Buna *short-circuit evaluation* (kısa devre hasaplaması) denir. Benzer
olarak, ``and`` işleci için, eğer ifadenin solundaki değer ``False`` sonucu
veriyorsa Python sol taraftaki değeri hesaplamaz. 

Böylece gereksiz hesaplamalar dikkate alınmaz. 

Doğruluk Tabloları
------------------

Doğrululuk tabloları, bütün muhtemel giriş değerleri üzerine mantıksal işleçleri
uyguyarak çıktıları listelememize imkan verir. ``and`` ve ``or`` işleçleri
yalnızca iki işlenen üzerine etkilediğinden, ``and`` işlecinin sonucunu veren
dört tane satır vardır. 


  ======= =======  ========
  a       b        a and b
  ======= =======  ========
  False   False    False
  False   True     False
  True    False    False
  True    True     True
  ======= =======  ========

Herbir Doğruluk tablosunda, bazen T'yi ``True`` ve F'i ``False`` kısaltmaları
olarak kullanırız. ``or`` için doğruluk tablosu ise:


  ===  ===  =======
  a    b    a or b
  ===  ===  =======
  F    F    F
  F    T    T
  T    F    T
  T    T    T
  ===  ===  =======

Üçüncü mantıksal işlemcisi ise ``not`` işlemcisidir. Bu yalnızca tek işlenen
değeri alır. Bu yüzden doğruluk tablosu yalnızca iki satıra sahiptir. 


  ===  ======
  a    not a
  ===  ======
  F    T
  T    F
  ===  ======


  ===  ======
  a    not a
  ===  ======
  F    T
  T    F
  ===  ======

Boolean İfadelerinin basitleştirilmesi
--------------------------------------

İfadeleri basitleştirme ve yeniden düzenlemek için bir takım kurallara *cebir*
denir. Örneğin, okulda gördüğümüz cebir kuralları ile tanışığız. Örneğin:


    .. sourcecode:: python3
    
        n * 0 == 0

Burda ise farklı bir cebir, *Boolean* cebri, göreceğiz. Bu cebir, Boolean
değerleri ile çalışmamız için kuralları  belirler.

İlk olarak, ``and`` işlemcisi:

      .. sourcecode:: pycon
    
        x and False == False
        False and x == False
        y and x == x and y
        x and True == x
        True and x == x
        x and x == x

``or`` işlemcisine karşılık gelen kurallar ise:

      .. sourcecode:: pycon
    
        x or False == x
        False or x == x
        y or x == x or y
        x or True == True
        True or x == True
        x or x == x    

İki ``not`` işlemcisi birbirinin etkisin yok eder. 

      .. sourcecode:: pycon
    
        not (not x) == x

.. index:: koşullu dallanma, koşullu yürütme, if, elif, else, if deyimi,
   birleşik deyim, deyimler bloğu, blok, gövde, pass deyimi

.. index::
    single: deyim; if
    single: birleşik deyim; başlık
    single: birleşik deyim; gövde
    single: birleşik deyim
    single: deyim; pass

Koşullu yürütme
---------------

Yararlı programlar yazabilmek için, neredeyse her zaman koşulları sınamamız ve
programın davranışlarını bu sınamaların sonucuna göre değiştirebilmemiz gerekir.
**Koşul deyimleri** bize bu yeteneği kazandırır. En basit örneği **if**
deyimidir.


    .. sourcecode:: python3
        :linenos:
        
        if x % 2 == 0:
            print(x, " çift sayıdır.")
            print("2'nin asal sayı olan yalnız çift sayı olduğunu biliyor
            musunuz?")
        else:
            print(x, "tek sayıdır.") 
            print(" İki tek sayının çarpımının her zaman tek sayı sonucu
            verdiğini biliyor muydunuz?")

``if`` deyiminden sonra yazılmış olan Boolean deyimine **koşul** adı verilir.
Eğer bu koşul doğru ise, bu deyimin altındaki  girintilenmiş bütün deyimler
çalıştırılır. Eğer değilse, ``else`` deyiminin altındaki girintilenmiş deyimler
çalışır. 


.. admonition::  if deyiminin else cümlesiyle akış diyagramı

   .. image:: illustrations/flowchart_if_else.png  

if cümlesinin sözdizimi şu şekildedir:


    .. sourcecode:: python3
        :linenos:
        
        if BOOLEAN İFADESİ:
            DEYİMLER         # Eğer koşul doğru ise hesaplanır 
        else:
            DEYİMLER        # Eğer koşul yalnış ise hesaplanır

Bir önceki bölümde gördüğümüz fonksiyon tanımlaması ve diğer bileşik deyimler
gibi, ``if`` deyimi bir başlık ve bir gövdeden oluşur. Başlık ``if`` anahtar
kelimesi ile başlar ve bir boolean deyimiyle devam eder. Sonu yine iki nokta
üstüste (:) ile belirlenmiştir. 

Takip eden girintili deyimlere **blok** adı verilir. İlk girintisiz deyim bloğun
sonunu belirler. 

Eğer Boolean ifadesi ``True`` ise ilk bloktaki  deyimlerin her biri sırasıyla
yürütülür. Eğer Boolean ifadesi ``False`` ise ilk blok atlanır ve ``else``
cümlesi altındaki girintili bütün deyimler çalıştırılır.

``if`` deyiminin altında oluşan iki cümlenin altındaki deyim sayısında bir
sınırlama yoktur. Fakat Her bir bir blokta en az bir deyim olması gereklidir.
Bazen boş ``if`` cümlesi yazmak (mesela daha sonra yazmak üzere alanı ayırmak
için) gerekebilir. Bu durumda ``pass`` deyimini, ki bu cümle hiç bir şey yapmaz,
kullanabilirsiniz. 

    .. sourcecode:: python3
        :linenos:
        
        if True:          # Bu her zaman doğrudur. Her zaman işletilir.
            pass          # Fakat hiçbir şey yapmaz. 
        else:
            pass          

.. index:: alternatif yürütme, dallanma, kodu fonksiyon içine yerleştirme

``else`` cümleciğini ihmal etme
-------------------------------


.. admonition::  Flowchart of an if statement with no else clause

   .. image:: illustrations/flowchart_if_only.png

``if`` deyiminin başka bir türü ``else`` cümleceğini ihmal etmektir. Bu durumda,
koşul durumu ``True`` ise, ``if`` deyiminin altındaki deyimler yürütülür; aksi
takdirde, ``if`` bloğunun altındaki girintili deyimler çalıştırılmadan diğer
deyimlerden yürümeye devam eder.

    .. sourcecode:: python3
        :linenos:

        if x < 0:
            print("negati sayı  ",  x, " geçerli değildir.")
            x = 42
            print("Bunun yerine 42 sayısını kullanmayı tercih ettim. ")
            
        print("Karekök x = " , math.sqrt(x))

Bu durumda, eğer program başında verilen ``x``'in değeri pozitif bir sayı ise,
if deyiminin altındaki girintili deyimler çalıştırılmadan atlanacak ve sonraki
girintili olmayan ``print`` deyimi çalıştırılacaktır. Dikkat ediniz ki ``if``
deyiminden sonra hemen ``print`` deyiminin çalıştırılması kendinden önce gelen
deyimler arasında boşluk bırakılmasından değil, kendisinden önce gelen
deyimlerin girintili olmasından dolayıdır. Bir önemli nokta da,  ``math.sqrt(x)`` fonksiyonunu çağrabilmek  için ``import math`` deyimini betik kodumuzun ilk satırlarına koymaktır. 

.. admonition:: Python Terminolojisi 
    
    Python belgelerinde bazen *block (blok)* terimi yerine **suite (takım)**
    terimi kullanılır. Her ikisi de aynı anlama gelir. Fakat biz diğer
    programlama dillerinde sık kullanılan *blok* terimini kullanacağız.

    Dikkat ediniz ki, ``else`` bir deyim değildir. ``if`` deyimi *iki cümleye*
    sahiptir. Bunlardan biri seçmeli ``else`` cümlesidir. 

.. index:: 
    single: zincirleme koşul ifadeleri
    single: koşullu; zincirleme

Zincirleme koşul ifadeler
-------------------------

Bazen ikiden fazla olasılık vardır ve iki dallanmadan fazlasına gereksinim
duyarız. Bunun gibi bir hesaplamayı ifade etmek için **zincirleme koşul
ifadelerini** kullanırız:


    .. sourcecode:: python3
        :linenos:
        
        if x < y:
            STATEMENTS_A
        elif x > y:
            STATEMENTS_B
        else:
            STATEMENTS_C

.. admonition:: Zincirleme koşul ifadesinin akış diyagramı

 
    .. image:: illustrations/flowchart_chained_conditional.png        

``elif``, ``else if`` ifadesinin kısaltılmışıdır. Daha öncede olduğu gibi sadece
bir dal (yol) yürütülecektir. ``elif`` deyimlerinin sayısında bir sınırlama
yoktur fakat tek ( ve isteğe bağlı) ``else`` deyimine izin vardır ve bunun son
deyim (son dal) olması gereklidir. 


    .. sourcecode:: python3
        :linenos:
        
        if secim == "a":
            function_one()
        elif secim == "b":
            function_two()
        elif secim == "c":
            function_three()
        else:
            print("Geçersiz seçim.")

Herbir koşul sırası ile sınanır. Eğer ilki yanlış ise bir sonraki kontrol edilir
ve böyle gider. Eğer herhangi bir tanesi doğru ise ilgili dal yürütülür ve
deyimin işlevi biter. Eğer birden fazla koşul doğru olsa bile, sadece ilk
karşılaşılan doğru dal çalışır. 

.. index::
    single:: İçiçe koşullar
    single:: koşullar; İçiçe

İçiçe koşullar
--------------

Bir koşul deyimi bir başka koşul deyimiyle içiçe olabilir. Bir önceki örneği
aşağıdaki gibi yazabildik:

.. admonition:: Bu içiçe koşulun akış diyagramı


   .. image:: illustrations/flowchart_nested_conditional.png

..

      .. sourcecode:: python3
          :linenos:

          if x < y:
              DEYİMLER_A
          else:
              if x > y:
                  DEYİMLER_B
              else:
                  DEYİMLER_C

Dışarıdaki koşul deyimi iki dal içermektedir. ikinci dal başka bir ``if``
cümlesi içerir ve bu cümle iki dal barındırır. Bu iki dal  da koşul deyimleri
içermelidir.

Her ne kadar deyimlerin girintisi yapıyı açık bir şekilde gösterse de, içiçe
geçmiş koşul deyimlerinin okunması gittikçe zorlaşır. Genellikle, bu tür içiçe
geçmiş koşul deyimlerinden kaçınmak gerekir.

Mantıksal işleçler içiçe koşul cümlelerini basitleştirmek için bir yöntem
sağlarlar. Örneğin aşağıdaki kodu tek bir koşul cümlesiyle yazabibilirsiniz:

    .. sourcecode:: python3
        :linenos:
        
        if 0 < x:            # x'in tamsayı olduğunu varsayın. 
            if x < 10:
                print("x pozitif ve tek basamaklıdır.")

``print`` fonksiyonu sadece iki koşulu da geçersek çalışır. Yukarıdaki örnekteki
iki ``if`` deyimini kullanmak yerine, ``and`` işleci kullanarak daha karmaşık
koşul deyimi oluşturabiliriz. Tek bir ``if`` deyimi 

    .. sourcecode:: python3
        :linenos:
        
        if 0 < x and x < 10:
            print("x pozitif ve tek basamaklıdır.")

.. index::
    single: geri dönüş (return) deyimi
    single: deyim; geri dönüş (return)

Geri dönüş deyimi
-----------------

Bir ``return`` deyimi bir fonksiyonun sona ulaşmadan bitirilmesini sağlar.
``return`` deyimini fonksiyon içinde erken kullanmamızın nedeni bir hata
durumuyla karşılaşmamız olabilir.

    .. sourcecode:: python3
        :linenos:
        
        def karekok_bas(x):
            if x <= 0:
                print("Sadece pozitif sayılar lütfen")
                return
        
            result = x**0.5
            print("x'in kare kökü", result)

``karekok`` fonksiyonu ``x`` isimli bir parametreye sahiptir. Bu fonksiyonun ilk
yaptığı işlem, ``x``'in 0'dan küçük veya eşit olması durumunda bir hata mesajını
ekrana basar ve ``return``'i kullanarak fonksiyondan çıkar. Yürütme akışı hemen
çağıran yere geri döner ve fonksiyonun geri kalan satırları çalıştırmaz.

Mantıksal işleçlerin karşıtları
-------------------------------

altı bağlantı işleçinin her birinin manktıksal karşıtı (zıttı) vardır. Örneğin,
yaşınız 18 veya 18'den daha büyük ise ehliyet alabileceğinizi, 18'den küçük ise
ehliyet alamıyacağınızı varsayalım. 

``>=``'in karşıtının ``<`` olduğuna dikkat ediniz.

  ========  =================
  işleç     mantıksal karşıtı     
  ========  =================
  ==        !=
  !=        ==
  <         >=
  <=        >
  >         <=
  >=        <
  ========  =================
 


Bu mantıksal karşıtlıkları anlamanız, bazen size  ``not`` işlecini
kullanmamanıza yardım eder.``not`` işlecini bilgisayar kodunda okumak genelde
zordur. Eğer ``not`` işlecini yok edersek, kod içindeki amacımız daha kolay
anlaşılacaktır.

Örneğin, bunu Python'da yazsaydık:

    .. sourcecode:: python3
        :linenos:
        
        if not (yas >= 18):
            print("Ehliyet almak için çok gençsiniz!")
 
Eğer basitleştirme kurallarını kullansanız, yukarıdaki kodu daha açık hale
gelebilir. Şu şekilde yazabiliriz:

    .. sourcecode:: python3
        :linenos:
        
        if age < 18:
            print("Ehliyet almak için çok gençsiniz!")

Karışık Boolean ifadeleri ile ugraşırken iki basitleştirme kuralı (De Morgan
kurralları)  oldukça yararlıdır:

      .. sourcecode:: pycon
    
          not (x and y)  ==  (not x) or (not y) 
          not (x or y)   ==  (not x) and (not y)

Örneğin, bilgisayar oyunumuzdaki bir canavarı ancak ışık kılıcımız %90 veya daha
yüksek seviyede ve savunma kalkanımızda tam dolu (%100) ise öldürebileceğimizi
varsayalım. Python ile yazılmış oyun kodunda bunu aşağıdaki gibi bulabiliriz:

      .. sourcecode:: python3
        :linenos:
        
        if not ((isin_kilici >= 0.90) and (kalkan_enerjisi >= 100)):
            print("Saldırmanız faydasız; canavar sizi perişan eder. ")
        else:
            print("Canavar parçalarına ayrılır. Prensesi kurtarıyorsunuz!")

Mantıksal karşıt ifadeleri ile De Morgan kuralları bize koşulları yeniden
düzenlemeye imkan vererek daha anlaşılır ifadeler yaratmamamıza imkan verir:


    .. sourcecode:: python3
        :linenos:
        
        if (isin_kilici < 0.90) or (kalkan_enerjisi < 100):
            print("Saldırmanız faydasız; canavar sizi perişan eder. ")
        else:
            print("Canavar parçalarına ayrılır. Prensesi kurtarıyorsunuz!")

``then`` ve ``else`` içindeki ``print`` fonksiyonunun yerlerini değiştirerek
``not`` işlecini yukarıdaki örnekten kaldırabiliriz:

    .. sourcecode:: python3
        :linenos:
        
        if (isin_kilici >= 0.90) and (kalkan_enerjisi >= 100):
            print("Canavar parçalarına ayrılır. Prensesi kurtarıyorsunuz!")
        else:
            print("Saldırmanız faydasız; canavar sizi perişan eder.")

Bu sürüm, olasılıkla yukarıdaki üç sürümün en iyisidir, çünkü başlangıçtaki
İngilizce duruma en yakın olanıdır. Kodunuz anlaşılır olması ( diğer kişiler
için) ve kodunuzun ne yaptığını kolayca görebilmek sizin yüksek önceliğiniz
olmalıdır.

Programlama yeteneklerimiz geliştikçe herhangi bir problemin çözümünün birkaç
yolunu bulacağız. Böylece iyi programlar *tasarlanır.* Programlarda, açıklık, basitlik ve güzellik ararız. Bizler bir mimar gibi, ürünlerimizde güzellik, işlerlik, basitlik ve açıklık arasında bir denge kurmaya çalışırız. 

.. admonition:: ipucu

    Programımız çalışır çalışmaz, o program çevresinde biraz oynayarak
    cilalamalıyız. Programda iyi açıklayıcı bilgiler yazın. Başka değişken
    isimleri kullanarak kodun daha açık olup olmayacağını düşünün. Bunu daha şık
    yapabilir miydiniz? Fonksiyon kullanmamız gerekli midir? Koşul deyimlerini
    basitleştirebilir miyiz?

.. index:: 
    single: tip dönüşümü
    single: tip; dönüşüm

Tip dönüşümü
------------

Bu konuya daha önceki konularda değinmiş olmalıydık. Burda işlemenin bir zararı
olmayacaktır!

Bir değişken tipini kendi tip değişkenine çevirmeye yarayan Python'da yerleşik
fonksiyonlar vardır. Örneğin, ``int`` fonksiyonu herhangi bir değişkeni alır ve
onu tam sayıya çevirmeye çalışır. Eğer başarısız olursa hata bildirimi verir. 


    .. sourcecode:: python3
        
        >>> int("32")
        32
        >>> int("Hello")
        ValueError: invalid literal for int() with base 10: 'Hello'

``int`` fonksiyonu, kayan noktalı değerleri tam sayıya çevirir. Hatırlayınız ki,
kesirli kısmı kesip atar:

    .. sourcecode:: python3
        
        >>> int(-2.3)
        -2
        >>> int(3.99999)
        3
        >>> int("42")
        42
        >>> int(1.0)
        1

``float`` fonksiyonu ise tam sayıları ve karakter dizilerini kayan noktalı
sayılara çevirir.


    .. sourcecode:: python3
        
        >>> int(-2.3)
        -2
        >>> int(3.99999)
        3
        >>> int("42")
        42
        >>> int(1.0)
        1

Python'un tam sayı olan ``1`` ile kayan noktalı sayıl olan ``1.0``\ ı birbirinden
farklı değerlendirmesi size garip gelebilir. İki sayı da aynı sayıyı temsil ederler,fakat
farklı tiplere aittirler. Bunun nedeni bilgisayar içinde farklı biçimlerde
temsil edilmeliridir. 

``str`` fonksiyonu, herhangi bir argümanı karakter dizisine (``string``)
çevirir:

    .. sourcecode:: python3
        
        >>> str(32)
        '32'
        >>> str(3.14149)
        '3.14149'
        >>> str(True)
        'True'
        >>> str(true)
        Traceback (most recent call last):
          File "<interactive input>", line 1, in <module>
        NameError: name 'true' is not defined

``str`` herhangi bir değerle çalışabilir ve o değeri karakter dizisine çevirir.
Daha önce de bahsedildiği gibi ``True`` bir Boolean değerdir; ``true`` ise
herhangi bir değişkendir ve burda tanımlanmamıştır. Bu yüzden hata alırız. 

.. index:: çubuk grafikler

Kamplumbağa Çubuk Grafikleri
----------------------------

Şimdi göreceğimiz kamplumbağa daha önce gördüklerimize göre daha çok güce sahip
olacaktır. Bununla ilgili dökümanlara http://docs.python.org/py3k/library/turtle.html
adresinden veya PyScripter'in içindeki *Help* menüsünden turtle modülünü
araştırabilirsiniz. 

Bizim kamplumbağlarımız için birkaç yeni zekice ipuçları vereceğiz:

* Kamplumbağamızın kanvas üzerindeki mevcut yerini ekranda göstermesini
  sağlayabiliriz. Bunun için kullanacağımız yöntem ``ahmet.write("Merhaba")``
  olacaktır.

* Bir şekli (çember, yarım çember, üçgen, vb. ) bir renk ile dolduracağız. Bunu
  iki adımda yapacağız. İlk önce ``ahmet.begin_fill()`` yöntemini çağırırız,
  sonra bir şekil çizer ve daha sonrasında ``ahmet.end_fill()`` yöntemini
  çağırırız. 

* Daha öncesinde kamplumbağamızın rengini belirledik. Biz aynı zamanda şekil
  doldurma rengini belirliyebiliriz. Bu rengin kamplumbağ ve kalem rengi ile
  aynı olması gerekmez. ``ahmet.color("blue","red")`` yöntemini kullanarak
  kamplumbağanın mavi çizmezini ve şeklin içini de kırmızı doldurmasını
  sağlayabiliriz. 

O zaman,  kamplumbağamızın bir çubuk grafik (bar chart) cizmezini   sağlayabilir miyiz? Çizilecek grafik için bazi verileri verelim: ``xs = [48, 117, 200, 240, 160, 260, 220]``

Her bir veriye karşılık gelen yükseklikte ve sabit bir genişlikte bir basit
dikdörtgen çizeceğiz.


    .. sourcecode:: python
        :linenos:

        def cubuk_ciz(t, yukseklik):
            """ t isimli kamplumbağanın verilen yukseklikte bir çubuk çizmesini
            sağlar"""
            t.left(90)           
            t.forward(yukseklik)     # Draw up the left side
            t.right(90)
            t.forward(40)         # Width of bar, along the top
            t.right(90)
            t.forward(yukseklik)     # And down again!
            t.left(90)            # Put the turtle facing the way we found it.
            t.forward(10)         # Leave small gap after each bar
     
        ...    
        for v in xs:              # xs ve tamer isimli kamplumbağanın hazır
                                  # olduklarını varsayalım. 
            cubuk_ciz(tamer, v)    

..

      .. image:: illustrations/tess_bar_1.png

Pek etkileyici olmasa bile iyi bir başlangıçtır! Önemli olan zihnimize uyan
parçalara ayırmak veya problemi daha küçük parçalara ayırmanın yolunu bulmaktır.
Bizim parçamız burda bir çubuk çizmek ve bunu yapan bir fonksiyon yazmaktır.
Daha sonra bütün bir grafik için fonksiyonumuzu tekrar tekrar çağırırız.

Daha sonra, herbir çubuk grafiğin en üstünde verimizin değerini basacağız.
``draw_bar`` fonksiyonunun içine ``t.write('  ' + str(yukseklik))`` yöntemini
üçüncü satıra yerleştireceğiz. Ekranda basılacak yüksekliğin önüne biraz boşluk
koyuyoruz ve yüksekliği ``string``'e ( karakter dizisi) çeviriyoruz. Bu fazladan
boşluk olmadan sayılarımız çubukların üstünde sola doğru sıkışmış olur. Sonuç
şimdi daha güzel olur:

    .. image:: illustrations/tess_bar_2.png
    
Ve şimdi herbir çubuğun içini doldurmak için iki satır ekleyeceğiz. Programızın
son hali şu şekilde olur:

    .. sourcecode:: python3
        :linenos:
       
        def cubuk_ciz(t, yukseklik):
            """ Get turtle t to draw one bar, of height. """
            t.begin_fill()           # Bu satır eklendi 
            t.left(90)
            t.forward(yukseklik)
            t.write("  "+ str(yukseklik))   
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(yukseklik)
            t.left(90)
            t.end_fill()             # Added this line
            t.forward(10)                 

        wn = turtle.Screen()         # Bir pencere ve pencerenin özelliklerini
                                     # oluştur.
        wn.bgcolor("lightgreen")

        tamer = turtle.Turtle()       # Kamplumbağa Tamer'i oluştur ve
                                     # özelliklerini belirle
        tamer.color("blue", "red")
        tamer.pensize(3)

        xs = [48,117,200,240,160,260,220]

        for a in xs:
            cubuk_ciz(tamer, a)

        wn.mainloop()

Bu ise aşağıdaki daha doyurucu grafiği oluşturur:

    .. image:: illustrations/tess_bar_3.png

Belki de çubukların altı birbirleriyle bağlanmasa daha güzel olur. Bunun için, çubuklar
arasında boşluk bırakırken kalemi kaldırmamız gerekecektir. Bunu size alıştırma
olarak bırakıyoruz. 

Sözlük
------

.. glossary::

    block
        Aynı girintiye sahip ardışık deyimler grubudur.

    gövde
        Bileşik deyimlerdeki başlığı takip eden deyimler bloğudur.

    Boolean cebri
        Boolean ifadelerini birleştirmede ve akıl yürütmede kullanılan kurallar. 

    Boolean ifadesi
        Sonucu doğru veya yanlış olan ifade

    Boolean değer
        İki tane Boolean değeri vardır: ``True`` and ``False``. Python yorumcusu 
        tarafından Boolean ifadeler üzerinde yapılan hesaplamalar sonucu çıkan
        Boolean değerleridir. Bunlar ``bool`` tipindedir. 

    dal
        Bir koşul tarafından belirlenen bir yürütme akış diyagramındaki olasılı yollardan biri.

    zincirleme koşul ifadesi
        İkiden fazla yürütme akış olasılığına sahip koşul dallanmasıdır.
        Python'da koşul ifadeleri ``if ... elif ... else`` deyimleri ile
        yazılmaktadır. 

    karşılaştırma işleçleri
        iki değeri karşılaştıran altı işleçlerden biridir: ``==``, ``!=``, ``>``,
        ``<``, ``>=``, and ``<=``.  

    koşul 
        Koşul deyimindeki Boolean ifadesidir ve hangi yolun (dalın)
        yürütüleceğine karar verir. 

    koşul deyimi
        Bazı koşullara göre yürütme akışını kontrol eden deyimdir. Python'da
        ``if``, ``elif`` ve ``else`` anahtar kelimeleri koşul cümleleri için
        kullanılmaktadır. 

    mantıksal işleç:
        Boolean ifadeleri birleştire işleçlerdir: ``and``, ``or`` ve ``not``.

    içiçe geçme
        Bir program yapısının bir başka program yapısı içinde bulunmasıdır.
        Örnek olarak, bir koşul deyiminin bir başka koşul deyimi içinde
        dallanmasını verebiliriz.

    bilgi istemi (prompt)
        Kullanıcıya veri girmesini söyleyen görsel ipucu.

    doğruluk tablosu
        Mantıksal işleçlerin değerler üzerine uygulanması sonucu ortaya çıkan
        ``Boolean`` değerlerini gösteren tablo.

    tip dönüşümü
        Bir tipteki değeri alıp başka bir tip değerine dönüştüren fonksiyon.

    kodu fonksiyonun içine yerleştirme
        Bir fonksiyon başlığı ve fonksiyonun alacağı parametreleri belirleme
        sürecidir. Program içindeki deyimlerin birkaç kere kullanılması
        gerektiğinde bu süreç oldukça faydalıdır. Bir karmaşık problemin nasıl
        parçalara ayrılacağına imkan vermesi dolayından bu faydası daha da
        artar. 

Alıştırmalar 
-------------

#. Pazardan Cumartesine kadar bir haftanın  günlerinin 0,1,2,3,4,5,6 olarak
   sayılandırıldığını varsayın. Verilen sayıya karşılık gelen günü geri döndüren
   (``string`` olarak) bir fonksiyon yazınız.

#. 3 numaralı günde (Çarşamba) harika bir tatile gittiğinizi ( belki de hapishaneye, eğer mutlu
   alıştırmalardan hoşlanmıyorsanız). 137 gün uyuduktan sonra eve dönüyorsunuz.
   Size gittiğiniz günü ve kalma süresini soran program yazınız. Bu program
   döndüğünüz günün ismini ekranda basmalıdır.

#. Aşağıdaki mantıksal ifadelerin karşıtlarını veriniz:
    
    #.  ``a > b`` 
    #.  ``a >= b``
    #.  ``a >= 18  and  day == 3``
    #.  ``a >= 18  and  day != 3``

#. Aşağıdaki ifadeler hangi değerleri verir?
    
  
        #.  ``3 == 3``
        #.  ``3 != 3``
        #.  ``3 >= 4``
        #.  ``not (3 < 4)``
 
#. Aşağıdaki doğruluk tablosunu tamamlayın:


          === === ======  =======
          p   q   r       (not (p and q)) or r
          === === ======  =======
          F   F   F        ?
          F   F   T        ?
          F   T   F        ?
          F   T   T        ?
          T   F   F        ?
          T   F   T        ?
          T   T   F        ?
          T   T   T        ?
          === === ======  ======= 
  
#. Aşağıdaki tabloya göre verilen sınav sonucuna karşılık gelen ve bu sonuca
   göre başarısını gösteren bir fonksiyon yazınız. 
    
           =======   =========
           Not       Derece
           =======   =========
           >= 85     Pek iyi 
           [60-85)   İyi   
           [50-60)   Orta  
           [25-50)   Zayıf  
           25 <      Başarısız
           =======   ========= 
 
    Köşeli parantez ``[``  ve yuvarlak parentez ``(`` sırasıyla kapalı ve açık
    aralıkları temsil ederler. Kapalı aralık   sayıyı açık aralığa dahil, açık aralık ise
    sayıyı dışlar. Örnek olarak 24.999999 alan birisinin derecesi Başarısız
    olacaktır fakat 25 alan birisinin derecesi Zayıf olacaktır. 

    Bir sınıfta alınan notlar aşağıdaki gibi olsun::
            
       xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 
                            49.9, 45, 44.9, 40, 39.9, 2, 0] 

    Listedeki bütün notları ve bunlara karşılık gelen dereceleri basarak
    yazdığınız fonksiyonu sınayınız.

#. Daha önce yazdığınız cubuk grafik programını değiştirerek herbir çubuk
   arasındaki boşlukta yatay çizgiler olmasın ( kalem'i yukarı kaldıran
   fonksiyonu kullanın).

#. Çubuk grafik programını değiştiriniz. Çubuğun yükselikliği 200 ve daha büyük
   ise içini kırmızı; [100, 200) arasında ise içini sarı; 100'den daha küçük ise
   yeşil ile doldurun. 

#. Çubuk grafik programınızda kullandığınız listedeki değerlerden biri veya daha
   fazlasının negatif olması durumunda ne olmasını beklersiniz? Deneyin! Çubuk
   grafik programını değiştirerek negatif değerleri çubuğun dibine yerleştirin. 

#. ``bul_hipotenus`` isimli fonksiyon yazınız. Bu fonksiyon, dik kenarlı üçgende
   verilen kenarları parametre olarak alıp hipotenüsün uzunluğunu geri
   döndürsun (İpucu: ``x ** 0.5``, ``x``'in kare kökünü döndürecektir.)

#. ``dik_ucgenmi`` adlı bir fonksiyon yazınız. Bu fonksiyon, üç kenarının
   uzunluğu verilen bir üçgeninin dik üçgen olup olmayacağını bulacak.
   Fonksiyona verilecek üç parametreden en sonuncusunun en uzun kenar olduğunu
   varsayın. Bu fonksiyon, üçgen dik üçgen ise ``True`` olarak, aksi
   takdirde ``False`` olarak geri dönecek.

   İpucu: Kayan noktalı sayılar hesaplaması her zaman kesin olarak doğru
   değildir. Bu yüzden kayan noktalı sayıların eşitlik işleçinde kullanılması
   güvenli değildir. Eğer iyi bir programcı, ``x``'in ``y``'ye eşit olup
   olmadağını veya yeteri kadar eşit olduğunu bilmek isterse, aşağıdaki gibi
   kodu yazabalir:

   .. sourcecode:: python3
        
        if abs(x-y) < 0.000001: # if x, y'ye yaklaşık olarak eşittir. 
            ...

#. Yukarıdaki programı genişletiniz ki fonksiyona argüman olarak girilecek
   kenarlar herhangi bir sırada olabilsin. 

#. Eğer kayan noktalı sayılar hesaplamalırının bazen niçin doğru sonuç
   vermediğini merak ediyorsanız; bir kağıt parçası üzerinde 10'u 3'e bölünüz ve
   kesirli kısmı kağıt üzerinde yazınız. Kesirli kısmın sürekli olarak devam
   edeceğini göreceksiniz. Bu yüzden sonsuz uzunlukta bir kağır parçasına
   ihtiyacınız olacaktır. Sayıların bilgisayar veya hesap makinasında  temsili aynı
   sorunla karşılaşır: Bellek sınırlıdır ve bazı basamaklar ihmal edilebilir. Bu
   yüzden küçük hatalar yavaşça hesaplamalara girer. Aşağıdaki betiği deneyin:

    .. sourcecode:: python3
        :linenos:

        import math
        a = math. sqrt(2.0)
        print(a, a*a)
        print (a*a == 2.0)



        

 
        














