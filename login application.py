from tkinter import *
root=Tk()
root.title('login app')
root.geometry('400x400')
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lbl1=Label(frame,text="full name",bg="#3895D3",fg='white',width=12)
lbl2=Label(frame,text="email id",bg="#3895D3",fg='white',width=12)
lbl3=Label(frame,text="enter password",bg="#3895D3",fg='white',width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")
def display():
        name=name_entry.get()
        greet="hey "+name
        message="\ncongragulations for ur new account!"
        textbox.inser(END,greet)
        textbox.inser(END,message)