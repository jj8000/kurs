from tkinter import Tk, Label, Entry, Button

root = Tk()
label_a = Label(master=root, text="Odległość w km: ")
label_a.pack()
a = Entry(master=root)
a.pack()


label_b = Label(master=root, text="Spalanie w l/100km: ")
label_b.pack()
b = Entry(master=root)
b.pack()

label_c = Label(master=root, text="Koszt paliwa w zł: ")
label_c.pack()
c = Entry(master=root)
c.pack()

def consumption():
    a_value = float(a.get())
    b_value = float(b.get())
    c_value = float(c.get())
    wynik.configure(text=f"Spalanie: {a_value * b_value / 100:.2f} l\nKoszt: {a_value * b_value * c_value/ 100:.2f} zł")

sum_button = Button(master=root, text="Oblicz zużycie\n paliwa i koszt podróży", command=consumption)
sum_button.pack()

wynik = Label(master=root, text="")
wynik.pack()

root.mainloop()