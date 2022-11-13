from tkinter import Tk, Label, Entry, Button

root = Tk()
label_a = Label(master=root, text="Liczba a: ")
label_a.pack()
a = Entry(master=root)
a.pack()


label_b = Label(master=root, text="Liczba b: ")
label_b.pack()
b = Entry(master=root)
b.pack()

def sum():
    a_value = float(a.get())
    b_value = float(b.get())
    wynik.configure(text=f"{a_value + b_value}")

sum_button = Button(master=root, text="Dodaj", command=sum)
sum_button.pack()

wynik = Label(master=root, text="")
wynik.pack()

root.mainloop()