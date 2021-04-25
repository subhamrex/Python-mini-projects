from tkinter import *


def click(event):
    global scan_value
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scan_value.get().isdigit():
            value = int(scan_value.get())
        else:
            try:
                value = eval(screen.get())
            except:
                value = "Error"
        scan_value.set(value)
        screen.update()
    elif text == "C":
        scan_value.set("")
        screen.update()
    elif text == "Exit":
        scan_value.set("")
        screen.quit()
    else:
        scan_value.set(scan_value.get() + text)
        screen.update()


root = Tk()
root.geometry("310x590")
root.title("Calculator")
root.wm_iconbitmap("1.ico")

scan_value = StringVar()
scan_value.set("")
screen = Entry(root, textvar=scan_value, font="lucida 40 bold", bg="#FBC088")
screen.pack(fill=X, padx=10, pady=10)

others0 = ["C", "%", "Exit"]
color0 = ["#67CB89", "#F9D85B", "#7861AB"]
f1 = Frame(root, bg="#36454F")
for i in range(len(others0)):
    b1 = Button(f1, text=f"{others0[i]}", padx=15, pady=15, font="lucida 15 bold", bg=f"{color0[i]}")
    b1.pack(side=LEFT, padx=18, pady=18)
    b1.bind("<Button-1>", click)
f1.pack()

others1 = ["+", "*", "-"]
color_op = ["#8FB48E", "#EBC16A", "#564BF7"]
for j in range(3, 0, -1):
    f1 = Frame(root, bg="#36454F")
    n = j * 3
    for i in range(n, n - 3, -1):
        b1 = Button(f1, text=f"{i}", padx=15, pady=15, font="lucida 15 bold")
        b1.pack(side=LEFT, padx=10, pady=10)
        b1.bind("<Button-1>", click)

    b1 = Button(f1, text=f"{others1[j - 1]}", padx=15, pady=15, font="lucida 20 bold", bg=f"{color_op[j - 1]}")
    b1.pack(side=LEFT, padx=10, pady=10)
    b1.bind("<Button-1>", click)
    f1.pack()

others2 = [0, ".", "=", "/"]
color_op2 = ["white", "#E43741", "#D04515", "#9D96D7"]
f1 = Frame(root, bg="#36454F")
for i in range(len(others2)):
    b1 = Button(f1, text=f"{others2[i]}", padx=10, pady=10, font="lucida 20 bold", bg=f"{color_op2[i]}")
    b1.pack(side=LEFT, padx=13, pady=13)
    b1.bind("<Button-1>", click)
f1.pack()

root.resizable(False, False)
root.mainloop()
