import os
import webbrowser
import pyautogui
import pyttsx3
import subprocess
from modules.free_conversation import generate_response

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def execute_action(action):
    if action == "open:browser":
        webbrowser.open("https://www.google.com")
        speak("Opening browser.")

    elif action == "file:create":
        with open("new_file.txt", "w") as f:
            f.write("This is a new file created by NITA.")
        speak("File created successfully.")

    elif action == "joke:tell":
        speak("Why did the computer get cold? Because it left its Windows open!")

    elif action == "media:play":
        speak("Playing music...")

    elif action == "media:stop":
        speak("Stopping music...")

    elif action == "open:notepad":
        os.system("notepad.exe")
        speak("Opening Notepad.")

    elif action == "search:web":
        webbrowser.open("https://www.google.com/search?q=your+query")
        speak("Searching Google.")

    elif action == "alarm:set":
        speak("Alarm set. I’ll remind you on time.")
    elif action == "weather:check":
        speak("Currently, I can't check weather, but I’m learning!")

    elif action == "ai:conversation":
        speak("I'm here to talk!")

    elif action == "email:send":
        speak("Email sending is not set up yet.")

    elif action == "time:check":
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif action == "screenshot:take":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot taken.")

    elif action == "open:calculator":
        os.system("calc.exe")
        speak("Opening Calculator.")

    elif action == "open:paint":
        os.system("mspaint.exe")
        speak("Opening Paint.")

    elif action == "open:camera":
        os.system("start microsoft.windows.camera:")
        speak("Opening Camera.")

    elif action == "open:explorer":
        os.system("explorer")
        speak("Opening File Explorer.")

    elif action == "open:cmd":
        os.system("start cmd")
        speak("Opening Command Prompt.")

    elif action == "open:settings":
        os.system("start ms-settings:")
        speak("Opening Settings.")

    elif action == "open:taskmanager":
        os.system("start taskmgr")
        speak("Opening Task Manager.")

    elif action == "open:controlpanel":
        os.system("control")
        speak("Opening Control Panel.")

    else:
        speak("I didn't understand that. Let me try responding with AI.")
        ai_response = generate_response(action)
        if ai_response:
            speak(ai_response)
        else:
            speak("I'm sorry, I couldn't generate a response.")
