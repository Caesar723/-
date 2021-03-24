from tkinter import*
import random
def Yes():
    love.config(text="我也喜欢你")
def No():
    no.place(x=random.randint(10,280),y=random.randint(10,280))

window=Tk()
window.title("surprise")
window.geometry("300x300+700+300")
love=Label(window,width=10,height=10,text="你喜欢我吗")
love.place(x=100,y=30)
yes=Button(window,text="喜欢!",width=10,command=Yes)
yes.place(x=50,y=190)
no=Button(window,text="不喜欢",width=10,command=No)
no.place(x=150,y=190)
window.mainloop()