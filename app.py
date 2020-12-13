from tkinter import *
from functools import partial
from tkinter import scrolledtext


root = Tk()
root.title("ASR Basic APP")
root.geometry("60x30")


def microcallback(txb):
    import main1
    txb.insert(END, main1.main())

def audiocallback(txb):
    import main2
    txb.insert(END, main2.main())


text = scrolledtext.ScrolledText(root, font="Calibri")


b1 = Button(root, text='Source:Microphone \n(Tap and Speak)', command=partial(microcallback, text), font="Calibri") 
b1.pack(pady=5)


b2 = Button(root, text='Source:Audio_file \n(Tap and Wait)', command=partial(audiocallback, text), font="Calibri") 
b2.pack(pady=5)

text.pack(pady=10)

def clear():
    text.delete(1.0,END)

clear_button = Button(root, text="Clear Screen", command = clear, font="Calibri")
clear_button.pack()


root.mainloop()