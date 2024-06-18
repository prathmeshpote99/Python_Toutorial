# import pyttx3 module which speaks what you want

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text") # Enter text what you want
engine.runAndWait()