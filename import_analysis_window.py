## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##


## Sub-menu import ##
import existing_cell_import
## Sub-menu import ##


## Class: Import Analysis ##
## input: Welcome Window Root Window ##
##        FROM WELCOME_WINDOW.PY ##
## output: Analysis window -> Cell, Machines, Sub Machines -> Plot ##
class import_analysis:

    ## Boilerplate window generation, don't touch ##
    def __init__(self, root):
        root.title("Import Analysis Tool: Team 12")                                                                     #Title of window
        import_analysis_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        import_analysis_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                            #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                               #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##


    ## Import splash ##
        ttk.Label(import_analysis_mainframe, text="Import Analysis").grid(column=2, row=0, sticky=(N))                  #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
    ## Import splash ##

        self.cell = StringVar()
        cell_entry = ttk.Entry(import_analysis_mainframe, width=7, textvariable=self.cell)
        cell_entry.grid(column=2, row=2, sticky=(N))

        ttk.Button(import_analysis_mainframe, text="Name Cell", command=import_analysis).grid(column=1, row=3, sticky=W)

    ## Shortcut for padding widgets ##
        for child in import_analysis_mainframe.winfo_children():                                                        #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                        #Let each child have padding around edges of padx/y=<pixels>
    ## Shortcut for padding widgets ##