## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##


## Sub-menu import ##
import new_analysis
import import_analysis
## Sub-menu import ##


## Class: Welcome Window ##
## input: Tk root window ##
##        FROM MAIN.PY ##
## output: Welcome window with buttons for new/import analysis -> new analysis window, import analysis window ##
class welcome_window:


    ## Boilerplate window generation, don't touch ##
    def __init__(self, root):
        root.title("Power Analysis Tool: Team 12")                                                                                  #Title of window
        mainframe = ttk.Frame(root, padding="3 3 12 12")                                                                            #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                                        #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                           #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##


    ## Welcome splash ##
        ttk.Label(mainframe, text="Welcome").grid(column=2, row=0, sticky=(N))                                                      #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
    ## Welcome splash ##


    ## Button labels and callbacks ##
        ttk.Button(mainframe, text="New", command=lambda:new_analysis.new_analysis(root)).grid(column=1, row=3, sticky=W)           #Buttons allow callbacks: command= lambda: <any_function_call>
        ttk.Button(mainframe, text="Import", command=lambda:import_analysis.import_analysis(root)).grid(column=3, row=3, sticky=W)  #Widgets can be assigned position with Grid=<ROWxCOL>, alignment
    ## Button labels and callbacks ##


    ## Shortcut for padding widgets ##
        for child in mainframe.winfo_children():                                                                                    #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                                    #Let each child have padding around edges of padx/y=<pixels>
    ## Shortcut for padding widgets ##
