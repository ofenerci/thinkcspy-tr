
Functions
=========

.. index::
    single: fonksiyon
    single: fonksiyon tanımı
    single: tanım; fonksiyon

Fonksiyonlar
------------

Belli bir işlemi gerçekleştirmek için gruplandırılmış komut (cümle) serisidir.
Fonksiyonların temel amacı üzerine düşündüğümüz programı parçalara ayırmada
bize yardım etmektir. 

**Fonksiyon tanımı**\ nın söz dizimi şu şekildedir:

    .. sourcecode:: python3
        
        def ISIM( PARAMETRE LİSTESİ ):
            KOMUTLAR

Fonksiyonlar için dilediğiniz ismi kullanabilirsiniz, ancak değişkenlerde  de
olduğu gibi Python anahtar kelimeleri kulannamazsınız. Değişkenlerde
kullandığımız isimleme kuralları fonksiyonlar için de geçerlidir. 

Fonksiyon içinde herhangi bir sayıda cümle olabilir, fakat bu cümleler
``def``'den sonra girintili olmak zorundadır. Kitaptaki örneklerde, standart
olan dört boşluk kullanacağız. Fonksiyon tanımlamaları gruplandırılmış cümlelerin
ikinci örneğidir ( ilk örneğimiz daha önceki bölümde gördüğümüz ``for``
deyimiydi.) Hepsinin de kalıbı aynıdır.

#. Bir **başlık** bir anahtar kelime ile başlar ve iki nokta üst üste ile biter. 

#. Bir **gövde**, bir veya daha fazla Python cümlesi içerir ve bu cümleler başlıktan aynı
   miktarda içeriye  girintilidir (*Python yazı rehberi 4 boşluk tavsiye eder.*) 

Daha önce ``for`` döngüsünün bu kalıbı izlediğini gördünüz. 

Fonksiyon tanımlanmasına yeniden bakarsak: Baştaki anahtar kelime ``def``
ifadesidir. Bu ifade, fonksiyonun ismi ve parantezin içine alınmış
parametreler izler. Parametre listesi boş olabilir veya birbirinden
virgüllerler ayrılmış herhangi bir sayıda parametre içerebilir. Her iki
durumda da parantezler gereklidir. Bir fonksiyonumuzu bir parametre yardımıyla
kullanıyorsak,  bu fonksiyona ne gibi bilgi sağlamamız gerektiğini gösterir. 

Varsayalam ki, biz kamplumbağalar ile çalışıyoruz ve yaptığımız işlem onlara
bir kare çizdirmek olsun. "Kare Çizdirme", küçük adımları olan bir
**soyutlama** veya zihinsel parçadır. Bu yapıtaşının kalıbını anlamak için bir
fonksiyon yazalım:

    .. sourcecode:: python3
       :linenos:
        
        import turtle 

        def kare_ciz(t, sz):
            """t isimli bir kamplumbağa'nın sz boyutunda bir kare çizmesi"""            
            for i in range(4):
                t.forward(sz)             
                t.left(90)
          
          
        wn = turtle.Screen()        # Pencere oluştur ve özelliklerini gir.
        wn.bgcolor("lightgreen")
        wn.title("Ahmet fonksiyon ile buluşuyor")

        ahmet = turtle.Turtle()      # ahmet adlı kamplumbağa oluştur. 
        kare_ciz(ahmet, 50)       # Fonksiyonu çağır ve kare çiz. 
        wn.mainloop()

        
    .. image:: illustrations/alex04.png 

 
Fonksiyonumuz ``kare_ciz`` olarak isimlendirdik. İki tane parametresi vardır:
Birincisi hangi hangi kamplumbağa'nın haraket edeceğini; diğeri ise çizilecek
karenin boyutunu verir. Fonksiyonun gövdesinin nerde bittiğine dikkat edin. Bu
tamamen girintiye bağlıdır ve boşluk olan satırın bununla ilgisi yoktur. 

