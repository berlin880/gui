from tkinter import *
import tkinter as tk
import sys
import os

#start the tkinter
root = tk.Tk()
root.title("Gpa Calculator")

#Lists

grades = []

# Define command

def calculate():
    global grade
    global gpa
    grade = e1.get()
    grade = e2.get()
    grade = e3.get()
    grade = e4.get()
    grade = e5.get()
    grade = e6.get()
    grade = grade.upper()
    grades.append(grade)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e9.delete(0, END)
    total_points=0
    total_hours=0
    total_semester_points = 0
    total_semester_hours = 0
    for n in grades:
        if n == "A+":
            point=12
        elif n == "A":
            point=11.5
        elif n == "A-":
            point=11
        elif n == "B+":
            point=10
        elif n == "B":
            point=9
        elif n == "B-":
            point=8
        elif n == "C+":
            point=7
        elif n == "C":
            point=6
        elif n == "C-":
            point=5
        elif n == "D+":
            point=4
        elif n == "D":
            point=3
        elif n == "F":
            point=0
    total_points += point
    total_hours += 3
    total_semester_points += total_points
    total_semester_hours += total_hours
    gpa=total_semester_points/total_semester_hours
    final_grade = gpa
    if (gpa>4.0):
        e7.delete(0, END)
        e7.insert(0,"ERROR !!")
    else:
        e4.delete(0, END)
        if (final_grade >= 3.6 and final_grade <= 4.0):
            e9.insert(0, "  \"Excellent\"")
        elif (final_grade >= 3.0 and final_grade <= 3.6):
            e9.insert(0, "  \"Very Good\"")
        elif (final_grade >= 2.6 and final_grade <= 3.0):
            e9.insert(0, "  \"GOOD\"")
        elif (final_grade >= 2.0 and final_grade <= 2.6):
            e9.insert(0, "  \"Pass\"")
        else:
            e9.insert(0, "  \"Failed\"")
        e7.insert(0, "%.2f" %gpa)
        e7.insert(0,"GPA = ")
    e1.config(state=DISABLED)
    e2.config(state=DISABLED)
    e3.config(state=DISABLED)
    e4.config(state=DISABLED)
    e5.config(state=DISABLED)
    e6.config(state=DISABLED)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    if __name__ == "__main__":
        restart_program()

def exit():
    sys.exit()

def about():
    top = Toplevel()
    label_about = tk.Label(top, text="Hello My Name Is Abdelrahman Adel").pack()

def first():
    label1.config(text="First Semster")

def second():
    label1.config(text="Second Semster")

def third():
    label1.config(text="Third Semster")

def fourth():
    label1.config(text="Fourth Semster")

def fifth():
    label1.config(text="Fifth Semster")

def sixth():
    label1.config(text="Sixth Semster")

def seventh():
    label1.config(text="Seventh Semster")

def eighth():
    label1.config(text="Eighth Semster")

# Make every thing

frame = tk.LabelFrame(root, padx=10, pady=10)
frame2 = tk.LabelFrame(root, padx=15, pady=15)
frame3 = tk.LabelFrame(root, padx=15, pady=15)

e1 = Entry(frame2, width=5, borderwidth=3)
e2 = Entry(frame2, width=5, borderwidth=3)
e3 = Entry(frame2, width=5, borderwidth=3)
e4 = Entry(frame2, width=5, borderwidth=3)
e5 = Entry(frame2, width=5, borderwidth=3)
e6 = Entry(frame2, width=5, borderwidth=3)
e7 = Entry(frame3, width=10, borderwidth=4)
e8 = Entry(frame3, width=10, borderwidth=4 ,state=DISABLED)
e9 = Entry(frame3, width=10, borderwidth=4)


label1 = tk.Label(frame2, text="First Semster")
label2 = tk.Label(frame2, text="LH135 : ESP 1")
label3 = tk.Label(frame2, text="BA113 : Physics 1")
label4 = tk.Label(frame2, text="BA101 : Calculus 1")
label5 = tk.Label(frame2, text="CS111 : Int. to Computers")
label6 = tk.Label(frame2, text="IS171 : Int. to Information Systems")
label7 = tk.Label(frame2, text="NC172 : Fundmentals Of Business")


button_1 = Button(frame, text="First", padx=20, pady=11, command=first)
button_2 = Button(frame, text="Second", padx=20, pady=11, command=second)
button_3 = Button(frame, text="Third", padx=20, pady=11, command=third)
button_4 = Button(frame, text="Fourth", padx=20, pady=11, command=fourth)
button_5 = Button(frame, text="Fifth", padx=20, pady=11, command=fifth)
button_6 = Button(frame, text="Sixth", padx=20, pady=11, command=sixth)
button_7 = Button(frame, text="Seventh", padx=20, pady=11, command=seventh)
button_8 = Button(frame, text="Eighth", padx=20, pady=11, command=eighth)
button_about = Button(frame3, text="About", padx=30, pady=18, command=about)
button_restart = Button(frame3, text="Calculate Again", padx=30, pady=18, command=restart_program)
button_calculate = Button(root, text="Calculate", padx=50, pady=25, command=calculate)
button_exit = Button(frame3, text="Exit", padx=30, pady=18, command=exit)


# Put all on the screen

button_exit.grid(row=7, column=0, columnspan=2)
button_calculate.grid(row=1, column=1, columnspan=2)
button_1.grid(row=1, column=1, columnspan=1)
button_2.grid(row=1, column=2, columnspan=1)
button_3.grid(row=1, column=3, columnspan=1)
button_4.grid(row=1, column=4, columnspan=1)
button_5.grid(row=2, column=1, columnspan=1)
button_6.grid(row=2, column=2, columnspan=1)
button_7.grid(row=2, column=3, columnspan=1)
button_8.grid(row=2, column=4, columnspan=1)
button_about.grid(row=6, column=0, columnspan=1)
button_restart.grid(row=5, column=0, columnspan=1)


e1.grid(row=1, column=4, padx=10, pady=10)
e2.grid(row=2, column=4, padx=10, pady=10)
e3.grid(row=3, column=4, padx=10, pady=10)
e4.grid(row=4, column=4, padx=10, pady=10, columnspan=1)
e5.grid(row=5, column=4, padx=10, pady=10, columnspan=1)
e6.grid(row=6, column=4, padx=10, pady=10, columnspan=1)
e7.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
e8.grid(row=3, column=0, padx=10, pady=10, columnspan=1)
e9.grid(row=4, column=0, padx=10, pady=10, columnspan=1)


label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
label3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
label4.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
label5.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
label6.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
label7.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

frame.grid(row=1, column=0)
frame2.grid(row=2, column=0)
frame3.grid(row=2, column=1)


root.mainloop()