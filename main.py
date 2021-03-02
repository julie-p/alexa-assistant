import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date, datetime
import os  # used to interact with the computer's directory

# Speech recognition constants
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Python text to speech (pyttsx3) constants
engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

# Trigger word in Listen Function
WAKE = "Alexa"

# Used to store user command for analysis
CONVERSATION_LOG = "Conversation Log.txt"

# Initial analysis of words to typically require a Google search
KEY_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}

class Alexa: 
    def __init__(self):
        # Initialization phase
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
    # Used to hear the commands after the trigger word has been said
    def hear(self, recognizer, microphone, response):
        try: 
            with microphone as source:
                print("Waiting for command...")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio)
                a.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")
            
    # Used to speak to the user
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()
        
    # Used to track the date of the conversation (maybe add time in the future)
    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as f:
            f.write("Conversation started on: " + today + "\n")
            
    # Writes each command from the user to the conversation log
    def remember(self, command):
        with open(CONVERSATION_LOG, "a") as f:
            f.write("User: " + command + "\n")
            
    # Find the key words in the users's request
    def find_key_words(self, command):
        if KEY_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:
            return True
    
    # Analyzes the command
    def analyze(self, command):
        try:
            # If the command starts with a key word => do a Google search
            if self.find_key_words(command):
                a.speak("Here is what I found.")
                webbrowser.open("http://www.google.com/search?q={}".format(command))
            # Different open commands
            elif command == "open youtube":
                a.speak("Opening Youtube.")
                webbrowser.open("https://www.youtube.com/feed/subscriptions")
            elif command == "open google":
                a.speak("Opening Google.")
                webbrowser.open("https://www.google.fr/")
            elif command == "open gmail":
                a.speak("Opening your Gmail.")
                webbrowser.open("https://mail.google.com/mail/u/0/?hl=fr#inbox")
            elif command == "open twitter":
                a.speak("Opening Twitter")
                webbrowser.open("https://twitter.com/")
            elif command == "open my documents":
                a.speak("Opening your Documents folder.")
                os.startfile("C:/Users/Julie/Documents")
            elif command == "introduce yourself":
                a.speak('I am Alexa. I am a digital assistant. How may I help you ?')
            else:
                a.speak("I don't know how to do that yet.")
        except TypeError:
            pass
        
    # Used to listen to the key words
    def listen(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source, timeout=5.0)
                    response = recognizer.recognize_google(audio)
                    if response == WAKE:
                        a.speak("How may I help you ?")
                        return response.lower()
                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error.")           
            
a = Alexa()
a.start_conversation_log()
while True:
    response = a.listen(recognizer, microphone)
    command = a.hear(recognizer, microphone, response)
    a.analyze(command)  