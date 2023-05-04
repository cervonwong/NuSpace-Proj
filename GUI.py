# Name: Cervon Wong
# Reference: https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd

# Variables
graph_index = 0
figure = Figure(figsize=(20, 20), dpi=100)
plot = figure.add_subplot(111)

def show_next_graph():
    global graph_index
    if (graph_index == 0):
        plot_graph_0()
    elif (graph_index == 1):
        plot_graph_1()
    elif (graph_index == 2):
        plot_graph_2()
    graph_index = (graph_index + 1) % 3

def plot_graph_0():
    # 0. PLOT OF HOTEL REVENUE AGAINST TIME (YEARS)
    HR_arr = np.loadtxt(
        "HotelRevenue.csv", delimiter=",", dtype=str)
    HR_years = pd.to_datetime(HR_arr[0, 1:], format='%Y %b ')
    HR_revenue = HR_arr[1, 1:].astype(float)

    plot.clear()
    plot.plot(HR_years, HR_revenue, label='Hotel revenue against time')
    plot.set_xlabel('Year')
    plot.set_ylabel('Revenue ($SGD)')
    plot.title.set_text('Hotel revenue against time')
    plot.axhline(y=HR_revenue.min(), color='r', linestyle='--')
    plot.text(pd.to_datetime("2008"), HR_revenue.min()+8000, 'Minimum revenue: $' +
               str(HR_revenue.min()), color='r')
    plot.axhline(y=HR_revenue.max(), color='g', linestyle='--')
    plot.text(pd.to_datetime("2008"), HR_revenue.max()-18000, 'Maximum revenue: $' +
                str(HR_revenue.max()), color='g')
    # Draw a big red arrow with a downwards line in Year 2021.
    plot.annotate('Covid-19', xy=(pd.to_datetime("2021"), 150000), xytext=(pd.to_datetime("2021"), 350000),
                     arrowprops=dict(facecolor='red', shrink=0.05), color='r')
    canvas.draw()
                     

def plot_graph_1():
    # 1. PLOT OF TYPES OF RESIDENT HOUSEHOLDS
    RH_arr = np.loadtxt("ResidentHouseholds.csv", delimiter=",", dtype=str)
    RH_categories = ("1", "2", "3", "4", "5", "6+")
    RH_HDB = RH_arr[3, 5::4].astype(int)
    RH_Condo = RH_arr[8, 5::4].astype(int)

    RH_index = np.arange(6)
    bar_width = 0.35

    plot.clear()
    plot.bar(RH_index, RH_HDB, bar_width, label = "HDB flats", color='purple')
    plot.bar(RH_index + bar_width, RH_Condo, bar_width, label="Condominiums", color='orange')
    plot.set_xlabel('Household size (persons)')
    plot.set_ylabel('Number of households')
    plot.legend()
    plot.set_xticks(RH_index + bar_width/2, RH_categories)
    plot.text(1, RH_HDB.max(), 'Max: ' + str(RH_HDB.max()), color='purple', bbox=dict(facecolor='white', edgecolor='white', alpha=0.7, boxstyle='round,pad=0'))
    plot.text(3, RH_Condo.max(), 'Max: ' + str(RH_Condo.max()), color='brown', bbox=dict(facecolor='white', edgecolor='white', alpha=0.7, boxstyle='round,pad=0'))
    plot.text(5, RH_HDB.min(), 'Min: ' + str(RH_HDB.min()), color='purple', bbox=dict(facecolor='white', edgecolor='white', alpha=0.7, boxstyle='round,pad=0'))
    plot.text(5, RH_Condo.min(), 'Min: ' + str(RH_Condo.min()), color='brown', bbox=dict(facecolor='white', edgecolor='white', alpha=0.7, boxstyle='round,pad=0'))
    plot.title.set_text('Number of households by size and type')
    canvas.draw()

def plot_graph_2():
    # 3. NEW PROBATION CASES OVER TIME
    NP_arr = np.loadtxt("NewProbation.csv", delimiter=",", dtype=str)
    NP_years = pd.to_datetime(NP_arr[0, 1:], format='%Y ')
    NP_cases = NP_arr[1, 1:].astype(int)

    plot.clear()
    plot.plot(NP_years, NP_cases, '.-', color='darkblue')
    plot.set_xlabel('Year')
    plot.set_ylabel('Number of cases')
    plot.title.set_text('New probation cases over time')
    plot.axhline(y=NP_cases.max(), color='r', linestyle='--')
    plot.text(pd.to_datetime("2014"), NP_cases.max()-40, 'Maximum cases: ' +
                str(NP_cases.max()), color='r')
    plot.axhline(y=NP_cases.min(), color='g', linestyle='--')
    plot.text(pd.to_datetime("2003"), NP_cases.min()+30, 'Minimum cases: ' +
                str(NP_cases.min()), color='g')
    canvas.draw()


# INITIALISE GUI WINDOW
window = Tk()
window.title('Plots')  # Window title.
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# Set default window size to screen size.
window.geometry("%dx%d" % (width, height))
window.state('zoomed')  # Maximize window.
window.configure(bg='white')  # Set background color to white.

# ADD TEXT LABELS
label_title = Label(master=window, text="Plotting SingStat Graphs with Tkinter in Python", font=(
    "Arial", 20), bg='white')
label_title.pack(pady=10)
label_details = Label(
    master=window, text="Name: Cervon Wong // Environment: Python 3.10 // IDE: VS Code", font=("Arial", 10), bg='white')
label_details.pack()

# CREATE BUTTON AND LOGIC
button = Button(master=window, text="Next graph", command=show_next_graph, font=("Arial", 15))
button.pack(pady=10)

# Create the canvas with the figure and append it to GUI.
canvas = FigureCanvasTkAgg(figure, master=window)
show_next_graph() # Show the first graph.
canvas.draw()
canvas.get_tk_widget().pack()

# START GUI
window.mainloop()
