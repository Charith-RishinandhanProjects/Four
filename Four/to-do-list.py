import tkinter as root
rot = root.Tk()
rot.title("To-Do List")
rot.geometry('600x600')
rot.resizable(False, False)
rot.configure(background='blue')
entry=root.Entry(rot,bg='white',fg='black',font=("Courier", 20))
entry.place(x=200, y=50, width=200, height=25)
def com():
          fah=entry.get()
          completed=(f"{fah} is Completed")
          return completed
def add():
    try:
        lost.insert(root.END,entry.get())
    except Exception as ex:
        entry.insert(ex,'enter an task to complete')
def remove():
    lost.delete(root.ACTIVE)
def clear():
    lost.delete(root.ACTIVE)
    lost.insert(root.ACTIVE,com())
label1 = root.Label(rot, text="To-Do List",bg="orange")
label1.pack()

label1.config(font=("Courier", 20))
label1.configure(relief='solid')
b=root.Button(rot, text="Add", command=add,bg='green',fg='black',padx=15,pady=5,activebackground='red',activeforeground='white')
b.place(x=140, y=100)
b=root.Button(rot, text="Remove", command=remove,fg='black',bg='red',padx=15,pady=5,activebackground='orange',activeforeground='white')
b.place(x=220, y=100)
b=root.Button(rot, text="Complete", command=clear,bg='orange',padx=15,pady=5,activebackground='green',activeforeground='white')
b.place(x=320, y=100)
lost=root.Listbox(rot,bg='black',fg='white',font=("Courier", 20))
lost.place(x=1, y=170,width=600,height=200)
root.mainloop()