.. admonition:: Belgelendirme için *docstring (belge açıklar) **

    Fonksiyon başlığından sonkaki ilk satır bir karakter dizisidir ve bir
    **docstring**  (belgeaçıklar) olarak değerlendirilir; Python tarafından ve bazı
    programlama dilleri tarafından bunlar özel olarak değerlendirilir.
    Örneğin, Python'da tanımlanmış bir fonksiyonu PyScripter'da yazdığımızda
    --- parantezi kapatmadan önce --- bir ipucu penceresi gözükür ve bize
    fonksiyonun hangi argümanları aldığını (Ç.n: Argüman ile parametre hemen
    hemen  aynı
    anlama gelmektedir. Daha kesin dille,  bir fonksiyonu çağırıp fonksiyonun
    içindeki  parametreye
    bir değer atadığımızda, bu parametre artık  argüman olarak adlandırılır.)  ve docstringler içindeki metini gösterir.

    `Docstring'ler` belgemizin içindeki fonksiyonları belgelendirmek için
    önemlidir. Çünkü kim bir fonksiyonu çağırırsa, fonksiyonun nasıl
    çalıştığını veya fonksiyon içinde neler olduğunu bilmek zorunda değildir.
    Bilmeleri gereken; fonksiyonun hangi argümanları aldığı, bunların ne
    yaptığı ve bu fonksiyonun beklenen sonucudur. Bu fonksiyonun içeriğine
    bakmadan, bu fonksiyonu kullanmamıza yeterli olmalıdır. Bu kavram, daha
    sonraki bölümlerde deneceğimiz *soyutlamaya* dayanır. 

    Docstring'ler genelde üçlü tırnak içine alınırlar. Bunun nedeni daha
    sonra bu docstring'leri genişletmek istdeğimizde, bize kolaylık sağlar. 

    Docstring, belge yorumları ile karıştırmamak  gerekir. Bir
    docstring,  Python'un çalışma zamanı sırasında işlenir. Belge yorumları ise,  program     yorumlandığı sırada bu belge yorumları ihmal edilir. 

Bir fonksyionu tanımlamak, fonksiyonu çalıştırmak için yeterli değildir. Bu
fonksiyonu çalıştırmak için **fonksiyonu çağırmak** gerekir. Örneğin
**print**, **range** ve **int** gibi Python'da tanımlanmış bazı fonksiyonları
nasıl çağıracağımızı gördük. Fonksiyonu çağırma, işlenecek fonksiyon ismi ve
arkasından bu fonksiyona verilecek *argüman* denen değerler listesinin
parametrelere atanmasıyla olur. Yukarıdaki örnekte sondan ikinci satırda, bir
fonksiyon çağırıyoruz; görev verilen kamplumbağa olarak ``ahmet'i`` seçiyoruz  ve 50'yi
ise istedğimiz karenin boyutu olarak atıyoruz. Fonksiyon çalışırken, ``sz``
değşikeni 50'ye işaret eder; ``t`` değişkeni ise ``ahmet``'in işaret ettiği
kamplumbağaya işaret eder. 

Bir kere fonksiyonu tanımladığımızda, bu fonksiyonu istediğiniz kadar
çağırabilirsiniz. Bu fonksiyonu herbir çağırışımızda, onun cümleleri her
defasında yürütülecektir. Biz bu fonksiyonu, herhangi bir kamplumbağanın kare
çizmesi için kullanabiliriz. Sonraki örnekte, ``kare_ciz`` fonksiyonunu biraz
değiştirelim. Bu sefer ``tamer'in`` 15 tane farklı çeşitlilikte (renkleri ve
boyutları)  kare çizmesini
isteyeceğiz. 

    .. sourcecode:: python3
        :linenos:

        import turtle

        def renkli_kareler_ciz(t, sz):  
            """t kamplumbağasına her kenarı  farklı renklerde ve boyutu birbirinden farklı 15 kare çizdir. """
            for i in ["red", "purple", "hotpink", "blue"]:
                t.color(i)
                t.forward(sz)
                t.left(90)
     
        wn = turtle.Screen()        # Pencereyi oluştur ve özelliklerini
        belirle
        wn.bgcolor("lightgreen")

        tamer = turtle.Turtle()      # tamer'i oluştur ve özelliklerini ata
        tamer.pensize(3)

        size = 20                   # En küçük boyutlu karenin ölçüsü
        for i in range(15):
            draw_multicolor_square(tess, size)
            size = size + 10        # Her keresinde boyutu artır.
            tess.forward(10)        # tamer'i biraz yerinden oynat
            tess.right(18)          # ve biraz döndür. 

        wn.mainloop()

    .. image:: illustrations/tess05.png 

Fonksiyonlar başka fonksiyonları çağırabilir
--------------------------------------------

Şimdi ise fonksiyonumuza bir dikdörtgen çizdirmek istediğimiz varsayalım.
Genişlik ve yükseklik için farklı argümanlara sahip bir fonksiyonu
çağırabilmeliyiz. Kareden farklı olarak, aynı şeyi 4 kere tekrar edemeyiz,
çünkü 4 kenar birbirine eşit değildir. 

