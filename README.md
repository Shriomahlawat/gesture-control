gesture-control
Real-time hand gesture controlled game using Computer Vision (MediaPipe + OpenCV) that maps hand gestures to keyboard actions.

Hand Gesture Controlled Game 🎮
This project uses Computer Vision to control a game using hand gestures captured through a webcam.

Using MediaPipe hand tracking, the system detects finger positions in real-time and converts gestures into keyboard inputs.

The project demonstrates how touchless human-computer interaction can be implemented using Python and real-time landmark detection.

Features
Real-time hand tracking using webcam
Gesture-based control system
Maps gestures to keyboard inputs
Works with games that support arrow key controls
Lightweight and fast response
Gestures Implemented
Gesture	Action
👉 Index finger right	Move Right
👈 Index finger left	Move Left
✋ Open palm	Jump
✊ Closed fist	Roll
Tech Stack
Python
OpenCV
MediaPipe
PyAutoGUI
How it Works
Webcam captures live video
MediaPipe detects 21 hand landmarks
Finger positions are analyzed to identify gestures
Detected gesture is mapped to keyboard input
Game responds to keyboard action in real-time
Installation
Install dependencies:

pip install opencv-python mediapipe pyautogui
