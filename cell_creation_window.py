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
        self.cell_name = cell_name
        self.path_to_machine_file = StringVar()

        root.title("Config Tool")                                                                                    #Title of window
        self.config_tool_mainframe = ttk.Frame(root, padding="3 3 12 12")                                            #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.config_tool_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                        #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                            #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)

        self.my_cell = simulation_classes.Cell(0, cell_name)

        ttk.Button(self.config_tool_mainframe, text=self.my_cell.getName(), 
            command=lambda:self.run_import_viewer(root)).grid(column=2, row=2, sticky=N)

        ttk.Label(self.config_tool_mainframe, text="Click cell to enter machines from file").grid(column=2, row=0, sticky=(N))                                                      #Label is a widget and can be assigned position inside root window with Grid=<ROWxCOL>, alignment

    ## Shortcut for padding widgets ##
        for child in self.config_tool_mainframe.winfo_children():                                                                       #Each child of the root window is indexed
            child.grid_configure(padx=5, pady=5)                                                                                    #Let each child have padding around edges of padx/y=<pixels>
    ## Shortcut for padding widgets ##

    def generate_machines(self):

        list_of_machines = []

        machine_names = pandas.read_csv(self.path_to_machine_file.get())["Name"]

        for name in machine_names:
            my_machine = simulation_classes.Machine(0, name)
            list_of_machines.append(my_machine)
            self.my_cell.addMachine(my_machine)

        for machine in list_of_machines:
            gen_button = ttk.Button(self.config_tool_mainframe, text=str(machine.getName())).grid(column=1, sticky=(E))



    def run_import_viewer(self, root):
        import_viewer.import_viewer(root, self.path_to_machine_file)

        machine_generate_button = ttk.Button(self.config_tool_mainframe, text="Click to generate machines", 
            command=lambda:self.generate_machines(machine_generate_button)).grid(column=3, row=2, sticky=N)