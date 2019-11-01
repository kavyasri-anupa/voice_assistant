import pyaudio
import speech_recognition as sr
import pyttsx3
import smtplib

speech=pyttsx3.init()
speech.say("say something")
speech.runAndWait()
r1=sr.Recognizer()
r2=sr.Recognizer()
with sr.Microphone() as source:
    print('what would you like to do?')
    audio=r1.listen(source)
    try:
        command=r1.recognize_google(audio)
        print(command)
        if 'mail' in command:
            from send_mail import mail
            mail()
        elif 'whatsapp' in command:
            from whatsapp_with_python import whatsapp_msg
           
        elif 'news' in command:
            from news_headlines import news
            
        elif 'events' in command:
            from events import events
            
        elif 'youtube' in command:
            from youtube import youtube
            
        elif 'music' in command:
            from music import music
        elif 'assistant' in command:
            from voice_assistant import voice_assistant
            
            
            
    except sr.UnknownValueError:
        print("couldn't recognize ur voice")

    
        
        