Bir dikdörtgen çizebilecek güzel bir kod oluşturalım:

      .. sourcecode:: python3
         :linenos:

         def dikdortgen_ciz(t,w,h):
            """ t kamplumbağasına  w genişliğinde ve h yüksekliğinde
            dikdörtgen çizdir"""

            for i in range(2):
               t.forward(w)
               t.left(90)
               t.forward(h)
               t.left(90)

Parametre isimleri yanlış anlamaya sebep vermemek için özellikle tek harf
seçilmiştir. Daha fazla deneyim kazandıkça, gerçek programlarda bu
parametrelerden daha iyi isimler seçebiliriz. Burdaki temel nokta, program
bizim bir ne bir dikdörtgen çizdiğimizi; ne de genişlik veya yüksekliği belirten
parametreleri anlar. Dikdörtgen, genişlik veya yükseklik gibi kavramlar
insanlar için bir anlam ifade eder. Bilgisayar veya program bu kavramları
anlayamaz.

*Bir bilgisiyar bilimcisi gibi düşünme*  örüntü (düzen) ve
bağıntı bulma gerektirir. Yukarıdaki programda, bunu bir dereceye kadar
yaptık. Yalnızca 4 kenar çizmedik. Bunun yerine, dikdörgen içinde bir örüntü
(düzen) baktık ve dikdörtgeni iki parçaya ayırdık. Kendini iki kere
tekrarlayan bu düzeni, loop döngüsü kullanarak iki kere tekrarladık.

Fakat şimdi karenin, dikdörtgenin özel bir hali olduğunu görebilirsiniz.
Halihazırda elimizde dikdörtgen çizen bir fonksiyon olduğundan, bunu bir kare
çizmek için kullanabiliriz. 

      .. sourcecode:: python3
         :linenos:

         def kare_ciz(tx,sz) # kare_ciz'in yeni sürümü
            dikdortgen_ciz(tx,sz,sz) 

Burda dikkat edilmesi gereken birkaç nokta vardır:

* Bir fonksiyon diğer bir fonksiyonu çağırabilir.
* Yukarıdaki örnekte ``karce_ciz``'i  yeniden yazarak kare ve dikdörtgen
  arasındaki bir bağıntıyı yakalarız.

* Bu fonksiyonu çağırırken ``kare_ciz(tamer,50)`` diyebiliriz. Bu fonsyonun
  parametreleri, ``tx`` ve ``sz`` sırasıyla tamer nesnesine ve int 50'ye
  atanmıştır.
* ``diktortgen_ciz`` fonksiyonuna çağrı yapıldığında, ``tx`` ve ``sz``
  değişkenlerindeki değerler ilk önce alınır ve sonrasında fonksiyon çağrılır. Bu fonksiyonun ``t`` değişkeni ``tamer`` nesnesine; ``w`` ve ``h`` değişkenlerinin herbiri 50 değerine atanır.


Şimdiye kadar, bu kadar yeni fonksiyon oluşturmak için katlandığımız bu kadar
zahmete değip değmeyeceği anlaşılmamış olabilir. Gerçekte, birçok neden
vardır, fakat şu örnek iki tanesini gösterir: 

#. Yeni bir fonksiyon yaratmak, komutlar grubunu isimlendirme fırsatını
   bize verir. Fonksiyon, karışık hesaplamaları saklayarak tek bir komut ile programı
   basitleştirir. Fonksiyon (ismi de dahil olmak üzere) düşünce yapımızı veya
   problemin soyutlanmasına yardım eder.

#. Yeni bir fonksiyon yaratmak, kendini tekrarlayan kodları ortadan kaldırmaya
   ve böylece kısa bir program yaratmamızı sağlar. 

Tahmin edebileceğimiz gibi, fonksiyonu çalıştırmadan önce o fonksiyonu
yaratmalıyız. Diğer bir deyişle, fonksiyon çağrılmadan önce fonksiyonunun
tanımı çalıştırılmalıdır. 

.. index:: yürütme akışı

Yürütme akışı
-------------

Fonksiyonun ilk kullanımından önce tanımlandığından emin olmak için,
cümlelerin yürütme sırasını bilmek gerekir. Bu sıraya **yürütme akışı (flow of
execution)** denir. Daha önceki bölümde bunun hakkında biraz konuşmuştuk.

Yürütme her zaman programın ilk satırıyla başlar. Cümleler yukarıdan aşağıya
olmak üzere her seferinde bir kere çalıştırılır.

Fonksiyon tanımlamaları, programın yürütme akışını değiştirmez, ancak
fonksiyon içindeki cümlelerin fonksiyon çağrılana kadar yürütülmediğini
unutmayın. Pek yaygın olmasa bile, bir fonksiyonu diğer bir fonksiyon içinde
tanımlıyabiliriz. Bu durumda içerideki fonksiyon tanımı, içerisinde
tanımlandığı fonksiyon çağrılana kadar yürütülmeyecektir. 

