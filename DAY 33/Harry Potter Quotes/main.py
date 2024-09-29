from tkinter import *
import requests


def get_quote():
    
    api_response = requests.get("https://api.portkey.uk/quote")
    api_response.raise_for_status()
    
    api_data = api_response.json()
    canvas.itemconfig(quote_text, text = f"{api_data['quote']}\n\n- {api_data['speaker']}, {api_data['story']}.")


window = Tk()
window.title("Harry Potter Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 13, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="dumbledore.png", height=150, width=150)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()