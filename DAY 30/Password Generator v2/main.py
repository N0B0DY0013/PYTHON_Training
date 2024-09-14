from tkinter import *
from tkinter import messagebox
import json
import password_generator


# ---------------------------- SEARCH PASSWORD ---------------------------------- #
def search_password():
    json_data = get_json_data()
    searched_website = txt_website.get()
    website_info =  {searched_website:details for (website, details) in json_data.items() if website.lower() == searched_website.lower()}
    if website_info != {}:
        messagebox.showinfo(title = txt_website.get(), message = f"Username: {website_info[searched_website]['username']}\nPassword: {website_info[searched_website]['password']}")
    else:
        messagebox.showinfo(message = "No data found.")
        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    txt_password.delete(0, END)
    txt_password.insert(END, password_generator.generate_password())
    txt_password.focus()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website_input = txt_website.get()
    username_input = txt_username.get()
    password_input = txt_password.get()
    
    if website_input != "" and username_input != "" and password_input != "":
        
        if messagebox.askokcancel(title = website_input, message = f"Are you sure to save this information?\nUsername: {username_input}\nPassword: {password_input}"):
            
            json_data = get_json_data()
            
            json_data.update({website_input: {"username": username_input,
                                              "password": password_input}})
                
            with open("password_data.json", mode = "w") as data_file:    
                # json.dump() accepts a dictionary ...
                json.dump(json_data,
                          data_file,
                          indent = 4)
                
            messagebox.showinfo(message = "Password successfully saved in 'password_data.json'.")
            
            clear_inputs()

            txt_website.focus()
            
    else:
        messagebox.showwarning(message = "Please insert data in all fields.")

def clear_inputs():
    txt_website.delete(0, END)
    txt_username.delete(0, END)
    txt_password.delete(0, END)
    
def get_json_data():
    json_data = {}
    try:
        with open("password_data.json", mode = "r") as data_file:
            try:
                json_data = json.load(data_file)
            except:
                pass
    except:
        pass
    
    return json_data

# ---------------------------- UI SETUP ------------------------------- #
def create_label(text, row_grid, col_grid, col_span = 1, label_width = 0):
    my_label = Label()
    my_label["text"] = text
    my_label.grid(row = row_grid, column = col_grid, columnspan = col_span)
    
    if label_width > 0:
        my_label["width"] = label_width
    
    return my_label

def create_text_entry(row_grid, col_grid, col_span = 1, text_width = 0):
    my_entry = Entry()
    my_entry.grid(row = row_grid, column = col_grid, columnspan = col_span)
    if text_width > 0:
        my_entry["width"] = text_width
     
    return my_entry

def create_button(text, row_grid, col_grid, col_span = 1, btn_width = 0, btn_command = None):
    my_button = Button()
    my_button["text"] = text
    my_button["command"] = btn_command
    my_button.grid(row = row_grid, column = col_grid, columnspan = col_span)
    if btn_width > 0:
        my_button["width"] = btn_width
    
    return my_button



my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx = 50, pady = 50)

my_canvas = Canvas(width = 200, height = 200)
tomato_img = PhotoImage(file = "logo.png")
my_canvas.create_image(100, 100, image = tomato_img)
my_canvas.grid(row = 0, column = 1)

lbl_website = create_label(text = "Website: ", row_grid = 1, col_grid = 0)
txt_website = create_text_entry(row_grid = 1, col_grid = 1, col_span = 2, text_width = 35)
txt_website.focus()
btn_search = create_button(text = "Search", row_grid = 1, col_grid = 3, btn_command = search_password)

lbl_username = create_label(text = "Email/Username: ", row_grid = 2, col_grid = 0)
txt_username = create_text_entry(row_grid = 2, col_grid = 1, col_span = 2, text_width = 35)

lbl_password = create_label(text = "Password: ", row_grid = 3, col_grid = 0)
txt_password = create_text_entry(row_grid = 3, col_grid = 1,  col_span=2, text_width=35)
btn_generate_pw = create_button(text = "Generate Password", row_grid = 3, col_grid = 3, btn_command = generate_random_password)

btn_add_pw = create_button(text = "Add", row_grid = 4, col_grid = 1, col_span = 2, btn_width = 36, btn_command = save_password)

my_window.mainloop()