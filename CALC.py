from tkinter import *
import math

s = Tk()
s.title("CALCULATOR")

def frame_maker(root, side):
    temp = Frame(root)
    temp.pack(side=side, expand=YES, fill=BOTH)
    return temp

def button_maker(root, text, command):
    temp = Button(root, text=text, command=command, width=6, height=1, bg="gray60", fg="black", font=("arial", 17, "bold"))
    #temp.pack(expand=YES, fill=BOTH)
    return temp

def calc(w):
    try:
        w.set(eval(w.get()))
    except:
        w.set("Error")

def tri_func(w, part="sin"):
    try:
        if radio.get() == 2:
            temp = (float(w.get())*math.pi)/180
        else:
            temp = float(w.get())
        if part == "sin":
            w.set(math.sin(temp))
        elif part == "cos":
            w.set(math.cos(temp))
        elif part == "tan":
            w.set(math.tan(temp))
        elif part == "fact":
            w.set(math.factorial(temp))
    except:
        w.set("Error")

def radio_change(v):
    if v == 2:
        label_rad.config(text="DEG")
    else:
        label_rad.config(text="RAD")

object_list = ["123", "456", "789"]
if __name__ == "__main__":
    flag = 0
    s = Frame(bg="gray30")
    s.pack(expand=YES, fill=BOTH)
    display = StringVar()
    radio = IntVar()
    disp = Entry(s, textvariable=display, font=("arial", 13))
    disp.pack(side=TOP, expand=YES, fill=BOTH)
    frame_0 = frame_maker(s, TOP)
    frame_1 = frame_maker(s, TOP)
    frame_2 = frame_maker(s, TOP)
    frame_3 = frame_maker(s, TOP)
    frame_4 = frame_maker(s, TOP)
    frame_5 = frame_maker(s, TOP)
    frame_7 = frame_maker(s, TOP)
    frame_6 = frame_maker(s, TOP)
    radio_1 = Radiobutton(frame_0, variable=radio, text="RAD", value=1, command=lambda: radio_change(1))
    radio_1.pack(anchor=W)
    radio_1.select()
    radio_2 = Radiobutton(frame_0, variable=radio, text="DEG", value=2, command=lambda: radio_change(2))
    radio_2.pack(anchor=W)
    label_rad = Label(frame_0, text="RAD", fg="red", font=("arial", 10, "bold"))
    label_rad.pack(anchor=W)
    button_1 = button_maker(frame_1, "1", lambda w=display: w.set(w.get()+"1")).grid(row=1, column=1)
    button_2 = button_maker(frame_1, "2", lambda w=display: w.set(w.get()+"2")).grid(row=1, column=2)
    button_3 = button_maker(frame_1, "3", lambda w=display: w.set(w.get()+"3")).grid(row=1, column=3)
    button_pi = button_maker(frame_1, "π", lambda w=display: w.set(w.get()+str(math.pi))).grid(row=1, column=4)

    button_4 = button_maker(frame_2, "4", lambda w=display: w.set(w.get()+"4")).grid(row=2, column=1)
    button_5 = button_maker(frame_2, "5", lambda w=display: w.set(w.get()+"5")).grid(row=2, column=2)
    button_6 = button_maker(frame_2, "6", lambda w=display: w.set(w.get()+"6")).grid(row=2, column=3)
    button_e = button_maker(frame_2, "e", lambda w=display: w.set(w.get()+str(math.e))).grid(row=2, column=4)

    button_7 = button_maker(frame_3, "7", lambda w=display: w.set(w.get()+"7")).grid(row=3, column=1)
    button_8 = button_maker(frame_3, "8", lambda w=display: w.set(w.get()+"8")).grid(row=3, column=2)
    button_9 = button_maker(frame_3, "9", lambda w=display: w.set(w.get()+"9")).grid(row=3, column=3)
    button_15 = button_maker(frame_3, "=", lambda w=display: calc(w)).grid(row=3, column=4, rowspan=2)

    button_10 = button_maker(frame_5, "+", lambda w=display: w.set(w.get()+"+")).grid(row=5, column=1)
    button_11 = button_maker(frame_5, "-", lambda w=display: w.set(w.get()+"-")).grid(row=5, column=2)
    button_12 = button_maker(frame_5, "/", lambda w=display: w.set(w.get()+"/")).grid(row=5, column=3)
    button_pow = button_maker(frame_5, "*", lambda w=display: w.set(w.get()+"*")).grid(row=5, column=4)

    button_13 = button_maker(frame_4, "^", lambda w=display: w.set(w.get()+"**")).grid(row=4, column=1)
    button_14 = button_maker(frame_4, "0", lambda w=display: w.set(w.get()+"0")).grid(row=4, column=2)
    button_dot = button_maker(frame_4, ".", lambda w=display: w.set(w.get() + ".")).grid(row=4, column=3)
    button_16 = button_maker(frame_4, "CLEAR", lambda w=display: w.set("")).grid(row=4, column=4)

    button_sin = button_maker(frame_7, "sin", lambda w=display: tri_func(w, "sin")).grid(row=6, column=1)
    button_cos = button_maker(frame_7, "cos", lambda w=display: tri_func(w, "cos")).grid(row=6, column=2)
    button_tan = button_maker(frame_7, "tan", lambda w=display: tri_func(w, "tan")).grid(row=6, column=3)
    button_fact = button_maker(frame_7, "fact", lambda w=display: tri_func(w, "fact")).grid(row=6, column=4)

    label_1 = Label(s, text="ITMO University, group P3177 Salov D. (2016)")
    label_1.pack(side=TOP, expand=YES, fill=BOTH)
    s.mainloop()
