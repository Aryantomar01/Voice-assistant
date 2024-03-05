import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour==12:
        speak("Good noon Sir")
    elif hour>12 and hour<=18:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    speak("I Am Aryan's Bot Sir. Please tell me how may i help you")

def takecommand():
    #it takes input from microphone and return output in string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sir please say that again...")
        return "None"
    return query






    

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        #Logic for executing query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Sir according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com")
        elif 'open Whatsapp web ' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open files' in query:
            filepath="C:\\Users\\Aryan Tomar\\OneDrive\\Desktop"
            os.startfile(filepath)
        elif 'open github' in query:
            webbrowser.open("github.com")
        

        

        
        
                
        

        
        









