import randfacts # pip install randfacts
from tkinter import *


def get_fact():
    t1.delete('1.0',END)
    f = randfacts.get_fact(False)
    t1.insert(END,f)


root = Tk()
root.geometry('500x200')
root.title('РАНДОМНЫЕ ФАКТЫ')
root.resizable(False,False)

t1 = Text(root,width=60,height=2,font='Arial 15 bold',padx=10,pady=10,wrap=WORD)
t1.pack(pady=10)

btn = Button(root,text='Сгенерировать факт',font='Arial 13 bold',command=get_fact)
btn.pack(padx=5,pady=10)


root.mainloop()