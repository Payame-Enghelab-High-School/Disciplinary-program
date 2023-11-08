from tkinter import Tk, Entry, Button, Label
root = Tk()

Label(root, text="Search:", bg='white', fg='black', font=('', 10)).place(x=4.5, y=8)
Search_bar = Entry(root, background="#ffe", width=100)
Search_bar.place(x=80, y=10)
Search_btn = Button(root, text="Go!", width=10, height=1, bg="white", fg="black")
Search_btn.place(x=700, y=7)

root.title("نرم افزار انضباطی")
root.resizable(False, False)
root.geometry("800x500")
root.config(bg="#fff")
root.mainloop()