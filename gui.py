from tkinter import *
from code import chat
def send():
    msg=EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg!='':
         ChatBox.config(state=NORMAL)
         ChatBox.insert(END,"you:"+msg+'\n\n')
         ChatBox.config(foreground="#446665",font=("Verdana",12))
         ans=chat(msg)
         ChatBox.insert(END,"Bot:"+ans+'\n\n')
         ChatBox.config(state=DISABLED)
         ChatBox.yview(END)
root=Tk()
root.title("THE ELITE")
root.geometry("600x700")
root.resizable(width=FALSE,height=FALSE)
ChatBox=Text(root,bd=0,bg="white",height="8",width="50",font="Arial")
ChatBox.config(state=DISABLED)
scrollbar=Scrollbar(root,command=ChatBox.yview,cursor="heart")
ChatBox['yscrollcommand']=scrollbar.set
SendButton=Button(root,font=("Verdana",12,'bold'),text="Send",width="12"
                                                          ,height=5,bd=0,bg="#f9a602",activebackground="#3c9d9b",fg='#000000',command=send)
EntryBox=Text(root,bd=0,bg="white",width="29",height="5",font="Arial")

scrollbar.place(x=576,y=6,height=620)
ChatBox.place(x=6,y=6,height=620,width=586)
EntryBox.place(x=0,y=640,height=60,width=500)
SendButton.place(x=500,y=640,height=60,width=100)
root.mainloop()