Fonksiyon tanımlamaları, yürütme akışındaki sapmalar gibidir. Sonraki cümleye
gideceğine, akış çağrılan fonksiyonun ilk satırına gider, fonksiyon içindeki
cümleleri çalıştırır ve daha sonra bıraktığı yerden (fonksiyonun çağrıldığı
satır) devam eder. 

Bu kolay gibi gözükse de, bir fonksiyonun bir başka fonksiyonu çağırabildiğini
bildiğimizden dolayı dikkatli olmalıyız. Bir fonksiyonun ortasında, program
bir başka fonksiyonunun içindeki cümleleri çalıştırmak zorunda kalabilir. Bu
yeni fonksiyon çalışırken, başka bir fonksiyonu  da çalıştırabilir!

Şansımız var ki, Python nerde kaldığını tutmada oldukça beceriklidir. Böylece
fonksiyonun yürütülmesi bittiğinde, program çağırdığı fonksiyon satırına geri
döner. Programın sonuna geldiğinde, programı sonlandırır. 

Bu sefil hikayenin anafikri nedir? Programı okurken  yukarıdan
aşağıya doğru okumayın. Bunun yerine, yürütme akışını takip edin. 

.. index:: PyScripter; tek adımlama

.. admonition:: Yürütme akışını canlı olarak izle

   Pyscripter'in ``single-stepping`` (tek adımlama) özelliğini kullanarak
   yürütme akışını adım adım izliyebiliriz. Kodun herbir satırı
   çalıştırılmadan önce Pyscripter tarafından vurgulanır (ışıklandırılır.)

   Pyscripter'de fareyi programdaki herhangi bir değişkenin üzerine getirerek, o
   değişkenin o andaki değerini görebilirsiniz. Böylece programın anlık durumunu  ---
   o anda değişkenlere atanan değerler --- kontrol etmemiz kolaylaşır. 

   Bu, herbir adımda tam  ve derinlemisine  ne olduğunu anlamak için oldukça
   kuvvetli bir mekanizmadır. Tek adımlama özelliğini iyi kullanmayı ve zihinsel
   olarak her zaman ileriyi görmeyi öğrenin. Kod üzerinden çalışırken, herbir adımdan
   önce kendinizi sınayın: *"Bu satırın programdaki değişkenler üzerindeki etkisi ne
   olacak?"* ve *"yürütme akışı bir sonraki adımda nereye gidecek?"*

   Geriye gidelim ve 15 tane çeşitli renklerde kare çizen programda bunun nasıl
   çalıştığını görelim. İlk olarak, ``import`` deyiminin altına bir satır
   ekleyeceğiz. Bu gerekli olmasa bile  hayatımızı oldukça kolaylaştıracak, çünkü
   `turtle` kodunu içeren modül içine adım atmamazı (girmemizi) önleyecek. 

 
       .. sourcecode:: python3

           import turtle
           __import__("turtle").__traceable__ = False
    
   Şimdi başlamaya hazırsınız. Farenizin imlecini (işaretçisini) kamplumbağa ekranı
   yaratacağımız satırın üstüne yerleştirin ( wn = turtle.Screen() )  ve *F4* tuşuna
   basın. Bu Python programınızı bu satıra kadar ( imlecin bulunduğu satır dahil
   değil) çalıştıracak. Programımız çalışmaya ara verecek ve çalıştırılacak sonraki
   satırı ışıklandıracaktır. Şu şekil gibi olacaktır:
    
   .. image:: illustrations/breakpoint.png

   Bu noktada, *F7* düğmesine arka arkaya basarak kod üzerinden adım adım gideriz.
   10,11,12, ... satırların nasıl bir kamplumbağa penceresi yarattığı, kanvas
   rengininin nasıl değiştiğini, başlığın nasıl değiştiği ve yürütme akışının nasıl
   döngü içine ve burdan da fonksiyona girdiğini gözlersiniz. 

   Biz bunu yaparken, faremizi bazı değişkenler üzerinde gezdirerek, bizim kafamızda
   yarattığımız model ile uyuşup uyuşmadığını onaylarız. 

   Birkaç döngü sonrası, programımız 20'inci satırı çalıştırmaya hazır olur ve
   sıkılmaya başladığımızda, *F8* düğmesini kullanarak çağırdığımız fonksiyonu
   atlarız. Bu, fonksiyon içindeki her komut üzerinden adım adım gitmemiz yerine,
   bütün bir fonksiyonu bir kerede çalıştırmamızı sağlar. Fonksiyon üzerinden
   "detaylı olarak" gidebiliriz veya fonksiyonu tek bir parça gibi çalıştırabiliriz. 

   Daha farklı seçenekler vardır; bunlardan birtanesi de çalışmayı durdaran (ara
   veren) *Resume* düğmesidir. Bunu PyScripter'in *Run* sekmesi altında
   bulabilirsiniz. 

