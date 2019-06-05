#!/usr/bin/python3

"""Feedback form for the Chirripó National Park in Costa Rica using tkinter by Alejandro Castillo (alejux)"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class FeedbackForm:

    def __init__(self,master):
        master.title('Chirripo Park Feedback')
        master.resizable(False, False)
        master.configure(background = '#399090')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#399090')
        self.style.configure('TButton', background = '#399090')
        self.style.configure('TLabel', background = '#399090',font =('Arial',11))
        self.style.configure('Header.TLabel',font =('Arial',18,'bold'))

        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        self.logo = PhotoImage(file = 'chirripo-logo.gif')
        ttk.Label(self.header_frame, image = self.logo).grid(row=0,column=0,rowspan=2)
        ttk.Label(self.header_frame, text = 'Thanks for visiting Chirripó!',style='Header.TLabel').grid(row=0,column=1)
        ttk.Label(self.header_frame, wraplength=300, text = 
        'We appreciate all kind of feedback for enhancing the Chirripó experience!').grid(row=1,column=1)

        self.form_frame = ttk.Frame(master)
        self.form_frame.pack()

        ttk.Label(self.form_frame, text = 'Name:').grid(row=0,column=0,padx=5,sticky='sw')
        ttk.Label(self.form_frame, text = 'Email:').grid(row=0,column=1,padx=5,sticky='sw')
        ttk.Label(self.form_frame, text = 'Comments:').grid(row=2,column=0,padx=5,sticky='sw')

        self.name_input = ttk.Entry(self.form_frame, width=24,font =('Arial',10))
        self.email_input = ttk.Entry(self.form_frame, width=24,font =('Arial',10))
        self.comments_input = Text(self.form_frame, width=50, height=10,font =('Arial',10))

        self.name_input.grid(row=1,column=0,padx=5)
        self.email_input.grid(row=1,column=1,padx=5)
        self.comments_input.grid(row=3,column=0,columnspan=2,padx=5)

        ttk.Button(self.form_frame, text='Submit',command=self.submit).grid(row=4,column=0,padx=5,sticky='e')
        ttk.Button(self.form_frame, text='Clear',command=self.clear).grid(row=4,column=1,padx=5,sticky='w')

    def submit(self):

        print('Name: {}'.format(self.name_input.get()))
        print('Email: {}'.format(self.email_input.get()))
        print('Comments: {}'.format(self.comments_input.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Chirripó Feedback', message = 'Comments Submitted!')

    def clear(self):
       
        self.name_input.delete(0, 'end')
        self.email_input.delete(0, 'end')
        self.comments_input.delete(1.0, 'end')

def main():            
    
    root = Tk()
    feedbackForm = FeedbackForm(root)
    root.mainloop()
    
if __name__ == "__main__": main()