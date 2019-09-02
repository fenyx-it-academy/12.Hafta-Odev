# 12.Hafta-Odev
Tasit isimli bir sinif tanimlayiniz. Bu sinif icerisinde sinif ozelligi (class method) olarak tasit_miktari isimli bir bos liste tanimlayiniz.  Bu tasit sinifinin motor_gucu, koltuk_sayisi, km_durumu, modeli, satis_yili gibi obje ozellikleri(instance attributes) olsun. Ve her orneklenme durumunda bu ozellikler parametre olarak verilsin. Ayrica her ornekte degismeyecek sekilde; tekerlek sayisi isimli bir ornek niteligi tanimlayin ve degeri 4 olsun. 
Ayrica bu objenin  su methodlari olmalidir:

    1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali  
    2.modelini goster (tasitin modelini ekrana yazdirmali)
    3. km_durumunu al (tasitin kilometre durumunu return etmeli) 
    4. tasit miktarini_guncelle. Sinif her orneklendiginde tasit miktarini 1 artirmali.

    - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
    - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
  
Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi, Tasit sinifindan miras aliniz. Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve max_hiz isimli bir ornek niteligi tanimlayiniz ve bu nitelik her orneklenme durumunda parametre olarak verilsin.
Bu sinifta su methodlari tanimlayiniz;

    1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
    2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
    3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
    4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise 
    “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan 
    miras alinmamistir.’ seklinde yazsin)
Ayrica bu Araba sinifinda; modelini goster isimli Tasit sinifina ait methodu override ediniz ve ‘Araba sinifinin methodu….’ seklinde ekrana cikti veriniz ve modeli yazdiriniz.
