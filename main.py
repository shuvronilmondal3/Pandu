import win32com.client
import speech_recognition as sr
import webbrowser
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "sorry Boss i don't understand you"

s=("Hello boss Tell me Something")
speaker.Speak(s)
while True:
    print("Listening.....")
    print("Tell something to pandu....")
    text = takeCommand()
    speaker.Speak(text)
    if "open YouTube".lower() in text.lower():
        speaker.Speak("Opening YouTube Sir")
        webbrowser.open("https://www.youtube.com/")
    if "go back".lower() in text.lower():
        print("Good Bye")
        speaker.Speak("Good Bye Sir")
        break

