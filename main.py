from tkinter.tix import Form
from selenium import webdriver
import time
import base64
import cv2
import pytesseract as pt
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from PyQt5 import QtCore, QtWidgets

dosya = open("Upkoy.txt","r",encoding="utf-8")
dizi = dosya.readlines()
dosya.close()

dosya2 = open("Anakoykoordinat.txt","r",encoding="utf-8")
dizi2 = dosya2.readlines()
dosya2.close()

dosya3 = open("multikoy.txt","r",encoding="utf-8")
dizi3 = dosya3.readlines()
dosya3.close()

class Ui_Form(object):
    def setupUi(self, form):
        Form.setObjectName("Form")
        Form.resize(120, 110)

        self.centralwidget = QtWidgets.QWidget(Form)
        self.photo = QtWidgets.QLabel(self.centralwidget)

        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(5, 5, 110, 40))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.Merkez)

        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(5, 55, 110, 40))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.Market)

        self.retranslateUi(Form)
    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Travianspeed.net Script"))
        self.pushButton1.setText(_translate("Form", "Upkoy yukseltme"))
        self.pushButton2.setText(_translate("Form", "Hammadde"))
    def Merkez(self, Form):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        for i in range(len(dizi)):
            koy = dizi[i]
            driver.get('https://travianspeed.net/ts2/logout.php')
            search = driver.find_element_by_name("user")
            search.clear()
            time.sleep(2)
            search.send_keys(koy)
            time.sleep(1)
            search2 = driver.find_element_by_name("pw")
            search2.send_keys("327866aa")

            img_base64 = driver.execute_script("""
                var ele = arguments[0];
                var cnv = document.createElement('canvas');
                cnv.width = 100; cnv.height = 40;
                cnv.getContext('2d').drawImage(ele, 0, 0);
                return cnv.toDataURL('image/jpeg').substring(22);    
                """, driver.find_element_by_xpath(
                "/html/body/div/div/div[2]/div[3]/div[2]/div/div/div/form/table/tbody/tr[3]/td[2]/img"))

            with open(r"image.jpg", 'wb') as f:
                f.write(base64.b64decode(img_base64))

            img = cv2.imread("image.jpg", 0)
            kernel = np.ones((2, 2), np.uint8)
            erosion = cv2.erode(img, kernel, iterations=1)

            kernel1 = np.ones((3, 3), np.uint8)
            opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel1)

            pt.pytesseract.tesseract_cmd = r'C:\Users\Aygün\AppData\Local\Tesseract-OCR\tesseract.exe'

            text = pt.image_to_string(opening)
            cv2.waitKey(0)

            search3 = driver.find_element_by_name("captcha")
            search3.send_keys(text)
            WebDriverWait(driver, 5)

            time.sleep(10)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/span/a")
            searchbutton.click()
            WebDriverWait(driver, 5)
            time.sleep(5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/span/a")
            searchbutton.click()
            WebDriverWait(driver, 5)
            time.sleep(5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/span/a")
            searchbutton.click()
            WebDriverWait(driver, 5)
            time.sleep(2)

            for i in range(19):
                driver.get("https://travianspeed.net/ts2/build.php?id=26")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 3]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            for i in range(3):
                driver.get("https://travianspeed.net/ts2/build.php?id=39")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 3]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=20")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[5]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(2):
                driver.get("https://travianspeed.net/ts2/build.php?id=20")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 3]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=21")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[8]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(12):
                driver.get("https://travianspeed.net/ts2/build.php?id=21")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 3]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get('https://travianspeed.net/ts2/build.php?id=32')
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[17]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(2):
                driver.get("https://travianspeed.net/ts2/build.php?id=32")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 3]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=30")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[20]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(19):
                driver.get("https://travianspeed.net/ts2/build.php?id=30")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 5]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=22")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[23]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(4):
                driver.get("https://travianspeed.net/ts2/build.php?id=22")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 5]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=23")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[23]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(2):
                driver.get("https://travianspeed.net/ts2/build.php?id=23")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 5]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=25")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[23]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(9):
                driver.get("https://travianspeed.net/ts2/build.php?id=25")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 5]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            driver.get("https://travianspeed.net/ts2/build.php?id=31")
            WebDriverWait(driver, 5)
            searchbutton = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[26]/div[3]/button")
            searchbutton.click()
            WebDriverWait(driver, 5)
            for i in range(19):
                driver.get("https://travianspeed.net/ts2/build.php?id=31")
                WebDriverWait(driver, 5)
                f = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                dakika = f[3:len(f) - 5]
                saniye = f[5:len(f)]
                zaman = (int(dakika) * 60) + int(saniye)
                searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                searchbutton.click()
                WebDriverWait(driver, 5)
                time.sleep(zaman)

            for i in range(5):
                driver.get("https://travianspeed.net/ts2/build.php?id=26")
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath("//option[@value='22']")
                searchbutton.click()
                searchbutton = driver.find_element_by_xpath("//div[@class='button-contents']")
                searchbutton.click()
                WebDriverWait(driver, 5)

            for i in range(3):
                driver.get("https://travianspeed.net/ts2/build.php?id=26")
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath("//option[@value='23']")
                searchbutton.click()
                searchbutton = driver.find_element_by_xpath("//div[@class='button-contents']")
                searchbutton.click()
                WebDriverWait(driver, 5)

            for i in range(10):
                driver.get("https://travianspeed.net/ts2/build.php?id=26")
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath("//option[@value='25']")
                searchbutton.click()
                searchbutton = driver.find_element_by_xpath("//div[@class='button-contents']")
                searchbutton.click()
                WebDriverWait(driver, 5)

            for i in range(3):
                driver.get("https://travianspeed.net/ts2/build.php?id=26")
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath("//option[@value='32']")
                searchbutton.click()
                searchbutton = driver.find_element_by_xpath("//div[@class='button-contents']")
                searchbutton.click()
                WebDriverWait(driver, 5)

            siginak = [19, 24, 28, 27, 34, 37, 35, 38, 36, 33, 29, 32]

            for i in siginak:

                driver.get("https://travianspeed.net/ts2/build.php?id=" + str(i))
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/button")
                searchbutton.click()
                WebDriverWait(driver, 5)

                for z in range(9):
                    driver.get("https://travianspeed.net/ts2/build.php?id=" + str(i))
                    WebDriverWait(driver, 5)
                    f = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                    dakika = f[3:len(f) - 5]
                    saniye = f[5:len(f)]
                    zaman = (int(dakika) * 60) + int(saniye)
                    searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                    searchbutton.click()
                    WebDriverWait(driver, 5)
                    time.sleep(zaman)


            for i in range(15):
                h = 0
                for i in range(18):
                    h = int(h) + 1
                    driver.get("https://travianspeed.net/ts2/build.php?id=" + str(h))
                    WebDriverWait(driver, 5)
                    f = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                    dakika = f[3:len(f) - 5]
                    saniye = f[5:len(f)]
                    zaman = (int(dakika) * 60) + int(saniye)
                    searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                    searchbutton.click()
                    WebDriverWait(driver, 5)
                    time.sleep(zaman)

            hammaddeboost = [22, 23, 25]

            for i in hammaddeboost:

                driver.get("https://travianspeed.net/ts2/build.php?id=" + str(i))
                WebDriverWait(driver, 5)
                searchbutton = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[29]/div[3]/button")
                searchbutton.click()
                WebDriverWait(driver, 5)

                for k in range(4):
                    driver.get("https://travianspeed.net/ts2/build.php?id=" + str(i))
                    WebDriverWait(driver, 5)
                    f = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span[6]").text
                    dakika = f[3:len(f) - 5]
                    saniye = f[5:len(f)]
                    zaman = (int(dakika) * 60) + int(saniye)
                    searchbutton = driver.find_element_by_xpath("//button[@value='Upgrade level']")
                    searchbutton.click()
                    WebDriverWait(driver, 5)
                    time.sleep(zaman)

        driver.quit()
    def Market(self, Form):

        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        while 1:
            for i in range(len(dizi3)):
                Farmtext = dizi3[i]
                xnamebox = dizi2[0]
                ynamebox = dizi2[1]

                driver.get("https://travianspeed.net/ts2/logout.php")
                WebDriverWait(driver, 5)

                search_input = driver.find_element_by_name("user")
                search_input.send_keys(Farmtext)
                search_input2 = driver.find_element_by_name("pw")
                search_input2.send_keys("327866aa")

                img_base64 = driver.execute_script("""
                                var ele = arguments[0];
                                var cnv = document.createElement('canvas');
                                cnv.width = 100; cnv.height = 40;
                                cnv.getContext('2d').drawImage(ele, 0, 0);
                                return cnv.toDataURL('image/jpeg').substring(22);    
                                """, driver.find_element_by_xpath(
                    "/html/body/div/div/div[2]/div[3]/div[2]/div/div/div/form/table/tbody/tr[3]/td[2]/img"))

                with open(r"image.jpg", 'wb') as f:
                    f.write(base64.b64decode(img_base64))

                img = cv2.imread("image.jpg", 0)
                kernel = np.ones((2, 2), np.uint8)
                erosion = cv2.erode(img, kernel, iterations=1)

                kernel1 = np.ones((3, 3), np.uint8)
                opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel1)

                pt.pytesseract.tesseract_cmd = r'C:\Users\Aygün\AppData\Local\Tesseract-OCR\tesseract.exe'
                text = pt.image_to_string(opening)

                driver.find_element_by_name("captcha").send_keys(text)
                WebDriverWait(driver, 5)

                driver.get('https://travianspeed.net/ts2/build.php?id=30')
                WebDriverWait(driver, 5)
                driver.find_element_by_name("x").send_keys(xnamebox)
                driver.find_element_by_name("y").send_keys(ynamebox)
                search = driver.find_element_by_name("r3")
                search.send_keys("4500000")
                search = driver.find_element_by_name("r4")
                search.send_keys("18000000")
                for i in range(10):
                    gonderbuton1 = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/form/table/tbody/tr/td[4]/a")
                    gonderbuton1.click()
                for i in range(4):
                    gonderbuton2 = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/form/table/tbody/tr[2]/td[4]/a")
                    gonderbuton2.click()
                for i in range(5):
                    gonderbuton3 = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div/form/table/tbody/tr[3]/td[4]/a")
                    gonderbuton3.click()
                searchbutton = driver.find_element_by_xpath("//button[@value='ok']")
                searchbutton.click()
                searchbutton = driver.find_element_by_xpath("//button[@value='ok']")
                searchbutton.click()
            driver.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())