.. index::
    single: parametre
    single: fonksiyon; parametre
    single: argüment
    single: fonksiyon; argüment
    single: import komutu
    single: kompozisyon
    single: fonksiyon; kompozisyon

Bir değer döndüren fonksiyonlar
-------------------------------

Daha önceki kısımdaki bütün fonksiyonlar değer döndürür. Ayrıca ``range``, ``int``
ve ``abs`` gibi fonksiyonlarının döndürdüğü değerler, daha karmaşık ifadeler yaratmak
için kullanılabilir. 

``kare_ciz`` fonksiyonu ile yukarıdaki fonksiyonlar arasındaki fark, ``kare_ciz``
fonksiyonu bir değer döndürmez çünkü onun bir değeri hesaplamasını istemedik. Tam
aksine, ``kare_ciz`` fonksiyonunun, kamplumbağının çizim yapmasını sağlayan bir dizi
adımı gerçekleştirmesini istedik.

Bu kitapta değer döndüren fonksiyonları **ürün veren** fonksiyonlar olarak
isimlendireceğiz. **ürün veren** fonksiyonun karşıtını ise **void fonksiyon** (ürün
vermeyen)  adını
vereceğiz. Bu tür fonksiyonlar, bir değer etmek için çalıştırılmaz fakat yararlı
şeyler yaptıkları için çalıştırılır ( Java, C#, C ve C++ programlama dilleri ürün
vermeyen bir fonksiyonu tanımlarken için "void function" terimi kullanılır.) Void
fonksiyonlar dönüş değerleri için çalıştırılmasa bile, Python her zaman birşey
döndürmek ister. Eğer programcı fonksiyona bir değer döndürmezse, Pyton otomatik
olarak dönüş değerine ``None`` (hiçbir şey) atar. 

Ürün veren bir fonksiyonu nasıl yazarız? İkinci bölümün sonunda bileşik hesap faizi
yapan formülü görmüştük; bunu şimdi ürün veren bir fonksiyon olarak yazacağız: 

    .. image:: illustrations/compoundInterest.png

    .. sourcecode:: python3
       :linenos: 

       def son_miktar(p, r, n, t):
           """
             Bileşik fazi formülünün p'ye uygularayak
             son miktarı hesapla
           """

 
           a = p * (1 + r/n) ** (n*t)
           return a         # Bunu yeni görüyoruz; fonksiyonu ürün veren hale getirir. 
                     
       # Yukarıdaki fonksiyonu 
       ilkYatirim = float(input("Ne kadar para yatırmak istiyorsunuz?"))
       sonMiktar = son_miktar(ilkYatirim, 0.08, 12, 5)
       print("Paranazın son miktarı ", sonMiktar)

* **return** deyimini bir ifade takip eder ( Bu durumda ``a``.) Bu ifade
  hesaplancak ve bu fonksiyonu çağıran fonksiyona bir ürün olarak
  döndürülecektir. ``ilkYatirim``'in tipi bir karakter dizidir, fakat bunu bir
  sayıya çevirmemiz gereklidir. O bir para olduğundan ve ondalıklı kısma sahip
  olduğundan dolayı, ``float`` tip değişkenini kullanarak onu float tipine
  çevirdik. 
* Argümanları fonksiyonlara nasıl girdiğimize dikkat edin. Argümanlarımız:
  yıllık %8 faiz oranı, elde edilen faiz her ay (yılda 12 kere)  hesabımıza ekleniyor ve hesap 5
  yıl boyunca (dönem) açık tutuluyor. 

* Biz bu programı fonksiyonu çalıştırdığımızda, aşağıdaki çıktıyı alırız: 

      *Paranızın son miktarı dönem sonunda 14898.457083*

  Ondalıklı haneler kısmı biraz uzun gibi gözüküyor. Fakat unutmayın ki, Python
  bizim para ile çalışıp çalışmadığımızı anlamaz. Python'un tek yaptığı, kendi
  imkanları içinde en iyi sayıyı yuvarlamadan en iyi sonucu vermektir. İleride
  bu çıktıyı nasıl biçimlendireceğimiz ve bunu iki basamaklı ondalık sayıya
  yuvarlayacağımızı göreceğiz.

