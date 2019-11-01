birthdays={'September 06':'John','March 08':'smith','May 06':'Tim','October 17':'Bella','October 23':'David','November 07':'Tina','December 09':'Shiyaa',
           }
anniversaries={'Febraury 11':'Tim and Tina'}
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
