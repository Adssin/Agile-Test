import speech_recognition as sr 
from GoogleNews import GoogleNews
import pyttsx3
import datetime
import webbrowser
import pywhatkit

#Intialization
googlenews = GoogleNews()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()


#Commands
def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source,timeout=5)
        print("Done recording..!")
    try:
        command=recognizer.recognize_google(recordedaudio,language='en_US')
        command=command.lower()
        print('Your message:',format(command))

    except Exception as ex:
        print(ex)


    #hello
    if 'hello' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 250)
        engine.say('Hello Aditya Sir, How are you today?')
        engine.runAndWait()


    #news
    if "today's news" in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 250)
        a = googlenews.get_news('Todays news')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5],sep=',')
        engine.say(a)
        engine.runAndWait()


    #time
    if 'what is time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say("Time right now is")
        engine.say(time)
        engine.runAndWait()


    #gm
    if 'good morning' in command:
        engine.say("Good morning Aditya Ji, Have a great day today!")
        engine.runAndWait()


    #youtube
    if 'open youtube' in command:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')


    #ram     
    if 'hare ram' in command:
        engine.say("Jay Shree Ram")
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=vVgz3Pg-EMs&t=107s')

    #creator
    if 'who is your creator' in command:
        engine.say("My Creator is Addy Sir, He lives in India and he made me using Python")
        engine.runAndWait()

    #weather
    if 'how is the weather today' in command:
        a = googlenews.get_news("Indore city Temprature")
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5],sep=',')
        engine.say(a)
        engine.runAndWait()

    #jarvis
    if 'hey jarvis' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 200)
        a = 'Ji Aditya Sir?'
        engine.say(a)
        engine.runAndWait()

    if 'how smart are you' in command:
        a='I can do anything for you Aditya ji, like'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('www.youtube.com/watch?v=dQw4w9WgXcQ')


    if 'aur batao' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 180)
        engine.say("Kya batao Aditya ji")
        engine.runAndWait()        


    if 'bye' in command:
        engine.say("Bye bye Aditya ji")
        engine.runAndWait()

    if 'open mail' in command:
        engine.say("opening mails sir")
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
        engine.runAndWait()

    if 'open linkedin' in command:
        engine.say("Opening Linkedin")
        webbrowser.open("www.linkedin.com/in/addy007")
        engine.runAndWait()
    
    if 'jay shri ram' in command:
        engine.say("JAY SHREE RAM!")
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=dZxrpr_yS5g&t=6s')


    if 'play a song' in command:
        engine.say("Here's a song for you, ")
        webbrowser.open("https://www.youtube.com/watch?v=LMeZAyPaRsU")
        engine.runAndWait()




    
    



cmd()