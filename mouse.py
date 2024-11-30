import pyautogui as pag
import time
import cv2  
import pytesseract as tess
import os
import sys

def resource_path(relative_path):
    """Dapatkan jalur file (baik saat dijalankan dari .exe maupun .py)"""
    if hasattr(sys, '_MEIPASS'):
        # Ketika dijalankan dari .exe, PyInstaller akan mengekstrak file ke folder sementara
        base_path = sys._MEIPASS
    else:
        # Ketika dijalankan dari .py
        base_path = os.path.abspath(".")
    full_path = os.path.join(base_path, relative_path)
    print(f"Resource path: {full_path}")  # Debug log
    return full_path


tess.pytesseract.tesseract_cmd = r'C:\Users\Jacky Sakti Pratama\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def lapak():
    a, b = pag.locateCenterOnScreen("images/web/lapak.png", confidence= 0.8)
    pag.moveTo(a, b, 0.5)
    pag.leftClick()
    pag.moveTo(117, 80, 0.5)
    pag.leftClick()
    time.sleep(1)
    pag.moveTo(228, 457, 0.5)
    pag.leftClick()
    time.sleep(0.5)
    pag.scroll(1000)

def paste():
    pag.moveTo(pag.locateOnScreen("images/tombolnew/input.png"))
    pag.leftClick()
    pag.hotkey("ctrl","v")
    pag.moveTo(1146, 633, 0.5)
    pag.leftClick()
    time.sleep(2)
    if pag.locateOnScreen("images/benar.png", confidence=0.8, region=[641, 427, 600, 370]) != None:
        x, y = pag.locateCenterOnScreen("images/tombolnew/ok.png", confidence=0.8, region=[641, 427, 600, 370])
        pag.moveTo(x, y, 0.5)
        pag.leftClick()
    else:
        print("Invalid Id")

def copy():
    pag.moveTo(628, 871, 0.5)
    pag.leftClick()
    pag.leftClick()
    pag.hotkey("ctrl","c")

def pid():
    time.sleep(1)
    if (pag.locateOnScreen("images/tombolnew/pids888.png", confidence= 0.8)) != None:
        x, y = pag.locateCenterOnScreen("images/tombolnew/pids888.png", confidence= 0.8)
        pag.moveTo(x, y, 0.5)
        pag.leftClick()
    else:
        x, y = pag.locateCenterOnScreen("images/tombolnew/pids18.png", confidence= 0.8)
        pag.moveTo(x, y, 0.5)
        pag.leftClick()
    pag.scroll(-500)
    time.sleep(0.5)

def donelapak():
    c, d = pag.locateCenterOnScreen("images/tombolnew/order.png", confidence= 0.8)
    pag.moveTo(c, d, 0.5)
    pag.leftClick()

def lapak31cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/31cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    pid()
    donelapak()

def lapak63cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/63cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak128cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/128cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak321cp():
    lapak()
    paste()
    pag.scroll(-500)
    pag.moveTo(596, 581, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()    

def lapak645cp():
    lapak()
    paste()
    pag.scroll(-500)
    pag.moveTo(1061, 579, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak800cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/800cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak1373cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/1373cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak2060cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/2060cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak3564cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/3564cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak5618cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/5618cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak7656cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/7656cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak15312cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/15312cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak38280cp():
    lapak()
    paste()
    pag.scroll(-500)
    pag.moveTo(1299, 793, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def lapak76560cp():
    lapak()
    paste()
    pag.scroll(-500)
    x, y = pag.locateCenterOnScreen("images/denom/76560cp.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    pag.scroll(-200)
    time.sleep(0.5)
    pid()
    donelapak()

def done():
    x, y = pag.locateCenterOnScreen("images/web/kustore.png", confidence= 0.8)
    pag.moveTo(x, y, 0.5)
    pag.leftClick()
    a, b = pag.locateCenterOnScreen("images/tombolnew/check.png", confidence= 0.8, region=[283, 853, 1620, 125])
    pag.moveTo(a, b, 0.5)
    pag.leftClick()
    c, d = pag.locateCenterOnScreen("images/tombolnew/aksi.png", confidence= 0.8)
    pag.moveTo(c, d, 0.5)
    pag.leftClick()
    e, f = pag.locateCenterOnScreen("images/tombolnew/sukses.png", confidence= 0.8)
    pag.moveTo(e, f, 0.5)
    pag.leftClick()
    time.sleep(1)
    g, h = pag.locateCenterOnScreen("images/tombolnew/iya.png", confidence= 0.8)
    pag.moveTo(g, h, 0.5)
    pag.leftClick()
    time.sleep(1)

# Loop utama untuk mencari orderan
while True:
    order_found = False  # Flag untuk menandai apakah ada order yang ditemukan

    try:
        if pag.locateOnScreen("images/denom/31cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) is not None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("images/id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 31 CP pada id "+text)
            copy()
            lapak31cp()
            done()
            print("Orderan Selesai")
            pag.moveTo(673, 705, 0.5)
            pag.leftClick()
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/63cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 63 CP pada id "+text)
            copy()
            lapak63cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/128cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 128 CP pada id "+text)
            copy()
            lapak128cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/321cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 321 CP pada id "+text)
            copy()
            lapak321cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/645cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 645 CP pada id "+text)
            copy()
            lapak645cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/800cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 800 CP pada id "+text)
            copy()
            lapak800cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/1373cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 1373 CP pada id "+text)
            copy()
            lapak1373cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/2060cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 2060 CP pada id "+text)
            copy()
            lapak2060cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/3564cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 3564 CP pada id "+text)
            copy()
            lapak3564cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/7656cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 7656 CP pada id "+text)
            copy()
            lapak7656cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/15312cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 15312 CP pada id "+text)
            copy()
            lapak15312cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/38280cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 38280 CP pada id "+text)
            copy()
            lapak38280cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    try:
        if pag.locateOnScreen("images/denom/76560cpku.png", confidence=0.8, region=[284, 851, 1590, 130]) != None:
            order_found = True  # Order ditemukan
            img = pag.screenshot("id.png",region=[545, 854, 200, 90])
            text = tess.image_to_string(img)
            print("Ada orderan 76560 CP pada id "+text)
            copy()
            lapak645cp()
            done()
            print("Orderan Selesai")
            time.sleep(3)
    except:
        pass

    # Jika tidak ada order yang ditemukan, cetak pesan "Sedang Mencari Orderan"
    if not order_found:
        print("Sedang Mencari Orderan")
        pag.moveTo(673, 705, 0.5)
        pag.leftClick()
        time.sleep(2)

# Cek Koordinasi (JANGAN HAPUS)
# while True:
#     x, y= pag.position()
#     print(x, y)
#     time.sleep(1)

# Test Screenshoot Koordinat (JANGAN HAPUS)
# pag.screenshot("coba.png",region=[641, 427, 600, 370])    

# print("Ada orderan 31 CP pada id 123456789")
# print("Invalid Id")