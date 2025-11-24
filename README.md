# Demo Intro

https://github.com/user-attachments/assets/94ce1b13-7564-4d9c-9b8f-81f6047eb340

# Advanced Robotic Control System

This project is a collection of Python scripts for controlling a robot using various advanced methods, including computer vision and voice recognition. It provides a flexible and extensible framework for developing and testing different robot control strategies.

## Features

- **Color Following**: The robot can detect and follow objects of a specific color.
- **Face Tracking**: The robot can detect and track human faces.
- **Gaze Control**: The robot's movement can be controlled by the user's gaze.
- **Hand Gesture Recognition**: The robot can be controlled using hand gestures.
- **Voice Control**: The robot can be controlled using voice commands.
- **Mobile Control**: The robot can be controlled using a mobile interface.
- **User Interface**: A user-friendly interface for controlling the robot.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- A webcam or camera module connected to your system

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required dependencies:**
    It is recommended to create a virtual environment to manage the project's dependencies.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    Install the necessary libraries using pip. A `requirements.txt` file is not yet available, but you can install the required packages manually. Key dependencies include:
    - `opencv-python`
    - `numpy`
    - `dlib`
    - `tensorflow`
    - `SpeechRecognition`
    - `pyaudio`

    You can install them like this:
    ```sh
    pip install opencv-python numpy dlib tensorflow SpeechRecognition pyaudio
    ```

## Modules

This project is organized into several modules, each responsible for a specific functionality.

- **`MotorModule.py`**: This module provides a low-level interface for controlling the robot's motors. It includes functions for moving the robot forward, backward, and turning.

- **`KeyboardPressModule.py`**: This module allows for controlling the robot using keyboard inputs, which is useful for testing and debugging.

- **`CustomRPIRobot/`**: This directory contains scripts related to custom Raspberry Pi robot functionalities, including lane detection and color picking.

- **`Hand_Gesture/`**: This module enables hand gesture recognition for robot control. It uses computer vision to detect and interpret hand gestures.

- **`Mobile/`**: This directory contains a script for a mobile interface to control the robot.

- **`User_Interface/`**: This module provides a graphical user interface for controlling the robot.

- **`colour_following_robot/`**: This module allows the robot to follow an object of a specific color.

- **`face_tracking_robot/`**: This module enables the robot to track faces in real-time.

- **`gaze_control/`**: This module implements gaze control, allowing the user to control the robot's movement with their eyes.

- **`voice_control_robot/`**: This module provides voice command functionality for controlling the robot.

## Usage

To run a specific module, you can execute the main script within that module's directory. For example, to run the face tracking module:

```sh
python face_tracking_robot/face_tracking.py
```

## Dependencies

This project relies on the following Python libraries:

- **OpenCV**: For computer vision tasks such as face detection, color tracking, and hand gesture recognition.
- **NumPy**: For numerical operations and handling image data.
- **dlib**: For facial landmark detection, used in the gaze control module.
- **TensorFlow**: For machine learning tasks, particularly in the gaze control module.
- **SpeechRecognition**: For converting spoken language into text.
- **PyAudio**: As a dependency for `SpeechRecognition` to handle audio input.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
