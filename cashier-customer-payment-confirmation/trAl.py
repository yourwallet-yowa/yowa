cuzdanAdresi = "0xea0a6e3c511bbd10f4519ece37dc24887e11b55d"

from selenium import webdriver
import time
import veritabanıOlustur
import cv2


browser = webdriver.Firefox(executable_path='geckodriver.exe')

def kontrolEt(yazi,miktar):

    parcala = str(yazi).split(" ")
    if (len(parcala) == 15):
        #print("kontrol",float(str(istenenDeger).strip()),float(str(parcala[12]).strip()))
        if (float(parcala[12]) == float(miktar)):
            gelenSonuc = veritabanıOlustur.veriOku(str(parcala[0]))

            if(gelenSonuc == "yeni"):

                browser.get("https://bscscan.com/tx/"+str(parcala[0]))
                time.sleep(1)

                def sonDurumuAl():

                    sonDurum = browser.find_element_by_xpath(
                        "/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div/div[2]/div[2]/span").text
                    if (sonDurum == "Success"):
                        print("success")
                        veritabanıOlustur.veriEkle(str(parcala[0]), str(parcala[12]))

                        img = cv2.imread('tick.png')

                        cv2.imshow('YOWA', img)

                        cv2.waitKey(5000)  # waits until a key is pressed
                        cv2.destroyAllWindows()  # destroys the window showing image

                        # img = Image.open('tick.png')
                        # img.show()
                        # time.sleep(2)
                        # img.close()
                    if (sonDurum == "Pending"):
                        print("pending")
                        time.sleep(3)
                        sonDurumuAl()

                sonDurumuAl()

            if (gelenSonuc == "eski"):
                print("it is already added, it is not new")

            #veritabanıOlustur.veriEkle(str(parcala[0]),str(parcala[12]))
            #print("oldu")
        #print(str(parcala[0])+":"+str(parcala[12]))

def odemeyiKontrolEt(miktar):


    browser.get("https://bscscan.com/address/"+str(cuzdanAdresi))  # example :: url = https://www.google.com
    time.sleep(1)
    q = browser.find_elements_by_tag_name("tr")

    for a in q:
        try:
            w = a.text
            kontrolEt(str(w),miktar)
        except Exception as e:
            pass
            #print("hata:",e)

odemeyiKontrolEt("0.110822578443882")