* ``ilkYatirim = float(input("Ne kadar para yatırmak istiyorsunuz?"))`` satırı
  kompozisyon özelliğinin bir başka örneğidir. Burda bir kaç fonksiyonu birden
  kompozisyon ( tek satırda birleştirme) yapıyoruz. Yani, ``input``
  fonksiyonunun çıktısı, ``float`` fonksiyonun bir argümanı oluyor. 

Burda bir şeye dikkat edin. ``sonMiktar`` fonksiyonuna argüman olarak girdiğimiz
``ilkYatirim`, ``p`` değişkeni ile herhangi bir ilgisi yoktur. Bu sanki
``sonMiktar`` çağırıldığı zaman,  ``p=ilkYatirim`` çalıştırılır. Burda
``final_amt``'yi çağıran ``p``'dir.

Kısa isimli değişkenler bazen yanıltıcı olabilir. Bu yüzden aşağıdaki sürümü
tercih etmik uygun olabilir:

    .. sourcecode:: python3
       :linenos:
     
       def son_miktar_v2(anapara, faizOrani,faizinAnaParayaEklenmeSayisi, yilSayisi):
           a = anapara * (1 + faizOrani / faizinAnaParayaEklenmeSayisi) ** (faizTekrar*years)
           " Burda faizinAnaParayaYıldaEklenmeSayisi,  edilen faizin  yılda kaç kere  anaparaya
           eklenme sayısıdır. 

           return a
           
       def son_miktar_v3(anapara, oran, faizTekrari,yil):
           a = anapara * (1 + oran/faizTekrari) ** (faizTekrari*yil)
           return a                  

Yukarıdakilerin hepsi aynı şeyi yapar. Sağduyunuzu kullanarak  başka kişiler tarafından anlaşılabilecek bir program yazmayı amaç edinin. Kısa değişken isimleri kodu daha ekonomik yapar  ve bazen kodun okunmasını kolaylaştırır. Eğer Einstein :math:`E=mc^2` (m:kütle, c:ı,ışık hızı) formülünde daha uzun değişken isimleri kullansaydı, bu kadar rahat akılda kalmayabilirdi. Eğer kısa isimleri kullanmayı tercih ederseniz, kısa isimlerin ne için kullanıldığını  açıklayan kısa yorumlar ekleyin. 

.. index::
    single: yerel değişken 
    single: değişken; yerel
    single: yaşam süresi

Değişkenler ve parametreler yereldir
------------------------------------

Bir fonksiyon içerisinde bir **yerel değişken** yarattığımızda, o değişken
sadece o fonksiyon icinde varolur. Bu değişkeni o fonksiyonun dışında
kullanamazsınız. Örneğin:

    .. sourcecode:: python3
       :linenos: 

       def son_miktar(p, r, n, t):
           a = p * (1 + r/n) ** (n*t)
           return a           
 
Eğer ``a`` değişkenini bu fonksiyonunun dışında kullanmaya çalışırsak, aşağıdaki
hatayı alırız:

    .. sourcecode:: python3
        
        >>> a
        NameError: name 'a' is not defined

``a`` yalnızca fonksiyon çalıştırıldığı sürece varolabilir. Biz buna, ``a``'nın
**yaşam süresi** diyeceğiz. Fonksiyonun çalışması sonlandığında, yerel
değişkenler ( fonksiyonun içindeki değişkenler) yokedilir. 

Parametreler de yereldir ve yerel değişkenler gibi davranır. Örneğin,
``p``,``r``, ``n``, ``t``'nin yaşam süreleri, ``son_miktar`` fonksiyonu
çağrıldığında başlar ve fonksiyonun çalışması durduğunda bu değişkenler
yokedilir. 

Bu yüzden bir fonksiyon içinde bir yerel değişkene değer atayıp, fonksiyon
çalışmasını tamamladıktan sonra bu değişkeni başka bir zaman tekrar kullanmak mümkün
değildir. Fonksiyonunun her çağrılmasında yeni bir yerel değişken yaratır ve
fonksiyonları çalışması sona erdiğinde, yerel değişkenlerinde ömrü sonra erer. 

.. index:: kodu yeniden düzenleme, kodu parçalamak

Kamplumbağa programına yeniden bakalım
--------------------------------------

Şimdiye kadar ürün veren fonksiyonları gördük. Dikkatimizi kodumuzun yeniden
düzenlemesine odaklarsak, program parçacıkları aklımıza daha iyi yatar. Bu
yeniden düzenleme işlemine **refactoring** ( yeniden faktörleme) denir. 

Kamplumbağalar ile çalışırken her zaman yapmak istediğimiz iki şey vardır:
Kamplumbağalar için pencere oluşturmak; ve bir veya birdan fazla kamplumbağayı
ekranda yaratmak. Bu işlemleri ileride daha kolay yapabilmek için bazı
fonksiyonlar yazabiliriz.

    .. sourcecode:: python3
       :linenos: 

       def pencere_yap(renk,baslik):   
           """
             İsmi ve başlığı olan bir pencere oluşturalım ve bu pencereyi
             fonksiyon içinde döndürelim. 
           """
           w = turtle.Screen()             
           w.bgcolor(renk)
           w.title(baslik)
           return w

       def kamplumbag_yap(renk,olcu):      
           """
             Rengi ve kalem ölçüsü olan olan bir kamplumbağa yaratalım.
           """
           t = turtle.Turtle()
           t.color(renk)
           t.pensize(olcu)
           return t

           
       wn = pencere_yap("lightgreen", "Ahmet Tamer ve Deniz Dans Ediyor")
       tamer = kamplumbag_yap("hotpink", 5)
       ahmet = kamplumbag_yap("black", 1)
       deniz = kamplumbag_yap("yellow", 2)  

Bir kodu yeniden düzenlememizin amacı, bir fonksiyonu çağırdığımızda hangi
şeyleri değiştirmek istiyebileceğimizi tahmin etmektir. Bunlar yazdığımız
fonksiyonun 
parametreleri ve değiştirelibecek kısımları  olmalıdır.

Sözlük
------

   .. glossary::
    
       argüman
           Bir forksiyon çağrıldığında, bu fonksiyona aktarılan değerdir. Bu değer
           fonksiyonda ilgili parametreye atanır. Bu argüman bir işlemin değerini
           alabilir  veya ürün
           veren bir fonsiyonu çağırabilir. 

       gövde
           Bir birleşik ifadenin ikinci kısmı. Gövdedeki bütün cümleler başlıktan
           itibaren aynı miktarda içeriye doğru girintilidir. Python kullanıcıları
           genelde 4 boşluklu içeriye girinti kullanırlar.

       bileşik deyim
           Bu deyim iki parçadan oluşur:

           A. başlık (header) - bir deyimin tipini belirleyen anahtar kelime
              başlar ve iki nokta üst üste ile biter.
           B. gövde- başlıktan itibaren aynı miktarda içeriye doğru girintilenmiş
              ifadeler
               
           Bir bileşik deyim şu şekilde oluşur:

               .. sourcecode:: python3

               keyword ... :
                   deyim
                   deyim ...

       docstring
               Bir fonksiyona ait olan ve onu belgelendirmede kullanılan bir
               özelliktir. Pyscripter gibi araçlar, docstringleri kullanarak
               programcılara ipucu ve kolaylık sağlar.  Module, sınıf ve yöntemleri 
               ilerideki bölümlerde
               gördüğümüzde, docstring'lerin bunlarda da kullanıldığını göreceğiz. 

       çerçeve
           Yığıt (stack) diyagramında bir fonksiyon çağrısını temsil eden
           çerçevedir. Bir fonksiyonunun yerel değişkenlerini ve
           parametrelerini içerir. 

       fonksiyon
           Bazı yararlı işlemler gerçekleştiren deyimler dizisinin
           isimlendirilmiş halidir. Fonksiyonlar parametre alıp almayacakları
           gibi, bir fonksiyon bir sonuç üretebilir ya da üretemeyebilir.

       fonksiyon çağrıcı
           Fonksiyonu çalıştıran deyim. Bu deyim fonksiyonun ismi, bu ismi
           izleyen iki parantezin arasına yerleştirilmiş argüman listesinden
           oluşur.

       fonksiyon tanımı
           Yeni bir fonksiyon yaratan; ismini, parametrelerini ve fonksiyon
           gövdesindeki cümleleri belirten bir deyim. 

       Ürün veren fonksiyon
           Bir fonksiyon çağrıldığında bir değer döndüren fonksiyon

       Başlık satırı
           Gruplandırılmış deyimlerin başlangıç kısmı. Başlangıç satırı bir
           anahtar kelime ile başlar ve iki nokta üst üste (:) ile biter.

       import deyimi
           Bir Python modülü içinde tanımlanmış fonksiyonları ve değişkenleri,
           başka bir betiğin içine getirilmesi için kullanılan deyimdir. 

       yaşam ömrü
           Değişkenlerin ve nesnelerin bir yaşam ömrü vardır. Programın
           çalışması esnasında bir noktada yaratılır ve bir süre sonra ise
           yokedilirler. 

       yerel değişken
           Bir fonksiyon içinde tanımlı değişkenlerdir. Yerel değişken sadece
           kendi fonksiyonu içerisinde kullanabilir. Bir fonksiyonun
           parametreleri de yerel değişkenlerin özel bir türüdür.
        
       parametre
           Bir fonksiyon içinde kullanılan ve fonksiyon içinde kullanılan
           argümanlara işaret eden isim. 

       refactor (yeniden yapılandırma)
           Bir programı genelde daha anlaşılır yapmak için programın yeniden
           düzenlemesine verilen isim. Çalışan bir programa sahip iken, o
           programa gidip yeniden düzenlemektir. Genelde bu işlem, daha iyi
           değişken isimleri seçmek, kendini tekrar eden kalıpları bulmak ve
           bunları fonksiyon içine yerleştirmektir.

       stack (yığıt) diyagramı
           Fonksiyonların, fonksiyon değişkenlerinin ve bu değişkenlerin
           gösterdiği değerlerini gösteren  diyagramı

       traceback (geri izleme) 
           Bir çalışma hatası oluştuğunda o anda çalıştırılan fonksiyonların
           listesidir. Geri izleme ayrıca yığıt izleme olarak da adlandırılır.
           `Çalışma zamanı yiğit diyagramında (Runtime Stack)
           <http://en.wikipedia.org/wiki/Runtime_stack>`__ saklandıkları sıraya
           göre bu fonksiyonlar bulunurlar. 

       void fonksiyonu
           Ürün veren bir fonksiyonun karşıtıdır. Yani bir değer döndürmez.
           Bir değer döndürmek yerine, yapması gereken bir işi çalıştırır. 

