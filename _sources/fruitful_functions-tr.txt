Ürün veren fonksiyonlar
=======================

.. index:: dönüş deyimi, dönüş değeri, geçici değer, ölü kod, None, ulaşılmayan
   kode

.. index:: 
    single: değer
    single: değişken; geçici


Geri dönüş değerleri
--------------------

Şimdiye kadar kullandığımız ``abs``, ``pow``, ``int``, ``max`` ve ``range``  
benzeri Python'un içinde tanımlı fonksiyonlar bir sonuç ürettiler. Bu
fonksiyonları her çağrımızda, fonksiyon bir değer üretir. Bu değerleri genellikle
bir değişkene atar   veya bir ifadenin parçası içinde kullanırız.



    .. sourcecode:: python3
        :linenos:

        enbuyuk = max(3,7,2,5)
        x = abs (3-11) + 10

Bileşik faiz hesabı yapıp, bu değeri bize döndüren kendi fonksiyonumuzu da
yazdık. 

Bu bölümde değer döndüren başka fonksiyonlar yazacağız ve bunlara *ürün veren
fonksiyonlar* adını vereceğiz. İlk örnek olarak, yarıçapı verilen bir dairenin
alanını hesaplayan ``alan`` fonksiyonunu vereceğiz:

    .. sourcecode:: python3
        :linenos:

        def area(yaricap):
            b = 3.14159*yaricap**2
            return b

Daha önce return deyimini gördük, ancak ürün veren bir fonksiyonda return deyimi
bir geri dönüş değeri verir. Bu cümlenin anlamı:  Bu fonksiyonunun dönüş
ifadesini hesapla ve hemen bunu fonksiyonun  sonucu (ürünü) olarak döndür. Dönüş
ifadesi isteğimize bağlı olarak karmaşık olabilir, örneğin yukarıdaki fonksiyonu
şöyle yazabilirdik:

    ..  sourcecode:: python3    
        :linenos:

        def alan(yaricap):
            return 3.14159*yaricap*yaricap

Diğer bir taraftan, ``b`` gibi **geçici değerleri** kullanmak hata ayıklamayı
kolaylaştırır. 

Bazı durumlarda, birden fazla dönüş deyimine sahip olmak faydalıdır. Herbir
dönüş değeri koşullu dalllanma içine yerleştirilir. Phyton'un içinde tanımlı
``abs`` fonksiyonunu daha önce görmüştük. Şimdi bu fonksıyonu kendimiz yazalım:
 
.. _my-ref-mutlakdeger:

    .. sourcecode:: python3   
        :linenos:
        
        def mutlak_deger(x):
            if x<0:
                return -x
            else:
                return x

Yukarıdaki fonksiyonu başka türlü yazmanın yolu ``else`` deyimini kaldırıp,
``if`` koşul gövdesinden sonra  ikinci bir ``return`` deyimi yazmaktır.   

      .. sourcecode:: python3
        :linenos:
        
        def mutlak_deger(x):
            if x < 0:
                return -x
            return x


Yukarıdaki örnek hakkında düşünüp, aynen ilki gibi çalıştığına kendinizi ikna
edin.``return`` deyiminden sonra gelen herhangi bir kod veya yürütme akışı açısından
erişilemez durumda olan kodlar **ölü kod** veya **erişilemez kod** olarak
adlandırılır. 

Bir ürünlü fonksiyonda olası her yolda bir ``return`` deyiminin olması iyi bir
fikirdir. ``mutlak_deger`` fonksiyonun aşağıdaki hali bunu
gerçekleştirememektedir. 

    .. sourcecode:: python3
        :linenos:

        def kotu_mutlak_deger(x):
            if x < 0:
                return -x
            elif x >0:
                return x

Fonksiyonumuzun bü sürümü doğru değildir çünkü eğer ``x``'in değeri 0 olduğunda,
hiçbir koşul değildir ve fonksiyon ``return`` deyimiyle karşılaşmadan sona erer. Bu durumda geri dönüş değeri **None (hiçbir şey)** olan özel bir değer olacaktır.  

