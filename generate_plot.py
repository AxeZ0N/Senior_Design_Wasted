## GUI library import ##
from importlib.resources import path
from tkinter import *
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
  
## GUI library import ##

class generate_plot():

    ## Boilerplate window generation, don't touch ##
    def __init__(self, root, path_to_machine_file):
        root.title("Existing Cell Import")                                                                                    #Title of window
        self.generate_plot_mainframe = ttk.Frame(root, padding="3 3 12 12")                                                               #distance from edge of window: padding=<pixels_top pixels_bottom pixels_left pixels_right>
        self.generate_plot_mainframe.grid(column=0, row=0, sticky=(N, W, E, S))                                                           #Grid == ROWxCOL assignment; sticky=Cardinal directions for alignment within grid
        root.columnconfigure(0, weight=1)                                                                                           #When resizing window, this has a priority of one
        root.rowconfigure(0, weight=1)
    ## Boilerplate window generation, don't touch ##

        my_plot = Toplevel(self.generate_plot_mainframe)
        self.path_to_machine_file = path_to_machine_file
        self.plot(my_plot)



# plot function is created for 
# plotting the graph in 
# tkinter window
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
