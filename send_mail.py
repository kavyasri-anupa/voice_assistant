import pyaudio
import speech_recognition as sr
import pyttsx3
import smtplib
r1=sr.Recognizer()
r2=sr.Recognizer()
speech=pyttsx3.init()
def mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    speech.say('enter user mail')
    speech.runAndWait()
    user=input('')
    speech.say('enter password')
    speech.runAndWait()
    password=input('')
    server.login(user,password)
    speech.say('enter receiver mail')
    speech.runAndWait()
    receiver=input('')
    speech.say('what shoud I say')
    speech.runAndWait()
                
    with sr.Microphone() as source:
        audio3=r2.listen(source)
        msg=r2.recognize_google(audio3)
        speech.say('you said'+msg)
        speech.runAndWait()
        server.sendmail(user,receiver,msg)
        server.quit()
        speech.say('message sent')
        speech.runAndWait()

        
