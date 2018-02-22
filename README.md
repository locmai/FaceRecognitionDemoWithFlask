# Face recognition demo with Flask

## Prerequisites

* CMake

## Required packages

Install by using pip:

```bash
pip install -r requirements.txt
```

List:

```bash
pip freeze
click==6.7
dlib==19.9.0
face-recognition==1.2.1
face-recognition-models==0.3.0
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
numpy==1.13.1
opencv-python==3.2.0.8
Pillow==5.0.0
scipy==1.0.0
```

## Run with OpenCV camera for streaming

```bash
set CAMERA=opencv
python main.py
```

## Run with Frame checker camera

```bash
set CAMERA=check
python main.py
```