Alıştırmalar
------------

#. Kare çizen bir void fonksiyon yazınız. Programınızı, aşağıdaki kareyi çizmek
   için kullanınız. Her kenarın 20 birim uzunluğunda olduğunu kabul edin.
   (İpucu: Program sonlandırıldığında, kamplumbağa en son karenin bitiş
   noktasından uzaklaşmıştır. )

       .. image:: illustrations/five_squares.png
           
#. Aşağıdaki şekli çizen bir program yazınız. En içteki karenin 20 birimlik bir
   kenarı olduğunu varsayın ve her ardışık karenin kenarının  kendisinden önce gelen
   kare kenarından 20 birim daha büyük olduğunu varsayın. 

       .. image:: illustrations/nested_squares.png


#. Kamplumbağaya düzgün çokgen çizdiren bir fonksiyon ``cokgen_ciz(t, n, sz)``
   yazınız. Fonksiyon ``cokgen_ciz(tamer, 8, 50)`` olarak çağrıldığında şu şekli
   vermelidir: 

       .. image:: illustrations/regularpolygon.png

#. Bu güzel şekli çizin:

       .. image:: illustrations/tess08.png

#. Aşağıdaki iki spiral birbirinden dönme açısıyla birbirinden farklıdır.
   İkisini de çiziniz:

        .. image:: illustrations/tess_spirals.png 
            :height: 240

