
import tkinter
import datetime

# def add(*args):
#     return sum(args)    

# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9,10))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# my_screen = tkinter.Tk()
# my_screen.minsize(width = 500, height = 500)
# my_screen.title("Show Time")

# label_1 = tkinter.Label()
# label_1["text"] = f"Time is: {datetime.datetime.now()}"
# label_1.pack()

# def show_time(label):
#     label["text"] =f"Time is: {datetime.datetime.now()}"

# button_1 = tkinter.Button()
# button_1["text"] = "Update Time"
# button_1["command"] = lambda: show_time(label_1)
# button_1.pack()

# label_2 = tkinter.Label()
# label_2["text"] = "Waiting for input ..."
# label_2.pack()

# input_1 = tkinter.Entry()
# input_1.pack()

# def show_input(entry, label):
#     label["text"] = entry.get()
    
# button_2 = tkinter.Button()
# button_2["text"] = "Show Input"
# button_2["command"] = lambda: show_input(input_1, label_2)
# button_2.pack()

# my_screen.mainloop()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# my_screen = tkinter.Tk()
# my_screen.minsize(width = 500, height = 500)
# my_screen.title("Show Time")

# label_1 = tkinter.Label()
# label_1["text"] = f"Time is: {datetime.datetime.now()}"
# label_1.grid(row = 0, column = 0)

# def show_time(label):
#     label["text"] =f"Time is: {datetime.datetime.now()}"

# button_1 = tkinter.Button()
# button_1["text"] = "Update Time"
# button_1["command"] = lambda: show_time(label_1)
# button_1.grid(row = 0, column = 2)


# def show_input(entry, label):
#     label["text"] = entry.get()
    
# button_2 = tkinter.Button()
# button_2["text"] = "Show Input"
# button_2["command"] = lambda: show_input(input_1, label_2)
# button_2.grid(row = 1, column = 1)


# label_2 = tkinter.Label()
# label_2["text"] = "Waiting for input ..."
# label_2.grid(row = 1, column = 0)

# input_1 = tkinter.Entry()
# input_1.grid(row = 2, column = 3)

# my_screen.mainloop()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

my_screen = tkinter.Tk()
my_screen.minsize(width = 300, height = 100)
my_screen.title("Mile to Km Converter")

my_screen.config(padx=20)

entry_1 = tkinter.Entry()
entry_1.insert(0, string = "0")
entry_1.grid(row = 0, column = 1)
entry_1.focus()

label_1 = tkinter.Label()
label_1["text"] = "Miles"
label_1.grid(row = 0, column = 2)

label_2 = tkinter.Label()
label_2["text"] = "is equal to"
label_2.grid(row = 1, column = 0)

label_3 = tkinter.Label()
label_3["text"] = "0"
label_3.grid(row = 1, column = 1)

label_4 = tkinter.Label()
label_4["text"] = "Km"
label_4.grid(row = 1, column = 2)

def convert_miles_to_Km(entry, label):
    if str(entry.get()).isnumeric():
        label["text"] = f"{round(int(entry.get()) * 1.609344, 2)}"
    
button_1 = tkinter.Button()
button_1["text"] = "Calculate"
button_1["command"] = lambda: convert_miles_to_Km(entry_1, label_3)
button_1.grid(row = 2, column = 1)

my_screen.mainloop()