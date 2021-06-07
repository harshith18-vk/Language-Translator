from googletrans import Translator,LANGUAGES
from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("1500x600")
root.title("Python Project - Language Translator")
root.config()
Label(root,text="LANGUAGE TRANSLATOR",font="aerial 18 bold",fg="black",bg="white").pack()
Label(root,text="ENTER TEXT",font="aerial 12 bold",bg="white").place(x=230,y=60)
input_text=Text(root,font="aerial 12",width=60,height=11)
input_text.place(x=30,y=100)
Label(root,text="OUTPUT",font="aerial 12 bold",bg="white").place(x=1000,y=60)
output_text=Text(root,font="aerial 12",width=60,height=11)
output_text.place(x=900,y=100)
language=list(LANGUAGES.values())
scr1=ttk.Combobox(root,font="aerial 20",values=language,width=12)
scr1.place(x=10,y=60)
scr1.set("english")
scr2=ttk.Combobox(root,font="aerial 20",value=language,width=12)
scr2.place(x=1150,y=60)
scr2.set("telugu")
def translates():
    translator=Translator()
    translated=translator.translate(text=input_text.get(1.0,END),src=scr1.get(),dest=scr2.get())
    output_text.delete(1.0,END)
    output_text.insert(END,translated.text)

b1=Button(root,text="Translate",bg="red",fg="black",command=translates)

b1.place(x=700,y=300)










root.mainloop()
