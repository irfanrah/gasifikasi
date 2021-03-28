from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
#---------End of imports

fig = plt.Figure(figsize = (5,4))

x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,
    
def my_mainloop():
	
	val = random.randint(0,200)
	Tk.Label(master=root, text=val,font=("Helvetica", 25)).place(x = 50, y = 520)
	Tk.Label(master=root, text=val,font=("Helvetica", 25)).place(x = 250, y = 520)
	Tk.Label(master=root, text=val,font=("Helvetica", 25)).place(x = 480, y = 520)
	Tk.Label(master=root, text=val,font=("Helvetica", 25)).place(x = 700, y = 520)
	print(val)
	
	root.after(1000, my_mainloop)

	
	
root = Tk.Tk()
root.geometry("1200x1000")

root.after(1000, my_mainloop)


label = Tk.Label(root,text="Gasification GUI Testing").grid(column=0, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=10, y=30)

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.Label(master=root, text="Blower Hisap" ,font=("Helvetica", 18)).place(x = 10, y = 480)
Tk.Label(master=root, text="Blower Primer" ,font=("Helvetica", 18)).place(x = 210, y = 480)
Tk.Label(master=root, text="Vibrating Grate" ,font=("Helvetica", 18)).place(x = 410, y = 480)
Tk.Label(master=root, text="Screw Feeder" ,font=("Helvetica", 18)).place(x = 660, y = 480)

Tk.mainloop()
