from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from os.path import splitext
import pandas

from import_viewer import csv_read

class import_viewer():

    ## Boilerplate window generation, don't touch ##
    def __init__(self, root, return_variable):                                                                                   #Title of window
        self.import_viewer_mainframe = ttk.Frame(root, padding="3 3 12 12")                                           #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.import_viewer_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                        #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        self.return_variable = return_variable
        root.columnconfigure(0, weight=1)                                                                            #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##

        raw_input = askopenfilename()

        machine_list_df = pandas.read_csv(raw_input)
        df_cleaned = machine_list_df.to_markdown()
        display_data = Toplevel(self.import_viewer_mainframe)
        ttk.Label(display_data, text=df_cleaned, font=('Courier', 15)).pack()
        ttk.Button(display_data, text="Yes", command=lambda:self.return_path_to_file(raw_input)).pack(side="top")
        ttk.Button(display_data, text="No", command=lambda:self.return_path_to_file("-1")).pack(side="top")

    def return_path_to_file(self, path_to_file):
        self.return_variable.set(path_to_file)
        self.import_viewer_mainframe.destroy()




