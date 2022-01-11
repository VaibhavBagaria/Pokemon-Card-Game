from tkinter import *
import random 
from PIL import ImageTk,Image
root=Tk()
root.title('Pokemon Card Game')
root.geometry('600x600')
root.configure(background="lightblue")
img=ImageTk.PhotoImage(Image.open("button.jpg"))

P1_label=Label(root,text="Player 1", bg="lightblue",fg="blue")
P2_label=Label(root,text="Player 2",bg="lightblue",fg="Blue")

P1S_label=Label(root,bg="blue",fg="yellow")
P2S_label=Label(root,bg="blue",fg="yellow")

status_label=Label(root,)

P1_Score=0
P2_Score=0

def rolldice1():
    global P1_Score

    
def rolldice2():
    global P2_Score


button_P1=Button(root,image=img,command=rolldice1)
button_P2=Button(root,image=img,command=rolldice2)

P1_label.place(relx=0.2,rely=0.3,anchor=CENTER)
P2_label.place(relx=0.8,rely=0.3,anchor=CENTER)

P1S_label.place(relx=0.2,rely=0.4,anchor=CENTER)
P2S_label.place(relx=0.8,rely=0.4,anchor=CENTER)

status_label.place(relx=0.5,rely=0.8,anchor=CENTER)

button_P1.place(relx=0.2,rely=0.6,anchor=CENTER)
button_P2.place(relx=0.8,rely=0.6,anchor=CENTER)

root.mainloop()