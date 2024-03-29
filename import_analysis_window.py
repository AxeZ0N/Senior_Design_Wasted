## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##


## Sub-menu import ##
import generate_plot
from import_viewer import import_viewer
## Sub-menu import ##


## Class: Import Analysis ##
## input: Welcome Window Root Window ##
##        FROM WELCOME_WINDOW.PY ##
## output: Analysis window -> Cell, Machines, Sub Machines -> Plot ##
class import_analysis:

    
    def __init__(self, root):
        ## Boilerplate window generation, don't touch ##
        root.title("Import Analysis Tool: Team 12")                                                                     #Title of window
        self.import_analysis_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.import_analysis_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                            #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                               #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
        ## Boilerplate window generation, don't touch ##

        self.path_to_machine_file = StringVar()

        ## Import splash ##
        ttk.Label(self.import_analysis_mainframe, text="Import Analysis").grid(column=3, row=0, sticky=(N))                  #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
        ## Import splash ##

        ttk.Button(self.import_analysis_mainframe, text="Select File", command=lambda:self.run_import_viewer(root)).grid(column=3, row=3, sticky=N)

        ## Shortcut for padding widgets ##
        for child in self.import_analysis_mainframe.winfo_children():                                                        #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                        #Let each child have padding around edges of padx/y=<pixels>
        ## Shortcut for padding widgets ##

    ## Function: Run Import Viewer ##
    ## input: root window for popup sub-window ##
    ##        FROM IMPORT_ANALYSIS_WINDOW.PY ##
    ## output: popup window to allow selection of file to import ## 
    ##         generates a button to generate plot inside original window ##
    def run_import_viewer(self, root):
        import_viewer(root, self.path_to_machine_file)                                                                                                      #Use my pre-built import previewer, more streamlined
        ttk.Button(self.import_analysis_mainframe, text="Generate Plot", command=lambda:self.generate_plot(root)).grid(column=2, row=3, sticky=N)           ##makes a button on the main window to generate plot. Not needed but it made it simpler to code


    ## Function: Generate Plot ##
    ## input: root window for popup sub-window ##
    ##        FROM IMPORT_ANALYSIS_WINDOW.PY ##
    ## output: popup window with interactive plot ## 
    def generate_plot(self, root):
        generate_plot.generate_plot(root, self.path_to_machine_file)                                                                                           #This is its own function because when I wrote this I was getting tired, doesn't have to be like this
