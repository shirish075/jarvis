from tkinter import *
from tkinter import messagebox

# Set the geometry of frame


window = ''
yon = False


def check():
    global yon
    tex = password.get()
    if tex == "888":
        messagebox.showinfo("Authenticaton Success", "Your password is correct")
        close_win()
        yon = True
    else:
        messagebox.showerror("failed", "please check your password")
        password.delete(0, END)
        yon = 0


def back():
    global password
    password = password.replace(password[-1], "")
    pass_lbl.config(text=password)


def close_win():
    window.destroy()


# Create a text label
def passwordprotect():
    global window
    # Create an instance of tkinter frame
    window = Tk()
    window.title("Jarvis Authetication")
    window.geometry("600x250")
    global password
    password = ""
    global pass_lbl
    pass_lbl = Label
    Label(window, text="Enter the Password", font=('Helvetica', 20)).pack(pady=20)

    # Create Entry Widget for password
    password = Entry(window, show="*", width=20)
    password.pack()

    # Create a button to close the window
    Button(window, text="Quit", font=('Helvetica bold', 10), command=close_win, height=2, width=5, bg="#63d636").place(
        x=350, y=100)
    enter = Button(window, text="enter", font=('Helvetica bold', 10), command=lambda: check(), height=2, width=5,
                   bg="#63d636").place(x=200, y=100)
    window.mainloop()
    return yon
