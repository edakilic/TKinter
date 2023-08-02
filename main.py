import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=300,height=300)

def click_button():
    user_input = my_entry.get()
    print(user_input)

#my_label
my_label = tkinter.Label(text="this is a my_label")
#my_label.config(bg="purple",fg="white")
#my_label.pack()
#my_label.place(x=0, y=0) -> tam olarak konum

#my_button
my_button=tkinter.Button(text="this is a my_button",command=click_button)
my_button.pack()

#entry
my_entry = tkinter.Entry(width=30)
my_entry.pack()

window.mainloop()
