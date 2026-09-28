import math as x
import tkinter as t
import math
root=t.Tk()

pi=math.pi
root.geometry("500x500")
root.title('Calculator')
root.configure(background='black')
root.resizable(False, False)
entry=t.Entry(root,bg='blue'
                      '',fg='white',width=20,)
entry.pack(expand=False,side=t.RIGHT)
entry.configure(font=('Comic Sans',20))
button=t.Button(text='Calculate',activebackground='#FF9F0A',activeforeground='black',command=lambda:calculate())
button.config(bg='#FF9F0A')
button.pack()
button.config(font=('Arial',15))
label=t.Label(root,text='* = Multiplication\n/ = division\n%=Modulus\n**=exponentation or power numbers\nx.sqrt(X)=for performing square root\nx.sin()=for sin and same for cos',bg='black',fg='white',font=('Comic Sans',15))
label.pack()
label1=t.Label(root,bg='#FF9F0A',fg='black',font=('Comic Sans',15))
label1.pack()
def calculate():
    expression=entry.get()
    cal=eval(expression)
    entry.delete(0,'end')
    entry.insert(0,cal)
    label1.config(text=cal)
entry.pack(side=t.TOP)
root.mainloop()