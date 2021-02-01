from tkinter import *
from translate import Translator
root = Tk()
bg = "green"
root.config(background=bg)

frame = Frame(root, bg=bg)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

heading = Label(frame, text="Translator", bg=bg, font=("Comic Sans MS", 20, 'underline'))
heading.pack()

mid_frame = Frame(frame, bg=bg)
mid_frame.pack()

bottom_frame = Frame(frame, bg=bg)
bottom_frame.pack()

from_label = Label(mid_frame, text="From:  ", bg=bg, font=("Comic Sans MS", 7))
from_label.grid(row=0, column=0)

to_label = Label(mid_frame, text="To:  ", bg=bg, font=("Comic Sans MS", 7))
to_label.grid(row=1, column=0)

enter_text_label = Label(mid_frame, text="Enter Text:  ", bg=bg, font=("Comic Sans MS", 7))
enter_text_label.grid(row=2, column=0)

translation_label = Label(mid_frame, text="Translation:  ", bg=bg, font=("Comic Sans MS", 7))
translation_label.grid(row=3, column=0)

fro = Entry(mid_frame)
fro.grid(row=0, column=1)

to = Entry(mid_frame)
to.grid(row=1, column=1)

text = Entry(mid_frame)
text.grid(row=2, column=1)

translation = Label(mid_frame, text="", bg=bg, fg="yellow", font=("Comic Sans MS", 14))
translation.grid(row=3, column=1)

def submit():
	translation['text'] = ""
	to_language = to.get()
	from_language = fro.get()
	input = text.get()
	translator = Translator(from_lang=from_language, to_lang=to_language)
	result = translator.translate(input)
	translation['text'] = result

submit_button = Button(bottom_frame, text="Submit", bg="sky blue", activebackground="pink", font=("Comic Sans MS", 7), command=submit)
submit_button.pack()

root.mainloop()
