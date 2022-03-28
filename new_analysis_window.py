## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##


## Sub-menu import ##
import cell_creation_window
## Sub-menu import ##


## Class: New Analysis ##
## input: Welcome Window Root Window ##
##        FROM WELCOME_WINDOW.PY ##
## output: Window with Cell name entry -> Config Tool window ##
class new_analysis:

## Fucntion: Config Tool Gen ##
## input: Cell Name ##
##        FROM NEW_ANALYSIS.PY ##
## output: Config Tool window with name of cell -> leading to machine and sub machine SELECTION ##
## returns: DOES NOT RETURN IN LIVE BUILD ##


    ## START INIT ##
    ## Boilerplate window generation, don't touch ##
    def __init__(self, root):
        root.title("New Analysis Tool: Team 12")                                                                                    #Title of window
        self.new_analysis_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                               #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.new_analysis_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                           #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                           #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##


    ## Enter Cell name ##
        ttk.Label(self.new_analysis_mainframe, text="Enter Cell name").grid(column=0, row=2, sticky=(N))                                    #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
    ## Enter Cell name ##


    ## String Variable for cell name ##
        self.cell = StringVar()                                                                                                          #StringVar allows easy access through inheritance
        cell_entry = ttk.Entry(self.new_analysis_mainframe, width=7)                                             #Entry widget gives a text box, allows inheritable text variable
        cell_entry.grid(column=2, row=2, sticky=(N))  
    ## String Variable and text entry ##


    ## Button labels and callbacks ##
        ttk.Button(self.new_analysis_mainframe, text="Create Cell",
         command=lambda:cell_creation_window.cell_creation_window(root, cell_entry.get())).grid(column=2, row=4, sticky=S)    #Buttons allow callbacks: command= lambda: <any_function_call>
    ## Button labels and callbacks ##                                                                                               #Widgets can be assigned position with Grid=<ROWxCOL>, alignment


    ## Shortcut for padding widgets ##
        for child in self.new_analysis_mainframe.winfo_children():                                                                       #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                                    #Let each child have padding around edges of padx/y=<pixels>
    ## Shortcut for padding widgets ##

        cell_entry.focus()

