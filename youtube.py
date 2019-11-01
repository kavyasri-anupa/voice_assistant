from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pyttsx3
import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
def youtube():
    driver=webdriver.Chrome()
    speech=pyttsx3.init()
    driver.get('https://youtube.com/')
    WebDriverWait(driver,20)
    search=driver.find_element(By.XPATH,'//*[@id="search"]')
    WebDriverWait(driver,20)
    speech.say('what would you like to see?')
    speech.runAndWait()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            insearch=r.recognize_google(audio)
            print(insearch)
            search.send_keys(insearch)
            driver.find_element_by_id("search-icon-legacy").click()
        except sr.UnknownValueError:
            speech.say("sorry couldn't recognize ur voice")
            speech.runAndWait()
youtube()
