import sqlite3

def veriEkle(hashcode,count):

    database_connect = sqlite3.connect("veritabani.db")

    imlec = database_connect.cursor()

    imlec.execute("""CREATE TABLE IF NOT EXISTS islemler(hashcode TEXT ,count TEXT)""")

    yazi = "\""+str(hashcode)+"\","+"\""+str(count)+"\""

    imlec.execute("INSERT INTO islemler VALUES("+yazi+")")
    database_connect.commit()
    database_connect.close()

def veriOku(hashcode):

    database_connect = sqlite3.connect("veritabani.db")

    imlec = database_connect.cursor()

    imlec.execute("""CREATE TABLE IF NOT EXISTS islemler(hashcode TEXT ,count TEXT)""")

    imlec.execute("SELECT * FROM islemler WHERE hashcode = '"+str(hashcode)+"' ")
    ogrenciler = imlec.fetchall()

    deger = int (len(ogrenciler))

    database_connect.commit()
    database_connect.close()
    if ( deger == 0):
        #print("yenii")
        return "yeni"
    else:
        #print("hayirr")
        return "eski"



