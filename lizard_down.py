import customtkinter
from tkinter import messagebox
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.attributes('-fullscreen', True)  # Make the window full screen

def on_button_click():
    result = messagebox.askquestion("Confirmation", "Are you sure?")
    if result == 'yes':
        messagebox.showinfo("Confirmed", "You clicked Yes!")
        app.destroy()# Close the window when "YES" is clicked
    else:
        print("no")
        app.destroy()
        os.system("shutdown /s /t 1")
    app.destroy()


def button_function1():
    print("button pressed")
    app.destroy()  # Close the window when "NO" is clicked
    os.system("shutdown /s /t 1")


label = customtkinter.CTkLabel(master=app, text="Are you Normal.", font=("Helvetica", 30))
label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="YES", command=on_button_click, font=("Helvetica", 20))
button.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)

button1 = customtkinter.CTkButton(master=app, text="NO", command=button_function1, font=("Helvetica", 20))
button1.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