#. Daha önceki sorudaki ``cokgen_ciz`` fonksiyonunu çağıran ve bir eşkanar üçgen
   çizen ``eskenar_ciz(t, sz)``  bir void fonksiyon yazınız. 

#. 1'den ``n``'e kadar (n dahil) sayıların toplamını yapan bir ürün (sonuç)
   veren bir fonksiyon yazınız. Örneğin ``toplam(10)`` yazdığınızda, `1+2+3...
   +10` sonucunu 55 olarak döndürsün. 

#. Yarıçapı ``r`` olan bir çemberin alanını hesaplayan ``cember_alan(r)`` bir
   fonksiyon yazınız.

#. Her bir kenarı 100 birim olan bir void fonksiyonu yazınız (İpucu: Her noktada
   kamplumbağayı 144 derece döndürmeniz gerekir.)

         .. image:: illustrations/star.png

#. Yukarıdaki programı genişletin. Beş tane yıldız çizin.  Herbir yıldızdan sonra; kalemi yukarı
   kaldırın ( kalemi etkisizleştirin), kalemi 144  derece sağa döndürün ve 350 birim
   ileri götürün, kalemi aşağıya koyun, yeniden bir yıldız çizin. Şekliniz
   aşağıdaki gibi olsun: 

        .. image:: illustrations/five_stars.png

   Eğer kalemi kaldırmasaydınız, şekliniz nasıl olurdu. 








 
           
 


 


