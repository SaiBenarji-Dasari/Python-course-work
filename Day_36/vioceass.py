import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# ----------------------------
# SPEAK FUNCTION
# ----------------------------

def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")

    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)
    else:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ----------------------------
# LISTEN FUNCTION
# ----------------------------

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=5) as source:
        print("Listening..........")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    print("Audio Done")

    try:
        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError as e:
        print("Could not connect to Google.")
        print("Error:", e)
        return ""


# ----------------------------
# PROCESS COMMAND
# ----------------------------
speak("Hello I'm Your Voice Assistant. How can i help You")

while True:

    command = listen()

    if "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(
            f"The current time is {current_time}"
        )

    elif "date" in command:

        today = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        speak(
            f"Today's date is {today}"
        )

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open(
            "https://www.google.com"
        )

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open(
            "https://www.youtube.com"
        )

    elif "open gmail" in command:

        speak("Opening Gmail")

        webbrowser.open(
            "https://mail.google.com"
        )

    elif "open chat g p t" in command:

        speak("Opening Chat GPT")

        webbrowser.open(
            "https://chatgpt.com"
        )

    elif "your name" in command:

        speak(
            "My name is Nova. I am your personal assistant."
        )

    elif "hello" in command:

        speak(
            "Hello. How can I help you today?"
        )

    elif "who created you" in command:

        speak(
            "I was created using Python and Tkinter."
        )

    elif "bye" in command or "exit" in command:

        speak(
            "Goodbye. Have a great day."
        )
        break


    elif "locate" in command:

        speak("Which place do you want to locate?")

        place = listen()

        if place:

            speak(f"Locating {place}")

            url = f"https://www.google.com/maps/search/{place}"

            webbrowser.open(url)
    
    elif "play" in command:

        song = command.replace("play","")

        speak(f"Playing {song}")

        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "who is" in command:

        person = command.replace("who is","")

        try:

            info = wikipedia.summary(
            person,
            sentences=2
            )

            speak(info)

        except:

            speak("Sorry, I couldn't find that.")
    
    elif "weather" in command:

        city = listen()

        webbrowser.open(
            f"https://www.google.com/search?q=weather+{city}"
            )

    else:

        speak(
            "Sorry. I do not know that command yet."
        )
