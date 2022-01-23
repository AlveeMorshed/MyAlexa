import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer();
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    try:
        with sr.Microphone() as source:
            command = ''
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            while command == '':
                talk("Sorry, I did not get you. Will you kindly repeat it?")
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def runAlexa():
    command = takeCommand()
    if 'alexa' in command:
        print(command)
        command = command.replace('alexa', '')
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)
        elif 'who is' in command or 'who are' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('Sorry, I have a headache')
        elif 'are you single' in command:
            talk("I'm in a relationship with WiFi")
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'stop' in command or 'shut up' in command:
            return 0
        else:
            talk("Sorry, I did not get you. Will you kindly repeat it?")
    else:
        talk("Sorry, I did not get you. Will you kindly repeat it?")


while True:
    rt = runAlexa()
    if rt == 0:
        break;
