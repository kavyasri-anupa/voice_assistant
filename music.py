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
def music():
    driver=webdriver.Chrome()
    driver.get('https://jiosaavn.com/')
    WebDriverWait(driver,20)
    speech=pyttsx3.init()
    with sr.Microphone() as source:
        speech.say('what song should i play?')
        speech.runAndWait()
        audio=r1.listen(source)
        try:
            song=r1.recognize_google(audio)
            print(song)
            driver.find_element_by_xpath('//*[@id="search"]').send_keys(song)
            WebDriverWait(driver,20)
            time.sleep(5)
            driver.find_element_by_class_name("play").click()
    #driver.find_element_by_xpath('//*[@id="main"]/div/section/div/div[2]/div/div/button').click()
            WebDriverWait(driver,20)
        except sr.UnknownValueError:
            speech.say("couldn't recognize ur voice")
            speech.runAndWait()
            print("couldn't recognize ur voice")
music()