``for`` döngüsünün ortasında ``return`` deyimini kullanmak mümkündür, bu durumda
``return`` deyimine rastlandığında fonksiyonun çalışması sona erer. Örneğin bir
kelime listesine bakan bir fonksiyon yazmak istiyoruz. Bu fonksiyondan, liste içinde iki harften oluşan ilk kelimeyi bulmasını istiyoruz. Eğer böyle bir kelime yoksa, boş bir karakter dizisi döndürmesini istiyoruz. 

    .. sourcecode:: python3
        :linenos:

        def 2harfli_ilk_kelimeyi_bul(xs):
            for kel in xs:
                if len(kel) == 2:
                    return kel
            return ""

    .. sourcecode:: python3

        >>> 2harfli_ilk_kelimeyi_bul(["Yazık", "Bu", "bir", "ölü", "papağandır"])
        'Bu'
        >>> 2harfli_ilk_kelimeyi_bul(["Ben", "papağandan", "hoşlanırım"])
        ''

Bu kodu tek adımla çalıştırın ve ilk durumdaki durum için fonksiyon listenin
ikinci kelimesinde sonuç döndürür. Bütün listeyi arşınlamak zorunda değildir. 

.. index:: iskele kurmak, arttırmsal geliştirme

Program geliştirme
------------------

Bu noktada, tamamlanmış fonksiyonlara bakarak ne yapabildiklerini
anlatabilmelisiniz. Ayrıca, alıştırmaları yapıyorsanız, bazı küçük fonksiyonlar
yazmış olmalısınız. Daha büyük fonksiyonlar yazdıkça zorlanmaya  başlar ve 
özellikle çalışma zamanı ve sözdizimi hataları yaparsınız. 

Artan karmaşık programlarla başa çıkabilmek için, **arttırımsal geliştirme**
tekniğini önereceğiz. Arttırımsal geliştirmenin hedefi, uzun hata ayıklama
süreçlerini kısaltmak için  programa küçük kodlar eklemek ve bu kodları
sınamaktır. 

Örneğin, iki nokta arasındaki uzaklığı bulma istediğimizi varsayalım.
Koordinatları verilmiş :math:`(x_1,y_1)` ve :math:`(x_2,y_2)` noktaları
arasındaki uzaklığı Pisagor teoremine göre şu şekilde hesaplarız. 

.. math::
        
    \mathrm{uzaklık} = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}

İlk adımımız ``uzaklık`` fonksiyonunun Python'da nasıl oluşturulacağını
anlamaktır. Başka bir ifadeyle, bu fonksiyonunun "girdileri (parametreleri)
ve çıktısı (dönüş değeri) nedir?" sorusuna cevap bulmaktır. 

Bu durumda, iki nokta girdilerimizdir. Bu iki noktayı dört parametre ile ifade
edebiliriz. Çıktımız ise uzaklıktır, bu da kayan noktalı bir sayıdır. 

Bu cevaplardan sonra fonksiyonumuzun ana hatlarını yazabiliriz.

    .. sourcecode:: python3
        :linenos:

        def uzaklik(x1,y1,x2,y2)
            return 0.0

Bu haliyle fonksiyonumuzun uzaklığı hesaplamadığı açıktır; her zaman sıfır
değerini döndürecektir. Fakat sözdizimi olarak doğrudur ve bu fonksiyon
çalışacaktır. Bunun anlamı, onu daha fazla karmaşık hale getirmeden önce
sınayabiliriz. 

    .. sourcecode:: python3

        >>> uzaklik(1,2,4,6)
        0.0

Bu değerleri seçtik ki; dikey uzunlık 3, yatay uzaklık 4 olsun ve böylece
sonucumuz 5'e eşit olur (dik ücgende 3-4-5 kuralı.) Bir fonksiyonu sınarken,
doğru sonucu bilmek yararlıdır.

