from tkinter import *

# Creating a Tkinter widget
base = Tk()
base.title("Simple Calculator")

# Text entry of the calculator
e = Entry(base, width= 35, borderwidth= 5)
e.grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)

def button_click(number):
    
    current =  e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num 
    global math 
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num 
    global math 
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num 
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_divide():
    first_number = e.get()
    global f_num 
    global math 
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "substraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))


# Defining Buttons
button_1 = Button(base, text= "1", padx= 40, pady= 20, command= lambda: button_click(1))
button_2 = Button(base, text= "2", padx= 40, pady= 20, command= lambda: button_click(2))
button_3 = Button(base, text= "3", padx= 40, pady= 20, command= lambda: button_click(3))
button_4 = Button(base, text= "4", padx= 40, pady= 20, command= lambda: button_click(4))
button_5 = Button(base, text= "5", padx= 40, pady= 20, command= lambda: button_click(5))
button_6 = Button(base, text= "6", padx= 40, pady= 20, command= lambda: button_click(6))
button_7 = Button(base, text= "7", padx= 40, pady= 20, command= lambda: button_click(7))
button_8 = Button(base, text= "8", padx= 40, pady= 20, command= lambda: button_click(8))
button_9 = Button(base, text= "9", padx= 40, pady= 20, command= lambda: button_click(9))
button_0 = Button(base, text= "0", padx= 40, pady= 20, command= lambda: button_click(0))

button_add = Button(base, text= "+", padx= 39, pady= 20, command= button_add)
button_subtract = Button(base, text= "-", padx= 41, pady= 20, command= button_subtract) 
button_multiply = Button(base, text= "*", padx= 41, pady= 20, command= button_multiply)
button_divide = Button(base, text= "/", padx= 39, pady= 20, command= button_divide)

button_equal = Button(base, text= "=", padx= 91, pady= 20, command= button_equal)
button_clear = Button(base, text= "Clear", padx= 79, pady= 20, command= button_clear)

# Displays buttons on the screen


# Buttons on row 1
button_7.grid(row= 1, column= 0)
button_8.grid(row= 1, column= 1)
button_9.grid(row= 1, column= 2)

# Buttons on row 2
button_4.grid(row= 2, column= 0)
button_5.grid(row= 2, column= 1)
button_6.grid(row= 2, column= 2)

# Buttons on row 3
button_1.grid(row= 3, column= 0)
button_2.grid(row= 3, column= 1)
button_3.grid(row= 3, column= 2)

# Buttons on row 4
button_0.grid(row= 4, column= 0)
button_clear.grid(row= 4, column= 1, columnspan= 2)

# Buttons on row 5
button_add.grid(row= 5, column= 0)
button_equal.grid(row= 5, column= 1, rowspan= 1,columnspan= 2)

# Buttons on row 6
button_subtract.grid(row= 6,column= 0)
button_divide.grid(row= 6, column= 1)
button_multiply.grid(row= 6, column= 2)


base.mainloop()
