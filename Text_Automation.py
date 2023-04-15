from pyautogui import *
from tkinter import *
import time
master=Tk()
master.config(bg="#1E90FF")
master.geometry("850x450+600+200")
master.title("Prank your friend")
Label(master,text='  ',bg="#1E90FF").pack()
Label(master,text="Multi-Message Prank",font=('Times new Roman',25,'italic','bold'),bg="#1E90FF").pack()
Label(master,text='  ',bg="#1E90FF").pack()
root=Frame(master,highlightbackground="white", highlightthickness=3,padx=50,pady=50)
root.pack()
root.configure(background="#ADD8E6")
Label(root,text="Enter text to be sent",bg="#ADD8E6",font=('Times new Roman',20)).grid(row=0,column=0,sticky='w')
Label(root,text="     ",bg="#ADD8E6",font=('Times new Roman',20)).grid(row=0,column=1,sticky='w')
print_text=StringVar()
Entry(root,font=('Times new Roman',15),textvariable=print_text).grid(row=0,column=2,sticky='w')
Label(root,text="Number of times to send",bg="#ADD8E6",font=('Times new Roman',20)).grid(row=1,column=0,sticky='w')
n=StringVar()
Entry(root,font=('Times new Roman',15),textvariable=n).grid(row=1,column=2,sticky='w')
accept=IntVar()
Checkbutton(root,text="Click here if you want to add",bg="#ADD8E6",variable=accept,font=('Times new Roman',15)).grid(row=3,column=0)
Label(root,text="count along",bg="#ADD8E6",font=('Times new Roman',15)).grid(row=3,column=1,sticky='w')
Label(root,text="with the text",bg="#ADD8E6",font=('Times new Roman',15)).grid(row=3,column=2,sticky='w')
def submission():
    global n
    if print_text.get()!='' and n.get()!='':
        try:
            n=int(n.get())
            master.destroy()
            time.sleep(4)
            if accept.get()==0:
                for i in range(n):
                    write(print_text.get())
                    press("enter")
            elif accept.get()==1:
                for i in range(n):
                    write(str(i+1))
                    write(": ")
                    write(print_text.get())
                    press("enter")
        except:
            Label(root,text="Please enter a Whole number",bg="#ADD8E6",font=('Times new Roman',15),fg='red').grid(row=2,column=0,sticky='w')
    else:
        Label(root,text="***Please fill the details***",bg="#ADD8E6",font=('Times new Roman',15),fg='red').grid(row=2,column=0,sticky='w')
Button(root,text="Submit",font=('Times new Roman',15),command=submission).grid(row=4,column=1)
master.mainloop()