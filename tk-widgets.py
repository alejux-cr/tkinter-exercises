#!/usr/bin/python3

"""tk widgets examples"""

from tkinter import *
from tkinter import ttk

class SampleApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(master, text = "San Jose",
                   command = self.sj_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Guanacaste",
                   command = self.guana_hello).grid(row = 1, column = 1)

    def sj_hello(self):
        self.label.config(text = 'Hello from SJ, Tkinter!')

    def guana_hello(self):
        self.label.config(text = 'Hello from Guana, Tkinter!')

def main():            
    
    root = Tk()
    app = SampleApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
