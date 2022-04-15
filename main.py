import sqlite3

con = sqlite3.connect("market.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE if not exists ürünler(marka TEXT, ürün TEXT, fiyat INT , stok INT , litrekilogram INT)")


def ürün_ekle():
    marka = input('Ürünün markası :')
    ürün = input('Ürün :')
    ürün_fiyatı = input('Ürün fiyatı :')
    ürün_stok = input('Ürün stoğu :')
    litre_kilogram = input('Ürünün litresi/kilogramı :')
    cursor.execute("INSERT INTO ürünler VALUES(?,?,?,?,?)", (marka, ürün, ürün_fiyatı, ürün_stok, litre_kilogram))
    con.commit()


def ürün_sil():
    silinecek_marka = input('Silinecek ürünün markası,ürün,kg :')
    silinecek = silinecek_marka.split(',')
    silinecek = tuple(silinecek)
    cursor.execute("DELETE from ürünler where (marka , ürün, litrekilogram )=(?,?,?)", silinecek)
    con.commit()


def ürünleri_goster():
    okuma = cursor.execute("SELECT * FROM ürünler")
    for i in okuma.fetchall():
        print(f"""
ürün markası : {i[0]}
ürün : {i[1]} 
ürün fiyatı : {i[2]}
ürün stoğu : {i[3]}
ürün kilogram/litresi : {i[4]} 
""")


def marka_ürünleri_goster():
    gösterilecek_marka = input('Hangi markanın ürünlerini istiyorsunuz? :')
    okuma1 = cursor.execute("SELECT * FROM ürünler where marka =?", (gösterilecek_marka,))
    for i in okuma1.fetchall():
        print(f"""
ürün markası : {i[0]}
ürün : {i[1]} 
ürün fiyatı : {i[2]}
ürün stoğu : {i[3]}
ürün kilogram/litresi : {i[4]} 
""")


def ürün_adıyla_ürünleri_goster():
    gösterilecek_ürün = input('Hangi ürünün çeşitlerini görmek istiyorsunuz? :')
    okuma1 = cursor.execute("SELECT * FROM ürünler where ürün =?", (gösterilecek_ürün,))
    for i in okuma1.fetchall():
        print(f"""
ürün markası : {i[0]}
ürün : {i[1]} 
ürün fiyatı : {i[2]}
ürün stoğu : {i[3]}
ürün kilogram/litresi : {i[4]} 
""")


def fiyat_güncelle():
    fiyat_değiştiriliyor = input('Fiyatı değiştirilecek ürün,markası :')
    fiyat_değiştirilecek = []
    for i in fiyat_değiştiriliyor.split(','):
        fiyat_değiştirilecek.append(i)
    yeni_fiyat = input('Ürünün yeni fiyatı :')

    güncelleme = cursor.execute("UPDATE ürünler set fiyat=? where (ürün,marka) = (?,?) ",
                                (yeni_fiyat, fiyat_değiştirilecek[0], fiyat_değiştirilecek[1]))
    con.commit()


def stok_güncelle():
    stok_güncelleniyor = input('Stok güncellenecek ürün,markası :')
    stok_güncellenecek = []
    for i in stok_güncelleniyor.split(','):
        stok_güncellenecek.append(i)
    yeni_stok = input('Ürünün yeni stoğu :')

    güncelleme = cursor.execute("UPDATE ürünler set stok=? where (ürün,marka) = (?,?) ",
                                (yeni_stok, stok_güncellenecek[0], stok_güncellenecek[1]))
    con.commit()


while True:
    print("""---------İŞLEM MENÜSÜ----------
    
    1.ürün ekle
    2.ürün sil
    3.Ürünleri göster
    4.Fiyat güncelle
    5.Stok güncelle
    6.Programı sonlandır
    
    
    """)
    işlem = int(input('İşlemi seçiniz :'))
    if işlem == 1:
        ürün_ekle()
    if işlem == 2:
        ürün_sil()
    if işlem == 3:
        print("""
        1.Tüm ürünleri göster
        2.Ürün çeşidine göre ürünleri göster
        3.Markaya göre ürünleri göster""")
        a = int(input('işlemi seçin :'))
        if a == 1:
            ürünleri_goster()
        if a == 2:
            ürün_adıyla_ürünleri_goster()
        if a == 3:
            marka_ürünleri_goster()
    if işlem == 4:
        fiyat_güncelle()
    if işlem == 5:
        stok_güncelle()
    if işlem == 6:
        con.close()
        break
