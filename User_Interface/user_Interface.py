import tkinter as tk
import subprocess

def run_colour_following_robot():

    subprocess.run(['Python', '../colour_following_robot/color.py'])

def run_face_tracking_robot():

    subprocess.run(['Python', '../face_tracking_robot/face_tracking.py'])

def run_hand_gesture_robot():

    subprocess.run(['Python', '../Hand_Gesture/hand.py'])

def run_custom_rpi_robot():

    video_file_path = '../CustomRPIRobot/test1.mp4'
    subprocess.run(['Python', '../CustomRPIRobot/LaneDetectionModule.py', video_file_path])

def run_voice_control_robot():

    subprocess.run(['Python', '../voice_control_robot/VoiceModule.py'])


root = tk.Tk()
root.title("Hybrid WheelChair")
root.geometry("640x480")

colour_following_robot_button = tk.Button(root, text="Colour_Following_Robot", command=run_colour_following_robot, padx=10, pady=10)

face_tracking_robot_button = tk.Button(root, text="Face_Tracking_Robot", command=run_face_tracking_robot, padx=10, pady=10)

hand_gesture_button = tk.Button(root, text="Hand_Gesture_Robot", command=run_hand_gesture_robot, padx=10, pady=10)

custom_rpi_robot_button = tk.Button(root, text="Lane_Detection_Robot", command=run_custom_rpi_robot, padx=10, pady=10)

voice_control_robot_button = tk.Button(root, text="Voice_Assistant_Robot", command=run_voice_control_robot, padx=10, pady=10)

colour_following_robot_button.pack()

face_tracking_robot_button.pack()

hand_gesture_button.pack()

custom_rpi_robot_button.pack()

voice_control_robot_button.pack()


root.mainloop()
