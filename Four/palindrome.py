import tkinter as tk
def data():
    v=entry.get()[::-1] .lower()
    return v
def theta():
    q=entry.get().lower()
    return q
def checking():
    if  data()==theta():
                        lab2.configure(text="Its a Palindrome")
    else:
        lab2.configure(text="Not a Palindrome")
w=tk.Tk()
w.title("Palindrome Checker")
w.geometry("500x500")
w.resizable(False,False)
w.configure(background="black")
lab=tk.Label(w,text="Palindrome Checker")
lab.pack(side="top")
lab.configure(bg="black",fg="white",font=('Comic Sans',25,'bold','underline','italic'))
entry=tk.Entry(w)
entry.pack()
entry.configure(bg="blue",fg="white",font=('Comic Sans',25,'bold','underline','italic'))
button=tk.Button(w,text="Check",command=checking,font=('Vani',15,'italic'))
button.pack()
lab2=tk.Label(w,text="",font=('Comic sans Ms',25,'underline'))
lab2.pack()



w.mainloop()