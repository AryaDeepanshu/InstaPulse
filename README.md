# InstaPulse
## Instant Pulse

This project estimates real time cardiac rate of a person through remote photoplethysmography(rPPG) without any physical contact with sensor, by detecing blood volume pulse induced subtle color changes from video stream through webcam sensor.

## Features

- Estimates heart rate in real time
- Ultra fast face detection
- Plots different graph in realtime
- Sepreately shows Region of Interest in separate window
- Graphs are automatically saved after test is over.

## Tech

InstaPulse is a Python based application and is powered by many powerfull modules and technologies 

- [OpenCV](https://opencv.org/) - Opensource computer vision library!
- [Mediapipe](https://google.github.io/mediapipe/) - Ultra fast and customizable ML solutions for live and streaming 
- [Numpy](https://numpy.org/) -  An open source project aiming to enable numerical computing with Python
- [Matplotlib](https://matplotlib.org/) - An comprehensive library for creating static, animated, and interactive visualizations in Python
- [Scipy](https://scipy.org/) - SciPy provides algorithms for optimization, differential equations, statistics and many other classes of problems
- [Butterworth Filter](https://en.wikipedia.org/wiki/Butterworth_filter) - A type of signal processing filter designed to have a frequency response that is as flat as possible in the passband

## Installation

### Linux (Recommended)
Re-Cordiac requires [Python](https://www.python.org/) v3.10+ to run.

1. Clone the repo
   ```sh
   git clone https://github.com/AryaDeepanshu/rppg.git
   ```
2.Setting up [virtual enviornment](https://docs.python.org/3/library/venv.html)

3. Install requirements
    ```sh
    pip3 install -r requirements.txt #for python version 3.0+
    pip install -r requirements.txt #for python version < 3
    ```
4. Running project
    ```sh
    python3 get_face.py #for python version 3.0+
    python getface.py #for python version < 3
    ```
### Windows
> :warning: **Make sure python is added to path correctly else the following command may not work, in case try to replace "python" with "py- m" in each command**: Be very careful here!
1. Clone the repo
   ```sh
   git clone https://github.com/AryaDeepanshu/rppg.git
   ```
2. Setting up [virtual enviornment](https://docs.python.org/3/library/venv.html)
3. Install requirements
    ```sh
    pip3 install -r requirements.txt #for python version 3
    pip install -r requirements.txt #for python version < 3.0+
    ```
    > :warning: **Some package like PyQT5 may need [Windows C++ Build Tool](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017) and mediapipe might also require some other dependenci **: Be very careful here!
4. Running project
    ```sh
    python3 get_face.py #for python version 3.0+
    python getface.py #for python version < 3
    ```
