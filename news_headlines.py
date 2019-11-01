from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pyttsx3
import speech_recognition as sr
import pyaudio
r1=sr.Recognizer()
#from whatsapp_with_python import whatsapp_msg
def news():
    speech=pyttsx3.init()
    url='https://inshorts.com/en/read'
    inshorts=requests.get(url)
    page=BeautifulSoup(inshorts.text,'lxml')
    headlines=page.find_all(attrs={"itemprop":"headline"})

    driver=webdriver.Chrome()
    whatsapp=driver.get("https://web.whatsapp.com")
    speech.say('scan qr')
    speech.runAndWait()
    time.sleep(10)
    speech.say('to whom should i send news')
    speech.runAndWait()
    with sr.Microphone() as source:
        audio=r1.listen(source)
        try:
            name=r1.recognize_google(audio)
            print(name)
        except sr.UnknownValueError:
            speech.say("couldn't recognize ur voice")
            speech.runAndWait()
            print("couldn't recognize ur voice")

        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        wait=WebDriverWait(driver,20)
        user.click()

    msg_box=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    wait=WebDriverWait(driver,20)

    for headline in headlines:
        msg_box.click()
        msg_box.send_keys(headline.text)
        button=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[3]/button/span')
        wait=WebDriverWait(driver,20)
        button.click()
news()


    
