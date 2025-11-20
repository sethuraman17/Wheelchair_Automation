import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assault' in command:
                command = command.replace('assault', '')
                print(command)

    except:
        pass
    return command

talk("Hi Boss, Iam assault")
talk("tell me, How can i halp you")


def run_baby():
    command = take_command()
    print(command)
    if 'play a song' in command:
        song = command.replace('play', '')
        talk('okay ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'who invented you' in command:
        talk('I was created by sethuraman and abiraj')
        talk('Im the result of programming and engineering efforts')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'go forward' in command:
        talk('moving forward')

    elif 'go backward' in command:
        talk('moving backward')

    elif 'take right' in command:
        talk('taking right')

    elif 'take left' in command:
        talk('taking left')

    elif 'follow me' in command:
        talk('okay')
        subprocess.run(['Python', 'face_tracking_robot/face_tracking.py'])

    elif 'track me' in command:
        talk('okay')
        subprocess.run(['Python', 'colour_following_robot/color.py'])

    elif 'listen my hand' in command:
        talk('okay')
        subprocess.run(['Python', 'Hand_Gesture/hand_gesture_robot.py'])

    elif 'go in lane' in command:
        talk('okay')
        subprocess.run(['Python', 'CustomRPIRobot/LaneDetectionModule.py'])

    elif 'play competitive game' in command:
        talk('okay')
        subprocess.run(['Python', 'pose_detection_unity/GTA.py'])

    elif 'play game with me' in command:
        talk('okay')
        subprocess.run(['Python', 'AIgame/main.py'])

    elif 'play multiplayer game' in command:
        talk('okay')
        subprocess.run(['Python', 'Pong Game/main.py'])

    elif 'stimulate your working' in command:
        talk('okay')
        subprocess.run(['Python', 'stimulation/lane.py'])

    elif 'book appointment for me' in command:
        talk('okay')
        subprocess.run(['Python', 'voice_control_robot/appointment_booking.py'])

    else:
        talk('I cant able to hear anything')
        talk('please can you repeat the command once again')

run_baby()
