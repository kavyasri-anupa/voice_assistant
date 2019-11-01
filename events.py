birthdays={'September 06':'kavya','March 08':'chinnu','May 06':'dad','October 17':'Pranavi','November 11':'Laasya','December 09':'Indu',
           'May 20':'Buffy','May 15':'Penta','October 23':'Devi','February 03':'chinna','February 10':'akky'}
anniversaries={'Febraury 11':'parents'}
import pyttsx3
speech=pyttsx3.init()
speech.setProperty('rates',0.2)

from datetime import date
def events():
    #date=input('enter date: ')
    dates=date.today().strftime("%B %d")
    if dates in birthdays:
        name=birthdays[dates]
        speech.say(f"{name}'s birthday is on {dates}")
        speech.runAndWait()
        print(f"{name}'s birthday is on {dates}")
    elif dates in anniversaries:
        name=anniversaries[date]
        speech.say(f"{name}'s anniversary is on {dates}")
        speech.runAndWait()
        print(f"{name}'s anniversary is on {dates}")
    else:
        speech.say(f" no birthdays and anniversaries on {dates}")
        speech.runAndWait()
        print(f'no birthdays and anniversaries on {dates}')
events()
