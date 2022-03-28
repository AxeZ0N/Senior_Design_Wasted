## GUI library import ##
from importlib.resources import path
from tkinter import *
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
## GUI library import ##


## Class: Generate Plot ##
## input: root window to base popup off ##
##        FROM IMPORT_ANALYSIS_WINDOW.PY ##
## output: popup window with interactive plot ##
class generate_plot():

    
    def __init__(self, root, path_to_machine_file):

        ## Boilerplate window generation, don't touch ##
        root.title("Existing Cell Import")                                                                                    #Title of window
        self.generate_plot_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                               #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.generate_plot_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                           #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                           #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
        ## Boilerplate window generation, don't touch ##

        ## Making popup for plot ##
        my_plot = Toplevel(self.generate_plot_mainframe)                                                                    #TopLevel generates a popup sub-window slave to the root
        self.path_to_machine_file = path_to_machine_file                                                                    #Using a return variable is the easiest way I could think of to pass information between tkinter windows
        self.plot(my_plot)                                                                                                  #A separate function to plot the data, should be easier to plot custom data now
        ## Making popup for plot ##



    ## Function: Plot ##
    ## input: root window for popup sub-window ##
    ##        FROM GENERATE_PLOT.PY ##
    ## output: popup window with interactive plot ##

    ##                  WARNING                    ##
    ##        THIS IS A HARDCODED EXAMPLE          ##
    ##        COPY/PASTED FROM GEEKSFORGEEKS       ##
    ## BECAUSE I DON'T KNOW WHAT FILES TO PLOT YET ##

    def plot(self, root):
        
        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5), dpi = 100)
    
        # list of squares
        y = [i**2 for i in range(101)]
    
        # adding the subplot
        plot1 = fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(y)
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = root)  
        canvas.draw()
    
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
    
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
    
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    ##                  WARNING                    ##
    ##        THIS IS A HARDCODED EXAMPLE          ##
    ##        COPY/PASTED FROM GEEKSFORGEEKS       ##
    ## BECAUSE I DON'T KNOW WHAT FILES TO PLOT YET ##