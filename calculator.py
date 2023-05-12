# Import tkinter module
import tkinter as tk
ab=tk.Tk()
# Applying required geometry
ab.geometry("400x350")
ab.title("Calculator")
ab.resizable(False,False)
eq=" "
# Define functions for each specifics individually
def show(value):
    global eq
    eq+=value
    label1.config(text=eq)  
def clear():
    global eq
    eq=" "
    label1.config(text=eq) 
def change_sign():
    global eq
    val=int(eq)
    eq=(-val)
    label1.config(text=eq)
def back():
    global eq
    l=[]
    for i in eq:
        l.append(i)    
    l.pop()
    str1=" "
    for j in l:
        str1+=j
    eq=str1
    label1.config(text=eq)   
def calculate():
    global eq
    result=""
    if eq!="":
        try:
            result= eval(eq)
            eq=eval(eq)
        except:
            result="error"
            eq=""
    label1.config(text=result)
label=tk.Label(ab,height=1,text="Standard",font=('Arial',16))
label.pack(anchor='w')
# Giving a label for test input
label1=tk.Label(ab,height=3,text="",font=('Arial',18))
label1.pack(anchor='e')
# Button frame configuration
buttonframe=tk.Frame(ab)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)
# Buttons with required sizes and linking to functions
ac1=tk.Button(buttonframe,text='AC',width=4,height=1,font=('Arial',14),bd=5,bg='blue',fg='white',command=lambda:clear())
ac1.grid(row=0,column=0,sticky=tk.W+tk.E)
clr=tk.Button(buttonframe,text='CLEAR',width=4,height=1,font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:back())
clr.grid(row=0,column=1,sticky=tk.W+tk.E)
sign=tk.Button(buttonframe,text='+/-',width=4,height=1,font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:change_sign())
sign.grid(row=0,column=2,sticky=tk.W+tk.E)
div=tk.Button(buttonframe,text='/',width=4,height=1,font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("/"))
div.grid(row=0,column=3,sticky=tk.W+tk.E)
bt1=tk.Button(buttonframe,text='7',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("7"))
bt1.grid(row=1,column=0,sticky=tk.W+tk.E)
bt2=tk.Button(buttonframe,text='8',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("8"))
bt2.grid(row=1,column=1,sticky=tk.W+tk.E)
bt3=tk.Button(buttonframe,text='9',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("9"))
bt3.grid(row=1,column=2,sticky=tk.W+tk.E)
bt4=tk.Button(buttonframe,text='*',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("*"))
bt4.grid(row=1,column=3,sticky=tk.W+tk.E)
bt5=tk.Button(buttonframe,text='4',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("4"))
bt5.grid(row=2,column=0,sticky=tk.W+tk.E)
bt6=tk.Button(buttonframe,text='5',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("5"))
bt6.grid(row=2,column=1,sticky=tk.W+tk.E)
bt7=tk.Button(buttonframe,text='6',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("6"))
bt7.grid(row=2,column=2,sticky=tk.W+tk.E)
bt8=tk.Button(buttonframe,text='-',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("-"))
bt8.grid(row=2,column=3,sticky=tk.W+tk.E)
bt9=tk.Button(buttonframe,text='1',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("1"))
bt9.grid(row=3,column=0,sticky=tk.W+tk.E)
bt10=tk.Button(buttonframe,text='2',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("2"))
bt10.grid(row=3,column=1,sticky=tk.W+tk.E)
bt11=tk.Button(buttonframe,text='3',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("3"))
bt11.grid(row=3,column=2,sticky=tk.W+tk.E)
bt12=tk.Button(buttonframe,text='+',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("+"))
bt12.grid(row=3,column=3,sticky=tk.W+tk.E)
bt13=tk.Button(buttonframe,text='%',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("%"))
bt13.grid(row=4,column=0,sticky=tk.W+tk.E)
bt14=tk.Button(buttonframe,text='0',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("0"))
bt14.grid(row=4,column=1,sticky=tk.W+tk.E)
bt15=tk.Button(buttonframe,text='.',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:show("."))
bt15.grid(row=4,column=2,sticky=tk.W+tk.E)
bt16=tk.Button(buttonframe,text='=',font=('Arial',14),bd=5,bg='black',fg='white',command=lambda:calculate())
bt16.grid(row=4,column=3,sticky=tk.W+tk.E)
buttonframe.pack(fill='x')
ab.mainloop()