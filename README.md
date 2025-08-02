# flask-screen-share
A lightweight screen sharing app built with Flask and WebSocket.  
This lets you stream your desktop screen to other devices (PC, phone, tablet) in the same local network, all through the browser.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)

---

## How It Works
This app uses Flask and WebSocket to capture your screen and stream it to other devices on the same network in real time:

- Flask serves the HTML interface (via Jinja templates).
- Flask-SocketIO (with eventlet) enables WebSocket communication between the server and client.
- MSS captures the primary monitor’s screen as an image every ~100ms.
- OpenCV encodes the image into a JPEG format.
- The JPEG is base64-encoded so it can be sent as text.
- The client receives the image via WebSocket and updates the <img> element instantly.
- The server logs the number of unique IPs that have connected.

The result: a lightweight screen viewer that updates live in any browser and no app installation needed.

---

## Features

- Real-time screen capture and streaming (~10 FPS)
- No installation needed on the client — just open a browser
- Accessible from other devices in the same Wi-Fi network
- Built with Flask, Flask-SocketIO, OpenCV, and eventlet
- Tracks connected clients (unique IP-based logging)
- Fullscreen viewing support

---

## Requirements

- Python 3.13 or newer  
- Operating System: Tested on Windows, but should also work on Linux and macOS  
- A local network connection (LAN or Wi-Fi)  
- A modern web browser (e.g. Google Chrome, Firefox, etc.)  
- At least one other device to access the shared screen

---

## Installation

Open Your terminal/CMD
Clone the project and navigate to the folder:

```bash
git clone https://github.com/sanriomisintaro/flask-screen-share.git
cd flask-screen-share
```   
Create a virtual environment (optional):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## How to Use

Start the screen-sharing server:
```bash
python start.py
```
You will see this in the terminal:
```bash
Akses aplikasi dari web browser dan masukkan URL:
  xxx.xxx.xxx.xxx:5000
    Pastikan anda menulis juga :5000 pada web browser
```
Then, open the given IP (with :5000) in a browser on another device. (ex: 192.168.2.100:5000)

To stop the apps, press CTRL+C in terminal.

---

## Security Notes

- This project is meant for local/private network use only
- No authentication or encryption is implemented
- Do not expose to the internet without additional layers (e.g. reverse proxy, TLS, password)
- Please Stop the apps after the class is over or just close the terminal to stop the running apps.

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute it for personal or commercial purposes, as long as you include the original license and credit.

---
