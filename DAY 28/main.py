
from tkinter import *
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----------------------------------------------------------- # 
window_after_id = ""
timer_cycle = 1

# ----------------------------------------------------------- # 
def add_check_text():
    lbl_check["text"] = lbl_check["text"] + "✅"

def update_timer(MIN, timer_text, timer_text_color):
    global window_after_id
    window_after_id = my_window.after(1000, start_timer,  datetime.datetime(2024, 1, 1, 0, MIN, 0) - datetime.timedelta(seconds = 0))
    lbl_timer["text"] = timer_text
    lbl_timer["fg"] = timer_text_color

# ----------------------------------------------------------- # 
def reset_timer(work_time = datetime.datetime(2024, 1, 1, 0, 0, 0)):
    my_canvas.itemconfig(timer_text, text =str(work_time).split(" ")[1])
    btn_start["state"] = "normal"
    btn_reset["state"] = "disabled"
    
    lbl_timer["text"] = "Timer"
    lbl_timer["fg"] = "black"
    
    lbl_check["text"] = ""
    
    global timer_cycle
    timer_cycle = 1
    
    my_window.after_cancel(window_after_id)
    
# ----------------------------------------------------------- # 
def start_timer(work_time = datetime.datetime(2024, 1, 1, 0, WORK_MIN, 0)):
    
    if btn_start["state"] == "normal":
        btn_start["state"] = "disabled"
        btn_reset["state"] = "normal"
        
        lbl_timer["text"] = "Work"
        lbl_timer["fg"] = GREEN

    text_to_show = str(work_time).split(" ")[1]
    my_canvas.itemconfig(timer_text, text = text_to_show)
    
    if text_to_show == "00:00:00":
        global timer_cycle
        timer_cycle += 1
        
        if timer_cycle == 2 or timer_cycle == 4 or timer_cycle == 6:
            # SHORT BREAK TIMER
            update_timer(SHORT_BREAK_MIN, "Break", PINK)
            add_check_text()
            
        elif timer_cycle == 3 or timer_cycle == 5 or timer_cycle == 7:
            # WORK TIMER
            update_timer(WORK_MIN, "Work", GREEN)
            
        elif timer_cycle == 8:
            # LONG BREAK TIMER
            update_timer(LONG_BREAK_MIN, "Long Break", RED)
            add_check_text()
            
        elif timer_cycle >= 9:
            # ENDS THE TIMER
            lbl_timer["text"] = "Timer"
            reset_timer()
    else:
        # CONTINUE DEDUCTING BY 1 SEC
        global window_after_id
        window_after_id = my_window.after(1000, start_timer, work_time - datetime.timedelta(seconds = 1))

# ---------------------------- UI SETUP ------------------------------- #
def create_label(text, FONT, BG_COLOR, FG_COLOR, row_grid, col_grid):
    my_label = Label()
    my_label["text"] = text
    my_label["font"] = FONT
    my_label["bg"] = BG_COLOR
    my_label["fg"] = FG_COLOR
    my_label.grid(row = row_grid, column = col_grid)
    
    return my_label

def create_button(text, FONT, row_grid, col_grid, btn_command = None):
    my_button = Button()
    my_button["text"] = text
    my_button["font"] = FONT
    my_button["command"] = btn_command
    my_button.grid(row = row_grid, column = col_grid)
    
    return my_button

my_window = Tk()
my_window.title("Pomodoro")
my_window.config(padx = 100, pady = 150, bg = YELLOW)
my_window.resizable(0, 0)

lbl_timer = create_label(text = "Timer", FONT = (FONT_NAME, 50, "bold"), BG_COLOR = YELLOW, FG_COLOR = "black", row_grid = 0, col_grid = 1)

my_canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
my_canvas.create_image(100, 112, image = tomato_img)
timer_text = my_canvas.create_text(100, 130, text = "00:00:00", fill = "white", font = (FONT_NAME, 30, "bold"))
my_canvas.grid(row = 1, column = 1)

btn_start = create_button(text = "Start", FONT =(FONT_NAME, 16, "bold"), row_grid = 2, col_grid = 0, btn_command = start_timer )

btn_reset = create_button(text = "Reset", FONT =(FONT_NAME, 16, "bold"), row_grid = 2, col_grid = 2, btn_command = reset_timer )
btn_reset["state"] = "disabled"

lbl_check = create_label(text = "", FONT = (FONT_NAME, 16, "bold"), BG_COLOR = YELLOW, FG_COLOR = GREEN, row_grid = 3, col_grid = 1)
lbl_check.config(pady = 25)

my_window.mainloop()