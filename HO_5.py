import tkinter as tk
window = tk.Tk()
window.configure(bg="blue")
window.title("Enrile_Exam")

def signin():
    win = tk.Toplevel(window)

    user = tk.Entry(win)
    user.pack()
    user.insert(0,"username")

    password =tk.Entry(window, show = "*")
    password.pack()
    password.insert(0,"password")

    show = tk.IntVar()
    def toggle():
        if show.get() == 1:
            password["show"] = ""
        else:
            password["show"] = "*"

    tk.checkbutton(window, text="show password",variable = show, command = toggle ).pack()

    
    window.mainloop()

