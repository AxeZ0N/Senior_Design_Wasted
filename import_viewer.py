from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from os.path import splitext
import pandas


## Class: Import Viewer ##
## input: window to treat as master ##
##        FROM CELL_CREATION_WINDOW.PY ##
##        FROM IMPORT_ANALYSIS_WINDOW.PY ##
## output: Popup file dialogue for selection, popup preview window yes/no, if yes returns file path, if no returns -1 ##
class import_viewer():

    def __init__(self, root, return_variable):

        ## Boilerplate window generation, don't touch ##
        self.import_viewer_mainframe = ttk.Frame(root, padding="3 3 12 12")                                           #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.import_viewer_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                        #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        self.return_variable = return_variable
        root.columnconfigure(0, weight=1)                                                                            #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
        ## Boilerplate window generation, don't touch ##

        ## Previewing File ##
        raw_input = askopenfilename()                                                                                   #Pandas easy data processing, markdown for portability
        machine_list_df = pandas.read_csv(raw_input)                                                                    
        df_cleaned = machine_list_df.to_markdown()
        ## Previewing File ##

        ## Displaying the file ##
        display_data = Toplevel(self.import_viewer_mainframe)                                                              #TopLevel generates a popup sub-window slave to the root
        ttk.Label(display_data, text=df_cleaned, font=('Courier', 15)).pack()                                              #Courier is a monospaced font so the preview looks nice 
        ttk.Button(display_data, text="Yes", command=lambda:self.return_path_to_file(raw_input)).pack(side="top")          #Packing the buttons automatically places them around the preview, no manual placing in case of resizing 
        ttk.Button(display_data, text="No", command=lambda:self.return_path_to_file("-1")).pack(side="top")
        ## Displaying the file ##

## Function: return path to file ##
## input: path to file ##
##        FROM IMPORT_VIEWER.PY ##
## output: Uses return variable to send back the chosen file path, destroys self after ##
    def return_path_to_file(self, path_to_file):
        self.return_variable.set(path_to_file)                                                                             #Uses the passed return variable, easiest way I know to transfer things between tkinter windows
        self.import_viewer_mainframe.destroy()                                                                             #Destroys the popup window, it's more streamlined to have a sub-window and just close it afterwards




