## GUI library import ##
from tkinter import *
from tkinter import Tk as Tk
## GUI library import ##


## Sub-menu import ##
import welcome_window as ww
## Sub-menu import ##


## Root window creation ##
root = Tk()                                                     #The root window is made from the base Tk() class
ww.welcome_window(root)                                         #Call the class above to generate the internals of the window


## DO NOT TOUCH ##
## Main loop controls all mouse/kb interaction with the gui ##
root.mainloop()                                                                                         
## DO NOT TOUCH ##