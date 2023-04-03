import tkinter as tk
import webbrowser as wb

def Show():
    msg = e1.get()

    if msg == 'Something':
        wb.open('https://www.youtube.com/watch?v=xm3YgoEiEDc')
        window.destroy()
    else:
        window.destroy()

window = tk.Tk()
window.title('Appication')
window.geometry('500x500')
window.resizable(False, False)
window.config(bg='white')

label1 = tk.Label(text=('Say Something'), font=('Angsana New', 30, 'bold'), fg='black', bg='#ffffff')
label1.place(x=160, y=100)

e1 = tk.Entry(font=('Angsana New', 15, 'bold'))
e1.place(x=160, y=160)

btn1 = tk.Button(text='confirm',font=('Angsana New', 15, 'bold'), fg='black', command=Show)
btn1.place(x=160, y=200)

window.mainloop()