Bu noktada fonksiyonun sözdizimsel olarak doğru olduğunu onaylamış olduk ve daha
fazla satır kodu ekleyebiliriz. Her bir arttırımsal değişiklikten sonra,
fonksiyonumuzu yeniden sınayabiliriz. Eğer bir noktada hata oluşursa, fonksiyona
eklediğimiz son satırların hata oluşturduğunu söyleyebiliriz.

Daha sonraki adımımız :math:`x_2-x_1` ve :math:`y_2-y_1` farklarını bulmaktır.
Bu değerleri geçici olarak ``dx`` ve ``dy`` değerlerinde saklayacağız. 

    .. sourcecode:: python3
        :linenos:

        def uzaklik(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            uKare = dx*dx + dy+dy
            return 0.0

Eğer bu fonksiyonu yukarıdaki argümanlar ile çağırarsak, program akışı
``return`` deyimine ulaştığında, ``dx``'in değeri 3 ve ``dy``'nin değeri 4
olmalidır. Bu durumu **PyScripter** kullanarak kontrol edebilirsiniz: Fare
imlecini ``return`` deyiminin üstüne yerleştirin ve program ``return`` deyiminin
olduğu satıra geldiğinde duracaktır (F4 düğmesini kullanarak.) 

Eğer ``dx`` ve ``dy`` değerlerinin üstüne faremizi gezdirdiğimizde,
fonksiyonunun doğru argümanları aldığı ve hesaplamaları doğru yaptığını
onaylayabiliriz. Eğer doğru değilse, yalnızca en son yazdığımız birkaç satırı
kontrol ederiz.

Daha sonra ``dx`` ve ``dy`` değişkenlerinin karelerini toplarız:


    .. sourcecode:: python3
        :linenos:
        
        def uzaklik(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            uKare = dx*dx + dy*dy
            return 0.0

Bu aşamada programı tekrar çalıştırıp, ``uKare``'nin (uzaklığın Karesi)
değerini buluruz ( 25 olmalıdır.) 

Son olarak, kesirsel üst ``0.5``'i kullanarak uzaklığın karekökü'nü hesaplar ve
sonuç olarak geri döndürürüz:

    .. sourcecode:: python3
        :linenos:
        
        def uzaklik(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            uKare = dx*dx + dy*dy
            sonuc = uKare**0.5
            return sonuc

Eğer bu doğru çalışırsa, işimiz bitmiştir. Çalışmazsa, ``sonuc`` değişkeninin
geri döndürmeden önceki değerini incelememiz gerekebilir.

Fonksiyonu yazmaya başladığınızda, bir anda sadece bir veya iki satır ekleminiz
gerekir. Deneyim kazandıkça kendinizi daha büyük parçalar yazıp, onları sınayıp
ve hata ayıklar durumda bulacaksınız. Her şekilde, kodunuzu anlık olarak satır
satır adımlamak ve her adımın beklentinize uyduğunu onaylamak sizin hata
ayıklama zamanınızı kısaltacaktır. Programlama yeteğinizi geliştirdikçe,
kendinizi daha büyük parçalar üzerinden hata ayıklar bulacaksınız. Bu bizim
okumayı öğrenirken ilk önce harfleri okumaya başlayıp, daha sonra heceleri,
kelimeleri, ifadeleri, cümleleri ve sonuçta paragrafları okur hale gelmemize
benzemektedir.

Bu sürecin ana hatları şunlardır: 

#. Çalışan bir programla başlayın ve bu program üzerinde küçük arttırımlar
   yapın. Herhangi bir noktada bir hata varsa hatanın nerede olduğunu
   bileceksiniz. 

#. Ara değerleri tutmak için geçici değişkenler kullanın; böylece bu değerleri
   inceleyibilir ve kontrol edebilirsiniz. 

#. Program çalışır hale gelince, rahatlayın, arkanıza yaslanın ve programınıza
   farklı işlemler yaptırarak oynayın.  ( Araştırmalar gösteriyor ku **oynamak**
   sizin bir şeyi daha iyi anlamanıza, neler yapabileceğiniz hakkında bir fikir
   elde edebilmenize yardımcı olur. Bu yüzden programınızla oynamayı
   unutmayınız.) 
   Fonksiyonun içindeki çeşitli deyimleri bir grup deyim içine toplamayı
   isteyebilir veya değişkenlerinizin isimlerini daha kısa hale
   getirebilirsiniz. Böylece fonksiyonunuz kısalır. Burdaki ilkemiz,
   programımızı okuyan insanların işlerini kolaylaştırmaktır. 

Aşağıda bu fonksiyonunun başka sürümünü bulacaksınız. Python'un ``math`` modülü
(modülleri daha sonra öğreneceksiniz.) içindeki karekök alma fonksiyonunu
kullanır. Hangisi tercih edersiniz? Hangisi Pisagor formülünü daha yakın
gözüküyor. 

    .. sourcecode:: python3
        :linenos:
        
        import math
        
        def uzakli(x1, y1, x2, y2):
            return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )  
   
    .. sourcecode:: python3

    >>> uzaklik(1,2,4,6)
    5.0

.. index:: hata ayıklama

``print`` ile hata ayıklama
---------------------------


Hata ayıklamada diğer bir kuvvetli  teknik ise  ( programı adımlama ve program
değişkenlerini incelemeye alternatif) programınızda dikkatlice seçtiğimiz
yerlere ``print`` fonksiyonlarını yerleştirmektir. Böylece programın çıktısını
inceleyerek, programımızın algoritmasının umduğumuz şeyleri yapıp yapmadığını
denetleyebiliriz. Fakat aşağıdaki noktalar hakkında berrak bir düşünceye sahip
olun: 

* Sorunun çözümü hakkında açık bir çözüme sahip olun ve hata ayıklamaya
  geçmeden önce programda neler olacağını bilmeniz gerekir. Programı yeniden
  yazmadan önce sorunun çözümü için 
  bir kağıt üzerinde çalışın ( belki de bir akış diyagramı üzerinde alacağınız
  adımları yazın.) Programı yazmak sorunu çözmez --- yalnızca atacağınız
  adımları otomatikleştirir. Elinizin altında kalem-kağıttan oluşan bir çözüm
  olmalıdır. 

* Gereksiz işler yapan fonksiyonlar yazmayın. Fonksiyonunuz ne yapması
  gerekiyorsa onu yapmalıdır.

  Örneğin ``range``, ``max`` ve ``abs`` gibi Python içinde tanımlı fonksiyonları
  görmüştük. Bu fonksiyonlar kendi amaçları dışında, eğer kullancıya giriş değeri
  sorsaydı veya hesaplamaları sırasında gereksiz yere ara sonuçları ekrana
  yazdırsaydı bu fonksiyonlar başka fonksiyonlar için yararsız olacaktı. 

  İyi bir ipucu olarak, eğer fonksiyonuzun amacı kullanıcıdan bir girdiyi
  beklemek ve çıktıyı ekrana bastırmak değilse ``print`` ve ``input``
  fonksiyonlarını ürün veren fonksiyonlar içinde kullanmaktan kaçının. Bu
  kurala istisna vardır: Hata ayıklamayı kolaylaştırmak ve programda çalışırken
  ne olduğunu anlamak için ``print`` fonksiyonunu kodunuz içine
  serpiştirebilirsiniz. Programınız çalışır çalışmaz, bu fonksiyonlar
  kaldıralacaktır. Örneğin daha önceki uzaklık fonksiyonumuzda, **Pyscripter**
  adım adım hata ayaklama yöntemini kullanmadan, yalnızca ``print`` fonksiyonunu
  kullanarak hata ayıklıyabilirdik:

    .. sourcecode:: python3
        
        def uzaklik(x1,y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            print("dx'nin değeri ", dx)
            print("dy'nin değeri = ", dy)
            uKare = dx*dx + dy*dy
            print("uKare'nin değeri = ", uKare)
            sonuc = uKare**0.5
            return sonuc

Yukarıdaki örnekte eğer ``dx``, ``dy`` ve ``uKare`` çıktıları beklediğimiz sonuçları veriyorsa
programımızın doğru çalıştığına emin olabiliriz. Böylece artık fonksiyonunun
içindeki ``print`` fonksiyonuna ihtiyacımız yoktur. Bunları kaldırmamız gerekir. 

.. index:: kompozisyon, fonksiyon kompozisyonu

Kompozisyon 
------------

Şimdiye kadar farketmiş olacağınız üzere, bir fonksiyonu başka bir fonksiyondan
çağırabilirsiniz. Bu yeteneği kompozisyon (bileşim) adı verilmektedir. 

Örnek olarak, dairenin merkezi ve çevresi üzerinde iki nokta alıp, dairenin
alanını hesaplayan bir fonksiyon yazacağız.  

Merkez noktanın ``xc`` ve ``yc`` değişkenlerinde; çevre üzerindeki
değişkenlerin de ``xp`` ve ``yp`` değişkenlerinde saklandıklarının varsayalım.
İlk yapmamız gereken, iki nokta arasındaki uzaklıktan yarıçapı
bulmaktır. Daha önce yazdığımız ``uzaklik`` fonksiyonunu iki nokta arasındaki
uzaklığı  hesaplamak için kullanabiliriz:

    .. sourcecode:: python3
        :linenos:

        yaricap = uzaklik(xc, yc, xp, yp)

İkinci adım ise bulduğumuz bu yarıçapı kullanarak dairenin alanını hesaplayıp
geri döndürmektir. Yine daha önce yazdığımız fonksiyonları kullanacağız.

    .. sourcecode:: python3
        :linenos:

        sonuc = alan(yaricap)
        return sonuc

Bu kodları diğer bir fonksiyon içinde yazarsak:

    .. sourcecode:: python3
        :linenos:

        def alan2(xc,yc, xp, yp):
            yaricap = uzaklik(xc, yc, xc, yp)
            sonuc = alan(yaricap)
            return sonuc

Daha önce tanımladığımız ``alan`` fonksiyonundan ayırtetmek için ``alan2``
fonksiyonunu kullandık. 

Geçici ``yaricap`` ve ``sonuc`` değişkenleri program geliştirme, hata ayıklama
ve adım adım program üzerinden ne olduğunu anlamak için yararlıdır. Programımız
çalışır çalışmaz, fonksiyon çağrılarını birleştirirsek (kompozisyon) daha az ve
kısa hale getirmiş oluruz:

    .. sourcecode:: python3
        :linenos:

        def alan2(xc, yc, xp, yp):
            return alan(uzaklik(xc, yc, xp, yp))

.. index:: Boolean fonksiyonlar 

Boolean (Doğru ve Yanlış ) fonksiyonları
----------------------------------------

Fonksiyonlar Boolean değerler ( Doğru=True, False=Yanlış) döndürebilirler.
Bunlar karmaşık sınamaları fonksiyon içinde saklamak için yararlıdır. Örneğin:


    .. sourcecode:: python3
        :linenos:
        
        def bolunebilirmi(x, y):
            """ x, y tarafından tam bölünebilir olup olmadığını sına """
            if x % y == 0:
                return True 
            else:
                return False 

**Boolean fonksiyonlarına** genelde evet/hayır sorusuymuş gibi isim verilir.
``bolunebilirmi`` fonksiyonu, ``x``'in ``y`` tarafından bölünebilir olup olmadığına
göre ``True`` veya `False`` döndürecektir. 

``ıf`` deyiminin kendisinin de bir Boolean ifadesi olduğu gerçeğinden
yararlanarak fonksiyonu daha kısa ve öz hale getirebiliriz. Doğrudan sonucu
döndürerek, ``if`` deyiminden kurtulabiliriz:

    .. sourcecode:: python3
        :linenos:

        def bolunebilirmi(x,y):
            return x % y == 0

Aşağıda bu yeni fonksiyonunun nasıl kullanıldığını görebilirsiniz:

    .. sourcecode:: python3

        >>> bolunebilirmi(6, 4)
        False
        >>> bolunebilirmi(6, 3)
        True

Boolean fonksiyonları genelde koşul cümlelerinde kullanılır: 

    .. sourcecode:: python3
        :linenos:

        def bolunebilirmi(x,y):
            if bolunebilirmi(x,y):
                ... # birşey yap
            else:
                ... # yoksa başka birşey yap

Aşağıdaki gibi bir şey yazmak cazip olabilir:

    .. sourcecode:: python3
        :linenos:

        if bolunebilirmi(x, y) == True:

Ancak ek karşılaştırma gereksizdir.

.. index:: tarz

Program yazım kuralları
-----------------------

Okunabilirlik programcılar açısından çok önemlidir, çünkü pratikte programlar
yazılmaktan ziyade okunması ve değiştirilmesi sık karşılaşılan durumdur. Bu
kitapta yazılan kod örneklerin çoğu Python topluluğu tarafından geliştirilen *Python Geliştirme Önerisi 8*
(`PEP 8 <http://www.python.org/dev/peps/pep-0008/>`__) ile uyumlu olacaktır.

Programlarımız karmaşıklaştıkça yazım kuralları konusunda söyleyeceklerimiz
artacaktır, fakat birkaç noktayı açıklamak yararlı olacaktır:

* Girintiler için 4 boşluk karakteri kullanın.
* Bir satırın uzunluğu 78 karakteri aşmasın.
* Tanımlayıcı sözcükler için; ``CamelCase``'i  (örnek: `YillikFaizHesabi`,
  `GunlukSutMiktari`, vb.) `sınıflar` için kullanın ( ileriki bölümlerde
  sınıfları göreceğiz.) Değişkenler ve fonksiyonlar için ise hepsi küçük harf ile başlayan ve
  kelimerin arasında alt çizgi olan kelimeler seçin ( örnek: `yil_sonu_miktari`, `uzaklik_kare`
  vb.) 
* Python modüllerini dosyanın en başına koyun.
* Fonksyion tanımlamaları bir arada olmalıdır.
* Fonksiyonları belgelendirmek için docstrings kullanın.
* Arka arkaya gelen fonksiyon tanımlamaları arasında iki boş satır bırakın.
* En üst seviye cümleleri, fonksiyon çağırımları da dahil olmak üzere, programın
  en altında birlikte tutun. 

doctest ile birim sınama (unit test)
------------------------------------

Yazılım geliştirmede kaynok kodun **birim sınama**\ sını yapmak (unit test)
yaygın olan en iyi alışkanlıktır. Birim sınama, fonksiyonlar gibi bağımsız kod
parçalarının otomatik olarak doğru çalıştığını onaylamak için bir yol sağlar. Bu
daha sonra fonksiyonunun gerçekleştirimini değiştirmeyi ve yine de beklenini
yapmasına olanak kılar.

Birkaç yıl öncesine kadar, program kodu ve programa ait belgeleri firmalar
tarafından önemli bir varlık olarak değerlendiriliyordu. Bu organizasyonlar
yazılım bütçelerinin büyük bir kısmını bu programları test etmede (ve korumada)
kullanıyorlar. 

Birim sınaması, fonksiyonunun ele alması gereken çeşitli durumları programcıya
düşündürtür. Programın içine bir testi yalnızca bir kere yazarsınız; böylece
kodunuzu geliştirdikçe  tekrar tekrar aynı test verilerini program içine
girmekten kurtulursunuz.

Fazladan kodun programızın içinde bulunmasının nedeni,  programı test etmeyi ve hata
ayıklamayı kolaylaştırmasıdır. Bu **iskele** (scaffolding) olarak
isimlendirilir.

Bir kod için yapılacak testlerin bütününe **test takımı** denir. 

Python'da birim sınaması yapmak için birkaç farklı yol vardır. Python
ile uğraşan kişilerin genelde birim sınaması için yaptıklarıni şimdilik dikkate almayacağız ve kendi yazacağımız iki fonksiyon ile başlayacağız.

Bu bölümde daha önce yazdığımız ``mutlak_deger`` fonksiyonu ile başlayalım. Biz
farklı sürümlerini yazdık; en son yazdığımız sürümü hatalı bir sürümdü ve bir
böcek içeriyordu. Bu böceği yakalayabilmiş miydiniz?

İlk önce testimizi tasarlıyoruz. Fonksiyonun argümanı negatif, pozitif veya sıfır
olduğunda fonksiyonumuzun doğru değer döndürüp döndürmediğini bilmek istiyoruz.
Testimizi tasarlarken en uç durumları dikkatlice düşünmeliyiz. ``mutlak_deger``
fonksiyonunun argümanı sıfır olduğu durum,  ``mutlak_deger`` fonksiyonumuzun
davranışının değiştiği bir uç durumdur. Bu bölümün başında gördüğümüz üzere, bir
programcı beklenmeyen yerde hata yapar. Bu yüzden test takımımızda bun eklemek
iyi bir durumdu. 

Bir testin sonuçlarını denetlemek için yardımcı bir fonksiyon yazacağız. Bu
fonksiyon Boolean argümanı alacak. Testen geçtiğini veya testen başarız olduğunu
belirten bir mesajı ekrana basacak. Fonksiyon gövdesinin ilk cümlesi
(fonksiyonunun docstring'inden sonra) programın içinde fonksiyon çağrılmasının
yapıldığı satırı belirler. Bu yapılan testin satır numarasını belirler. Bu bize
hangi testlerin başarılı veya başarısız olduğunu belirlemede yardımcı olacak.


    .. sourcecode:: python3
        :linenos:

        import sys
        
        def test(did_pass):
            """  Test sonuçlarını basar """
            linenum = sys._getframe(1).f_lineno   # Çağırıcının satır numarasını belirler. 
            if did_pass:
                msg = "{0} satır testi ok.".format(linenum)
            else:
                msg = (" {0} satır testi BAŞARISIZ.".format(linenum))
            print(msg)

Katar dizisini hızlı bir şekilde biçimlendirmede kullanılan ``format``
fonksiyonuna birazdan göz gezdireceğiz ve ilerideki bölümde daha detaylı olarak
işleyeceğiz. Yazdığımız fonksiyon ile, test takımımızı kontrol etmeye
başlayabiliriz. 

    .. sourcecode:: python3
        
        def test_suite():
            """ Bu modül içindeki test takımını çalıştırır. 
            """
            test(mutlak_deger(17) == 17)  
            test(mutlak_deger(-17) == 17) 
            test(mutlak_deger(0) == 0) 
            test(mutlak_deger(3.14) == 3.14) 
            test(mutlak_deger(-3.14) == 3.14) 
        
        test_suite()        # Burda testi çağıyoruz. 
 
Burda gördüğünüz gibi test takımımız içinde 5 tane test oluşturduk. Biz bunu :ref:`multak_deger <my-ref-mutlakdeger>` fonksiyonunun birinci ve ikinci sürümleri (doğru sonuç veren fonksiyonlar)
çalıştırdığımızda aşağıdaki benzer çıktıyı alırız. 

    .. sourcecode:: pycon
        
        19 satır testi OK.
        20 satır testi OK.
        21 satır testi OK.
        22 satır testi OK.
        23 satır testi OK.

Şimdi ise fonksiyonu doğru olmayan sürüme çevirelim:

    .. sourcecode:: python3
        :linenos:
     
        def mutlak_deger(n):   # Bocekli sürüm
            """ n'nin mutlak değerini hesaplayalım. """  
            if n < 0:
                return 1
            elif n > 0:
                return n
    
Yukarıdaki fonksiyonda en az iki hata bulabilir misiniz? Bizim test takımımız bu
hataları bulabilir! Sonuçta 

    .. sourcecode:: pycon

            19 satır testi OK.
            20 satır testi BAŞARISIZ.
            21 satır testi BAŞARISIZ.
            22 satır testi OK.
            23 satır testi BAŞARISIZ.

Burda başarısız olan 3 test vardır.

Python'un içinde tanımlı **assert** deyimi **test** fonksiyonu ile hemen hemen
aynı şeyi yapar (programın ilk **savı** (assertion)  başarısız olduğunda program
çalışmasını durdurur. **assert** hakkında daha fazla okuyabilir ve bunu test
fonksiyonu yerine kullanabilirsiniz.

Sözlük
------

.. glossary::

    Boolean fonksiyon
        Boolean değer döndüren fonksiyon. ``False`` (yanlış) ve ``True``(doğru)
        değerleri ``bool`` türünün yalnız dönme değerleridir.

    chatterbox (konuşan) fonksyion
        ``input`` ve ``print`` deyimlerini kullanarak, gereksiz olarak kullanıcı ile etkileşime
        giren fonksiyonlara denir. Bu fonksiyonların karşıtı `sessiz
        fonksiyonlar` ise aldıkları argümanları bir çıktıya çevirirler. Bu
        fonksiyonlar genelde en faydalı fonksiyonlardır.

    kompozisyon (fonksiyonların)
        Bir fonksiyon gövdesinden bir başka fonksiyonu çağırmak veya bir
        fonksiyonun geri dönüş değerini, bir başka fonksiyonunun argümanı
        olarak kullanmak.

    ölü kod
        Bir kısım programın asla çalıştırılamamasıdır. Genelde sebebi fonksiyon
        içindeki ``return`` deyiminden sonra cümleler konulmasıdır. 

    ürün veren fonksiyon
        ``None`` dışında bir değer döndüren fonksiyon

    arttırımlı geliştirme
        Hata ayıklamayı kolaylaştırmak küçük miktarda bir kodun programa
        eklenmesi vo o anda çalıştırılmasına dayanan program geliştirme
        yöntemidir.

    None
        Özel bir Python değeri. Fonksiyon içinde ``return`` deyimi olmayan veya argümansız
        ``return`` deyimi içeren fonksiyonların döndürdükleri değerdir.

    geri dönüş değeri
        Bir fonksiyonun çağrılması sonucu sağlanan değer

    iskele (scaffolding)
        Programın geliştirilmesinde ve hata ayıklanmasına yardım etmek için
        programın içinde kullanılan kod. Bu bölümde kullandığımız `birim testi`
        iskele örnekleridir.

    geçici değişken
        Karmaşık hesaplamalarda ara değerleri saklamak için kullanılan değişken.

    test takımı
        Test yapmak için yazdığınız test sayısı (topluluğu)

    birim sınama (birim testi)
        Bağımsız kod parçalarını doğrulamak için kullanılan otomatik yordamlar.
        Bir kodun içinde test takımı bulundurmak, o kodu geliştiren veya
        düzenleyen kişi için çok faydalıdır. Daha önceden hatasız çalışan bir kodun 
        içinde bocek oluşmasını ve yeniden geriye dönmeyi engellemek  için bir güvenlik duvarı oluşturur. 
        *Geriye dönme sınaması* (regression testing) genelde 
        `programda gerilememek` fikrini vermesi için kullanılmaktadır. 

Alıştırmalar
------------



        
        




