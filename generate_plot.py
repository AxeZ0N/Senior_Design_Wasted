## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##

import import_viewer

class existing_cell_import():

    ## Boilerplate window generation, don't touch ##
    def __init__(self, root):
        root.title("Existing Cell Import")                                                                                    #Title of window
        self.new_analysis_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                               #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.new_analysis_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                           #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                           #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##

        
