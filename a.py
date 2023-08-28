import tkinter as tk
from tkinter import ttk

def update_options():
    # Replace these options with your updated list of options
    new_options = ["Option 4", "Option 5", "Option 6"]
    
    # Clear the existing menu options
    menu = option_menu['menu']
    menu.delete(0, 'end')
    
    # Add the updated options
    for option in new_options:
        menu.add_command(label=option, command=tk._setit(option_var, option))
    
    # Reconfigure the StringVar with the first option from the updated list
    option_var.set(new_options[0])

root = tk.Tk()
root.title("Update OptionMenu")

# Create a StringVar to hold the selected option
option_var = tk.StringVar()

# Initial list of options
options = ["Option 1", "Option 2", "Option 3"]

# Create an OptionMenu widget
option_menu = ttk.OptionMenu(root, option_var, options[0], *options)
option_menu.pack(pady=10)

# Button to update options
update_button = ttk.Button(root, text="Update Options", command=update_options)
update_button.pack()

root.mainloop()
