import string

#Girilen metinden noktalama isaretlerini silen fonksiyon.Arguman olarak metin gonderiliyor
def noktalama_isaretleri_sil(metin):
    yeni_metin = ""
    for kelime in metin:  #metnin karakterlerinden noktalama isaretleri cikartilarak yeni metine ekleniyor
        if kelime not in string.punctuation:
            yeni_metin += kelime
    return yeni_metin


#Metni kucuk harflerle yazdiran fonksiyon,gereksiz kelimeler kucuk harflerle oldugundan once bu fonksiyonu tanimladim,
# arguman olarak noktalama isaretleri silinmis metin gonderiliyor
def metni_kucultme(yeni_metin):

    #turkcede I ve İ farkli oldugundan kucultmeden once onlari kucuk i ve ı ile degistirdim
    yeni_metin = yeni_metin.replace('I','ı')
    yeni_metin = yeni_metin.replace('İ','i')

    kucuk_metin = yeni_metin.lower() #tum metnin kucultulmesi

    return kucuk_metin


#Metinden stop words'leri cikartan fonksiyon,arguman olarak noktalama isaretleri silinmis ve karakterleri kucultulmus metin gonderiliyor
def gereksiz_kelimeleri_cikar(kucuk_metin):
    gereksiz_kelime = 'acaba altı altmış altmýþ altý ama ancak arada aslında ayrıca bana bazı bazý belki ben benden beni benim beri beş beþ bile bin bir birçok biri birkaç birkez birşey birşeyi birþey birþeyi biz bizden bize bizi bizim böyle böylece bu buna bunda bundan bunlar bunları bunların bunu bunun burada çok çünkü da daha dahi de defa değil diğer diye	doksan dokuz dolayı dolayısıyla dört edecek eden ederek edilecek ediliyor edilmesi ediyor eğer elli en etmesi etti ettiği ettiğini gibi göre halen hangi hatta hem henüz hep hepsi her herhangi herkesin hiç hiçbir için iki ile ilgili INSERmi ise işte itibaren itibariyle kadar karşın katrilyon kendi kendilerine kendini kendisi kendisine kendisini kez ki kim kimden kime kimi kimse kırk kýrk mı milyar milyon mu mü mý nasıl nasýl ne neden nedenle nerde nerede nereye niçin niye o olan olarak oldu olduğu olduğunu olduklarını olmadı olmadığı olmak olması olmayan olmaz olsa olsun olup olur olursa oluyor on ona ondan onlar onlardan onlari onları onların onlarýn onu onun otuz öyle oysa pek rağmen sadece sanki sekiz seksen sen senden seni senin şey şeyden şeyi şeyler siz sizden sizi sizin şöyle şu şuna şunda şundan şunları şunu tarafından þey þeyden þeyi þeyler þu þuna þunda þundan þunu trilyon tüm üç üzere var vardı ve veya ya yani yapacak yapılan yapılması yapıyor yapmak yaptı yaptığı yaptığını yaptıkları yedi yerine yetmiş yetmiþ yine yirmi yoksa yüz zaten'
    gereksiz_kelime_liste = gereksiz_kelime.split() #gereksiz kelime stringini listeye donusturuyor
    noktalama_isaretsiz_metin = kucuk_metin.split() #metni listeye donusturuye
    metnin_son_hali = ''

    #Metnin gereksiz kelime listesinde olmayan kelimelerini toplayarak metnin son halini elde ediyor
    for index in range (len(noktalama_isaretsiz_metin)):
        if noktalama_isaretsiz_metin[index] not in gereksiz_kelime_liste:
            metnin_son_hali = metnin_son_hali + noktalama_isaretsiz_metin[index] + ' '

    return metnin_son_hali


#metinde kullanilan her kelimenin sayini bulan fonksiyon. Arguman olarak noktalama isaretleri ve
# gereksiz kelimelerden temizlenmis ve karakterleri kucultulmus metin gonderiliyor
def tekrar_kelime_say_bul(kucuk_harfli_metin):
    print('Kelime',(' ')*100,'Tekrar Say')
    print(('-')*100,'      ',('-')*10)
    tekrar_soz_say = {} #tekrarlanan sozu ve tekrar sayisini kendinde bulunduran dic
    for soz in kucuk_harfli_metin:
        tekrar_soz_say[soz] = tekrar_soz_say.get(soz, 0) + 1
    for soz in tekrar_soz_say:
        print(soz, (' ') * (115 - len(soz)), tekrar_soz_say[soz])


#Ayni uzunlukta olan kelime sayini ve uzunlugunu bulan fonksiyon. Arguman olarak tum gereksiz
# ifadelerden temizlenmis ve karakterleri kucultulmus metin gonderiliyor
def kelime_uzunluk_bul(kucuk_harfli_metin):
    print('Uzunluk             Kelime Say')
    print('-------             ----------')
    kelime_uzunluk = {}
    harf_sayi =[]
    for soz in kucuk_harfli_metin:
        kelime_uzunluk[len(soz)] = kelime_uzunluk.get(len(soz), 0) + 1
    for soz in kelime_uzunluk:
        harf_sayi.append(soz)   #kelime uzunlugu sirali sekilde buyukden kucuge gozuksun diye
    harf_sayi.sort()            #listeye yerlestirilib sort methodu ile duzenleniyor
    for uzunluk in range (len(harf_sayi)):
        print(format(harf_sayi[uzunluk],'7d'),format(kelime_uzunluk[harf_sayi[uzunluk]],'22d'))


#fonksiyonlar main fonksiyonu icinde cagriliyor
def main():
    metin = input('Türkçe bir metin giriniz:\n')
    yeni_metin = noktalama_isaretleri_sil(metin)
    print('\nNoktalama işaretleri ve gereksiz kelimeler çıkarıldıktan sonra küçük harflerle kalan metin:\n')
    kucuk_metin = metni_kucultme(yeni_metin)
    metnin_son_hali = gereksiz_kelimeleri_cikar(kucuk_metin)
    print(metnin_son_hali)
    kucuk_harfli_metin = metnin_son_hali.split()
    print('\nKalan metindeki kelimeler ve tekrar sayıları:\n')
    tekrar_kelime_say_bul(kucuk_harfli_metin)
    print('\nKalan metindeki her uzunluktaki kelime sayıları:\n')
    kelime_uzunluk_bul(kucuk_harfli_metin)

main()


