import requests
from bs4 import BeautifulSoup
import time

"""""""""
BeautifulSoup kütühanesi kullanarak arabam.com sitesinden görsel indir
"""""""""
a=1
for a in range(2):
    istek_yapılacak_sayfa="https://www.arabam.com/ikinci-el/otomobil?page="   ##Veri çekmek istediğin sayfa

    r=requests.get(istek_yapılacak_sayfa+str(a)+"") #a sayfayı belirtir a=1 1.Sayfa
    soup=BeautifulSoup(r.content,"lxml")

    st1=soup.find("div",attrs={"class":"flex1 pr"})
    st2=st1.find("table",attrs={"class":"table listing-table w100 border-grey2"})
    st3=st2.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})


    for detaylar in st3:
            link_sonu=detaylar.a.get("href")
            link_basi="https://www.arabam.com"
            link=link_basi+link_sonu          #Linkleri birleştir ve istek yap
            r1=requests.get(link)
            soup1=BeautifulSoup(r1.content,"lxml")
            st4=soup1.find("div",attrs={"class":"container detail-v2-identifier bg-grey2018 mt10"})
            st5=st4.find("a",attrs={"class":"slick-wrapper"})

            try:
                name = st5.img.get('alt')    #araç isimleri
                foto = st5.img.get('src')    #fotoğraf linki
            except:
                pass

            print(foto)

            #Görselleri indir
            try:
                with open(name.replace(' ', '-').replace('/','').replace('\n','').replace(';','').replace(':','')+ '.jpg', 'wb') as f:
                         im = requests.get(foto)
                         f.write(im.content)
            except:
                pass

    time.sleep(20)


a=a+1







