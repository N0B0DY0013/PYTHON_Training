THEME_COLOR = "#375362"

import tkinter
from quiz_brain import QuizBrain

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz_brain = quiz_brain
        
        self.window = tkinter.Tk()
        
        self.window.title("Quizzler")
        self.window["bg"] = THEME_COLOR
        self.window["padx"] = 20
        self.window["pady"] = 20
        
        self.question_count = self.create_label(label_txt = f"1 / {len(self.quiz_brain.question_list)}", fg = "white", bg = THEME_COLOR, font = ("Arial", 14, "normal"), grid_row = 0, grid_col = 0)

        self.quiz_score = self.create_label(label_txt = "Score: 0", fg = "white", bg = THEME_COLOR, font = ("Arial", 14, "normal"), grid_row = 0, grid_col = 1)

        self.canvas = tkinter.Canvas()
        self.canvas["height"] = 250
        self.canvas["width"]  = 300
        
        self.question_text = self.canvas.create_text(150, 125, width = 280,  text = "", font=("Arial", 20, "italic"), fill = THEME_COLOR)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)
        
        TRUE_image = tkinter.PhotoImage(file = "images/true.png")
        self.true_button = self.create_button(command = self.pressed_TRUE, image =  TRUE_image, width = 100, height = 100, grid_row = 2, grid_col = 0)
        
        FALSE_image = tkinter.PhotoImage(file = "images/false.png")
        self.true_button = self.create_button(command = self.pressed_FALSE, image =  FALSE_image, width = 100, height = 100, grid_row = 2, grid_col = 1)
        
        self.window_after_id = 0
                
        self.get_next_question()
        self.activate_window()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text = self.quiz_brain.next_question())
    
    def update_score(self):
        self.quiz_score["text"] = f"Score: {self.quiz_brain.score}"
    
    def update_question_count(self):
        self.question_count["text"] = f"{self.quiz_brain.question_number} / {len(self.quiz_brain.question_list)}"
    
    def pressed_TRUE(self):
        self.submit_answer("true")
    
    def pressed_FALSE(self):
       self.submit_answer("false")
    
    def submit_answer(self, value_pressed):
        self.quiz_brain.check_answer(value_pressed)
        
        if self.quiz_score["text"] == f"Score: {self.quiz_brain.score}":
            self.canvas["bg"] = "red"
        else:
            self.canvas["bg"] = "green"
        
        self.window_after_id = self.window.after(850, self.update_quiz)
    
    def update_quiz(self):
        
        if self.window_after_id != 0:
            self.window.after_cancel(self.window_after_id)
        
        self.canvas["bg"] = "white"
        self.update_score()
        
        if self.quiz_brain.still_has_questions():
            self.get_next_question()
            self.update_question_count()
        else:
             if self.window_after_id != 0:
                    self.window.after_cancel(self.window_after_id)
                    self.window.after(1000, self.window.destroy)
                    
    
    def create_label(self, label_txt, fg, bg, font, grid_row, grid_col):
        my_label = tkinter.Label()
        my_label["text"] = label_txt
        my_label["fg"] = fg
        my_label["bg"]= bg
        my_label["font"] = font
        my_label.grid(row = grid_row, column = grid_col)
        
        return my_label
    
    def create_button(self, command, image, width, height, grid_row, grid_col):
        my_button = tkinter.Button()
        my_button["command"] = command
        my_button["image"] = image
        my_button["width"] = width
        my_button["height"] = height
        my_button["highlightthickness"] = 0
        my_button.grid(row = grid_row, column = grid_col)
        
        return my_button
    
    def activate_window(self):
        self.window.lift()
        self.window.attributes('-topmost',True)
        self.window.after_idle(self.window.attributes,'-topmost',False)
        self.window.focus_force()
        self.window.deiconify()
        self.window.eval('tk::PlaceWindow . center')