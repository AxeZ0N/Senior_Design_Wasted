## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##



class new_analysis:

    ## Boilerplate window generation, don't touch ##
    def __init__(self, root):
        root.title("New Analysis Tool: Team 12")                                                                            #Title of window
        new_analysis_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                       #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        new_analysis_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                   #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                   #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)

    ## Boilerplate window generation, don't touch ##


    ## Welcome splash ##
        ttk.Label(new_analysis_mainframe, text="New Analysis").grid(column=2, row=0, sticky=(N))                            #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
    ## Welcome splash ##

        self.cell = StringVar()
        cell_entry = ttk.Entry(new_analysis_mainframe, width=7, textvariable=self.cell)
        cell_entry.grid(column=2, row=2, sticky=(N))

        ttk.Button(new_analysis_mainframe, text="Name Cell", command="fuck").grid(column=1, row=3, sticky=W)

        for child in new_analysis_mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        
        new_analysis_mainframe.bind("<Return>", self.cell)