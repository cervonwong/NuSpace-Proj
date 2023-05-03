# Name: Cervon Wong
# Reference: https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Generates graphs and attaches them to GUI.
def plot_graphs():
    figure = Figure(figsize = (20, 20), dpi = 100)

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.cos(2 * np.pi * x) * np.exp(-x)

    plot1 = figure.add_subplot(221)
    plot1.plot(x, y1, label='sin(x)')
    plot1.legend()

    plot2 = figure.add_subplot(222)
    plot2.plot(x, y2, label='cos(x)')
    plot2.legend()

    plot3 = figure.add_subplot(212)
    plot3.plot(x, y3, '.-', label='Dampened oscillation')
    plot3.legend()
  
    # Create the canvas with the figure and appending it to GUI.
    canvas = FigureCanvasTkAgg(figure, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()

# INITIALISE GUI WINDOW
window = Tk()
window.title('Plots') # Window title.
width = window.winfo_screenwidth()              
height = window.winfo_screenheight()   
window.geometry("%dx%d" % (width, height)) # Set default window size to screen size.
window.state('zoomed') # Maximize window.
window.configure(bg = 'white') # Set background color to white.

# ADD TEXT LABELS
label_title = Label(master = window, text = "Plotting SingStat Graphs with Tkinter in Python", font = ("Arial", 20), bg = 'white')
label_title.pack(pady = 10)
label_details = Label(master = window, text = "Name: Cervon Wong // Environment: Python 3.10 // IDE: VS Code", font = ("Arial", 10), bg = 'white')
label_details.pack()

# PLOT AND DISPLAY GRAPHS
plot_graphs()

# START GUI
window.mainloop()