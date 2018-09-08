
# coding: utf-8

# ### Logistic Map

# In[42]:


from Tkinter import *
from random import randint
 
# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading
import numpy as np
continuePlotting = False
points = 40 # No of points in the x-axis


def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True

def logistic_map(A,x0):
    x1 = A * x0 * (1 - x0)
    return x1
def data_points(A,x0, points):
    
    x = []
    # value is between  0 < A < 4 
    
    for iter in range(0,points):
        x.append(x0)
        xn = logistic_map(A,x0)
        x0 = xn
    return x

def app():
    # initialise a window.
    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")
    axis_font = { 'size':'14'}
    
    lab = Label(root, text="Live Plotting", bg = 'white').pack()
    
    fig = Figure()
    
    ax = fig.add_subplot(111)
    ax.set_xlabel('n - Time steps',**axis_font)
    ax.set_ylabel('x(n)',**axis_font)
   
    ax.grid()
    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)
   
 
    def plotter():
        
            axis_font = { 'size':'20'}
            ax.cla()
            ax.grid()
            
            x = data_points(w2.get(),w1.get(), points)
            n = np.linspace(0,points,points)
            ax.plot(n,x, marker='o', color='orange')
            ax.set_xlabel('n - Time steps',**axis_font)
            ax.set_ylabel('x(n)',**axis_font)
            ax.set_title(r'Discrete Time Logistic map $x_( n+1 ) = A * x_( n ) (1 - x_( n ))$',size = 18)
            graph.draw()
            time.sleep(0.1)
        
    def gui_handler():
        change_state()
        threading.Thread(target=plotter()).start()
 
    b = Button(root, text="Plot", command=gui_handler, bg="red", fg="white")
    b.pack()
    w1 = Scale(root, from_=0, to= 1,resolution=0.0001,tickinterval=0.5,length=300, orient=HORIZONTAL)
    w1.set(0.01)
    w1.pack()
    w2 = Scale(root, from_=0, to= 4,resolution=0.0001,tickinterval=0.5,length=800, orient=HORIZONTAL)
    w2.set(1)
    w2.pack()
    
    root.mainloop()
 
if __name__ == '__main__':
    app()
    
## Note: In the GUI the scroll bar varying from [0,4] is the value of A and scroll bar varying from [0,1] 
##is the intial value range

