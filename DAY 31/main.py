from tkinter import *
import random
import pandas

from os import listdir
from os.path import isfile, join



BACKGROUND_COLOR = "#B1DDC6"
SECONDS_DELAY = 3000
window_after_id = ""
selected_language = ""

def create_button(text, row_grid, col_grid, col_span = 1, btn_width = 0, btn_command = None, photo_img = None, btn_pad_y = 0):
    my_button = Button()
    my_button["text"] = text
    my_button["command"] = btn_command
    my_button.grid(row = row_grid, column = col_grid, columnspan = col_span, pady = btn_pad_y)
    
    if btn_width > 0:
        my_button["width"] = btn_width
    
    if photo_img != None:
        my_button["image"] = photo_img
    
    my_button["highlightthickness"] = 0
    
    return my_button


def language_selection():

    def select_language(lang):
        global selected_language
        selected_language = lang
        
        first_window.destroy()
        flash_card()
        
    first_window = Tk()

    first_window.title("Language Selection")
    first_window["bg"] = BACKGROUND_COLOR
    first_window["padx"] = 50
    first_window["pady"] = 50
    i = 0
    for file in [f.replace(".csv", "").upper() for f in listdir(path = "data") if isfile(join("data", f))]:
        btn_lang = create_button(file, row_grid = i, col_grid = 0, btn_width = 50, btn_pad_y = 5, btn_command = lambda lang = file.capitalize(): select_language(lang))
        btn_lang["pady"] = 20
        btn_lang["font"] = ("Courier", 20, "bold")
        i += 1

    first_window.eval('tk::PlaceWindow . center')
    first_window.mainloop()
    

def flash_card():
    
    def cancel_previous_after_method():
        global window_after_id
        if window_after_id != "":
            my_window.after_cancel(window_after_id)
    
    def next_word():
    
        cancel_previous_after_method()
        
        word_list = df_words.to_dict(orient = "records")
        
        if len(word_list) > len(shown_words):
            
            word = random.choice(word_list)
            base_language = list(word.keys())[0]
            
            while (word[base_language] in shown_words):
                word = random.choice(word_list)
                
            my_canvas.itemconfig(txt_base_lang, text = base_language, fill = "black")
            my_canvas.itemconfig(txt_word_to_learn, text = word[base_language], fill = "black")
            my_canvas.itemconfig(img_background, image = img_card_front)
            
            shown_words[word[base_language]] = word[list(word.keys())[1]]
            translate_button["state"] = "normal"
            
            global window_after_id
            window_after_id = my_window.after(SECONDS_DELAY, func = lambda: flip_card(True))
        else:
            close_flash_card()

    def known_word():
        next_word()
    
    def translate_word():
        flip_card(True)

    def close_flash_card():
        cancel_previous_after_method()
        my_window.destroy()
        language_selection()
            
    def flip_card(front):

        cancel_previous_after_method()
        
        if front:
            
            base_text = my_canvas.itemcget(txt_word_to_learn, "text")
            my_canvas.itemconfig(txt_base_lang, text = "English", fill = "white")
            my_canvas.itemconfig(txt_word_to_learn, text = shown_words[base_text], fill = "white")
            my_canvas.itemconfig(img_background, image = img_card_back)
            
            translate_button["state"] = "disabled"
            
            global window_after_id
            window_after_id = my_window.after(SECONDS_DELAY, func = lambda: flip_card(not front))
        else:
            next_word()
    
    
    my_window = Tk()
    shown_words = {}
    df_words = pandas.read_csv(filepath_or_buffer = f"data/{selected_language}.csv", sep = ";", encoding="ANSI")

    my_window.title(f"Language Flash Card - {selected_language}")
    my_window["bg"] = BACKGROUND_COLOR
    my_window["padx"] = 50
    my_window["pady"] = 50

    my_canvas = Canvas()
    my_canvas["width"] = 800
    my_canvas["height"] = 526
    my_canvas["bg"] = BACKGROUND_COLOR
    my_canvas["highlightthickness"] = 0

    img_card_front = PhotoImage(file = "images/card_front.png")
    img_card_back = PhotoImage(file = "images/card_back.png")

    img_background = my_canvas.create_image(400, 264, image = img_card_front)
    txt_base_lang = my_canvas.create_text(400, 150, text = "Title", font =  ("Arial", 30, "italic"))
    txt_word_to_learn = my_canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"))

    translate_img = PhotoImage(file = "images/translation.png")
    translate_button = create_button("", row_grid = 1, col_grid = 0, photo_img = translate_img, btn_command = translate_word)
    translate_button["bg"] = BACKGROUND_COLOR

    known_img = PhotoImage(file = "images/right.png")
    known_button = create_button("", row_grid = 1, col_grid = 1, photo_img = known_img, btn_command = known_word)
    
    close_img = PhotoImage(file = "images/wrong.png")
    close_button = create_button("", row_grid = 1, col_grid = 2, photo_img = close_img, btn_command = close_flash_card)

    my_canvas.grid(row = 0, column = 0, columnspan = 3)

    my_window.eval('tk::PlaceWindow . center')

    next_word()

    my_window.mainloop()
    
    

language_selection()
