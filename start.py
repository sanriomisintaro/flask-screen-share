# === Start screen streaming server ===

import eventlet
eventlet.monkey_patch()  # Enable WebSocket support via eventlet

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import mss
import base64
import time
import socket
import sys

# Initialize Flask app and Socket.IO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

connected_ips = set()  # Menyimpan IP unik yang sudah terhubung (hapus IP dari console '1 dari 3')

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    """Menangani koneksi client dan mencatat IP unik."""
    ip = get_client_ip()
    if ip not in connected_ips:
        connected_ips.add(ip)
        print(f"IP baru terhubung: {ip}")
        print(f"Total client unik terhubung: {len(connected_ips)}\n")
    #hapus IP dari console '2 dari 3'
    #hapus baris ke 30 - 35, mulai dari ip = get_client_ip() hingga  print(f"Total client unik...") 
    #dan hilangkan tanda # pada #pass di bawah menjadi hanya pass    
    #pass

@socketio.on('start_stream')
def start_stream():
    """Start capturing the screen and stream frames via WebSocket."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        while True:
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            success, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 60])
            if not success:
                continue
            encoded = base64.b64encode(buffer).decode('utf-8')
            emit('frame', {'image': encoded})
            time.sleep(0.1)  # Approx. 10 FPS


def get_local_ip():
    """Get local IP address for access from other devices."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.168.0.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

from flask import request

def get_client_ip():
    """Mendeteksi alamat IP client dari request Flask."""
    if request.environ.get('HTTP_X_FORWARDED_FOR'):
        # Jika lewat proxy
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.remote_addr
    return ip

if __name__ == '__main__':
    try:
        local_ip = get_local_ip()
        print("\nAkses aplikasi dari web browser dan masukkan URL:")
        print(f"  {local_ip}:5000\n")
        print(f"    Pastikan anda menulis juga :5000 pada web browser\n")
        socketio.run(app, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nServer dihentikan oleh pengguna.")
        sys.exit(0)