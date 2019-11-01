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
r2=sr.Recognizer()
r3=sr.Recognizer()
r4=sr.Recognizer()

def whatsapp_msg():
    driver = webdriver.Chrome()
    speech=pyttsx3.init()
    driver.get("https://web.whatsapp.com/")
    speech.say('scan qr')
    speech.runAndWait()
    time.sleep(10)
    speech.say('to whom should i send message')
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
        
    speech.say('what should i say')
    speech.runAndWait()
    with sr.Microphone() as source:
        audio=r2.listen(source)
        try:
            msg=r1.recognize_google(audio)
            print(msg)
        except sr.UnknownValueError:
            speech.say("couldn't recognize ur voice")
            speech.runAndWait()
            print("couldn't recognize ur voice")
    speech.say("should i repeat")
    speech.runAndWait()
    user=driver.find_element_by_xpath('//span[contains(@title,'+'"'+name+'"'+')]')

    wait=WebDriverWait(driver,20)
    user.click()

   
    with sr.Microphone() as source:
        audio=r3.listen(source)
        try:
            cmnd=r3.recognize_google(audio)
            print(cmnd)
            if 'yes' in cmnd:
                speech.say('enter how many times should i repeat?')
                speech.runAndWait()
                count= int(input())
                msg_box=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

                wait=WebDriverWait(driver,20)
                msg_box.click()
                for i in range(count):
    
                    msg_box.send_keys(msg)
                    button=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[3]/button/span')
                    wait=WebDriverWait(driver,20)
                    button.click()
                speech.say('message sent')
                speech.runAndWait()
            elif 'no' in cmnd:
                msg_box=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                wait=WebDriverWait(driver,20)
                msg_box.click()
                msg_box.send_keys(msg)
                button=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[3]/button/span')

                wait=WebDriverWait(driver,20)
                button.click()
                speech.say('message sent')
                speech.runAndWait()
        except sr.UnknownValueError:
            speech.say("couldn't recognize ur voice")
            speech.runAndWait()
            print("couldn't recognize ur voice")
        
    #//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span
whatsapp_msg()
