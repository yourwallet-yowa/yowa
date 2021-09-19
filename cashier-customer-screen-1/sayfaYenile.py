cuzdanAdresi = "0xea0a6e3c511bbd10f4519ece37dc24887e11b55d"

from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path='geckodriver.exe')

def refreshPage():
    browser.get("https://bscscan.com/address/" + str(cuzdanAdresi))
    time.sleep(5)
    refreshPage()

refreshPage()