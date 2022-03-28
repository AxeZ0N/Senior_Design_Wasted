## GUI library import ##
from tkinter import *
from tkinter import ttk
## GUI library import ##

import simulation_classes
import import_viewer
import pandas


## Class: Cell Creation Window ##
## input: New Analysis Root Window ##
##        FROM NEW_ANALYSIS.PY ##
## output: Importer Verification Window -> No user modification needed, manual name entry ##

class cell_creation_window():

    def __init__(self, root, cell_name):
        ## Boilerplate window generation, don't touch ##
        root.title("Config Tool")                                                                                    #Title of window
        self.config_tool_mainframe = ttk.Frame(root, padding="3 3 12 12")                                            #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.config_tool_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                        #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                            #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
        ## Boilerplate window generation, don't touch ##

        ## Internal variables ##
        self.cell_name = cell_name                                                                                  #Lets me use cell name from last page in further pages
        self.path_to_machine_file = StringVar()                                                                     #StringVar lets me pass an argument to another page that returns it back to here

        self.my_cell = simulation_classes.Cell(0, cell_name)                                                        #It's better to have established data structures, so use the simulation classes
        ## Internal variables ##

        ## Buttons, Labels, Widgets ##
        ttk.Button(self.config_tool_mainframe, text=self.my_cell.getName(),                                        
            command=lambda:self.run_import_viewer(root)).grid(column=2, row=2, sticky=N)

        ttk.Label(self.config_tool_mainframe, text="Click cell to enter machines from file").grid(column=2, row=0, sticky=(N))                                                      #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment
        ## Buttons, Labels, Widgets ##

        ## Shortcut for padding widgets ##
        for child in self.config_tool_mainframe.winfo_children():                                                                       #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                                    #Let each child have padding around edges of padx/y=<pixels>
        ## Shortcut for padding widgets ##




    ## Function: Generate Machines ##
    ## input: none ##
    ##        FROM CELL_CREATION_WINDOW.PY ##
    ## output: Generates buttons inside the cell_creation_window window, ## 
    ##         generates machines from simulation classes and adds them to cell ##

    def generate_machines(self):

        list_of_machines = []

        machine_names = pandas.read_csv(self.path_to_machine_file.get())["Name"]                #Extract name column from whatever file they chose, lets me name each machine easily

        for name in machine_names:                                                              #Go through each name in the file they chose and generate a new machine named accordingly
            my_machine = simulation_classes.Machine(0, name)
            list_of_machines.append(my_machine)
            self.my_cell.addMachine(my_machine)                                                 #Add each machine to the cell for later use in more complex functions

        for machine in list_of_machines:
            gen_button = ttk.Button(self.config_tool_mainframe, text=str(machine.getName())).grid(column=1, sticky=(E))     #Generates buttons on the cell_creation_window window dynamically correlating to number of machines in the file
                                                                                                                            #so I don't have to do it manually or open a new window

    ## Function: Run Import Viewer ##
    ## input: Window to base popup window on ##
    ##        FROM CELL_CREATION_WINDOW.PY ##
    ## output: popup window to allow selection of file to import ## 
    ##         generates a button to generate machines inside original window ##
    def run_import_viewer(self, root):
        import_viewer.import_viewer(root, self.path_to_machine_file)                                                        #Call my import viewer function, it's multi-purpose and just gives a formatted preview of their file

        machine_generate_button = ttk.Button(self.config_tool_mainframe, text="Click to generate machines", 
            command=lambda:self.generate_machines(machine_generate_button)).grid(column=3, row=2, sticky=N)                 #makes a button on the main window to generate machines. Not needed but it made it simpler to code