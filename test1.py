from tkinter import*

def printHello():
    print('HI!')

base = Tk()
w = Label(base, text = 'Python Test')
b = Button(base, text = 'Hello Python', command = printHello)
c = Button(base, text = 'Quit', command = base.quit)

w.pack()
b.pack()
c.pack()

base.mainloop()
