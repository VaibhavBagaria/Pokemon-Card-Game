from tkinter import *l,;[[p[]]
import random 
from PIL import ImageTk,Image
root=Tk()
root.title('Pokemon Card Game')
root.geometry('800x700')
root.configure(background="lightblue")
img=ImageTk.PhotoImage(Image.open("button.jpg"))

abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))

finish=ImageTk.PhotoImage(Image.open("End.jpg"))

title_label=Label(root,text="Pokemon Card Game",bg="lightblue",fg="orange")

P1_label=Label(root,text="Player 1", bg="lightblue",fg="blue")
P2_label=Label(root,text="Player 2",bg="lightblue",fg="Blue")

P1S_label=Label(root,bg="blue",fg="yellow")
P2S_label=Label(root,bg="blue",fg="yellow")

status_label=Label(root)

P1_Score=0
P2_Score=0

P1_Check=0
P2_Check=0

Pokemon_card_names=[abra,bulbasour,charmender,Iyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu,ratata,squirtle]
Pokemon_power=[30,60,50,100,70,70,60,90,40,70,200,40,50]
def rolldice1():
    global P1_Score
    global P1_Check
    random_number=random.randint(0, 12)
    
    random_pokemon=Pokemon_card_names[random_number]
    random_power=Pokemon_power[random_number]
    P1_Score=P1_Score+random_power
    
    status_label['image']=random_pokemon
    P1S_label['text']=P1_Score
    
    P1_Check+P1_Check+1
    
def rolldice2():
    global P2_Score
    global P2_Check
    random_number=random.randint(0, 12)
    
    random_pokemon=Pokemon_card_names[random_number]
    random_power=Pokemon_power[random_number]
    P2_Score=P2_Score+random_power
    
    status_label['image']=random_pokemon
    P2S_label['text']=P2_Score
    
    P1_Check+P1_Check+1

button_P1=Button(root,image=img,command=rolldice1)
button_P2=Button(root,image=img,command=rolldice2)

title_label.place(relx=0.5,rely=0.05,anchor=CENTER)

P1_label.place(relx=0.2,rely=0.3,anchor=CENTER)
P2_label.place(relx=0.8,rely=0.3,anchor=CENTER)

P1S_label.place(relx=0.2,rely=0.4,anchor=CENTER)
P2S_label.place(relx=0.8,rely=0.4,anchor=CENTER)

status_label.place(relx=0.5,rely=0.4,anchor=CENTER)

button_P1.place(relx=0.2,rely=0.6,anchor=CENTER)
button_P2.place(relx=0.8,rely=0.6,anchor=CENTER)

root.mainloop()