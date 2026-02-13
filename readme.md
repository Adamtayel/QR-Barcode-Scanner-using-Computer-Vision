QR & Barcode Scanner using Computer Vision
-----------------------------------------
# Description:
This project uses computer vision to scan QR codes and barcodes in real-time using your computer camera.
-----------------------
# Features:

Automatically scans QR Codes and Barcodes.

Draws a green rectangle around detected codes.

Works on Mac M1/M2/M3/M4/M5 computers.

Easy to run with Python and OpenCV.
------------------------
# Requirements:

Python 3.10+

OpenCV

pyzbar

qrcode

PIL (Pillow)
-----------------------
Installation:

## Clone the repository
git clone https://github.com/Adamtayel/QR-Barcode-Scanner-using-Computer-Vision.git

## Go to the project folder
cd QR-Barcode-Scanner-using-Computer-Vision

## Install dependencies
pip install opencv-python pyzbar qrcode pillow

-----------------------
# Usage:

## Run the scanner
python scanner.py


Point your camera at a QR code or barcode.

The program will detect it, draw a green rectangle around it, and print the decoded data in the terminal.

Press q to quit the scanner.
-----------------------------------------------
# How it works:

The program uses OpenCV to access your computer camera and process video frames.

The pyzbar library detects QR codes and barcodes in each frame.

Detected codes are highlighted with a green rectangle, and their data is printed to the terminal.


![Scanner Test](screenshots/cam_test.png)
