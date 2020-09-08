from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ctypes
import time
import threading

# INFORMATION ABOUT 20/20/20 RULE MSG BOX

def info_msg_box():
    messagebox.showinfo("20/20/20 Rule info", "The rule says that for every 20 minutes spent looking at a screen, \n"
                                              "a person should look at something 20 feet away for 20 seconds. \n"
                                              "Following the rule is a great way to remember to take frequent breaks. \n"
                                              "This should reduce eye strain caused by looking at digital screens for too long.\n\n\n"
                                              "This is free software which turns your display window off every 20 minutes. \n"
                                              "Fell free to use it. Wish Your EYES Best! @Propsowicz")

# TURN SCREEN DISPLAY OFF AND ON FUNCTION

blacking = True
def black_on():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

def black_off():
    return ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)

def run():
    while blacking:
        time.sleep(20)
        black_on()
        black_off()
        time.sleep(20 * 60)

# TKINTER GUI

root = Tk()
root.title("20/20/20 Rule")
frame = Frame(root)
root.geometry("210x20+400+400")
root.resizable(height = False, width = False)
ttk.Style().theme_use("clam")

the_menu = Menu(root)
file_menu = Menu(the_menu, tearoff = 0)
file_menu.add_command(label = "20/20/20 Rule info", command = info_msg_box)
file_menu.add_separator()
the_menu.add_cascade(label = "Info", menu = file_menu)
root.config(menu = the_menu)

threading.Thread(target = run).start()

mainloop()

blacking = False



