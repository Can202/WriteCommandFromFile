import pyautogui
import tkinter
from tkinter import ttk
import time
import threading
import os
import random
import subprocess

class App:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("")
        self.root.minsize(210, 300)

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(expand=True, fill="both")
        
        self.shuffle = False
        self.breaking = False
        self.styles()

        self.options = self.getFiles()
        self.option_var = tkinter.StringVar()
        self.option_var.set(self.options[0])  # Set the default selected option

        self.LabelStatus = tkinter.Label(self.frame, text="Status: ")
        self.LabelStatus.grid(row=0, column=0, padx=5, pady=5)

        self.canvas = tkinter.Canvas(self.frame, width=30, height=30)
        self.canvas.grid(row=0, column=1)
        self.mini_circle = self.canvas.create_oval(5,5,25,25,
            fill="red", outline="black",  width=1)

        self.LabelPrefix = tkinter.Label(self.frame, text="Prefix:")
        self.LabelPrefix.grid(row=1, column=0, padx=5, pady=5)
        self.EntryPrefix = tkinter.Entry(self.frame)
        self.EntryPrefix.grid(row=1, column=1, padx=5, pady=5)
        
        self.LabelOption = tkinter.Label(self.frame, text="Option:")
        self.LabelOption.grid(row=2, column=0, padx=5, pady=5)
        self.Option = ttk.OptionMenu(self.frame, self.option_var, self.options[0], *self.options)
        self.Option.grid(row=2, column=1, padx=5, pady=5)

        self.LabelSuffix = tkinter.Label(self.frame, text="Suffix:")
        self.LabelSuffix.grid(row=3, column=0, padx=5, pady=5)
        self.EntrySuffix = tkinter.Entry(self.frame)
        self.EntrySuffix.grid(row=3, column=1, padx=5, pady=5)


        self.submit_button = ttk.Button(self.frame, text="Start", style="Custom2.TButton", command=self.start)
        self.submit_button.grid(row=4, column=1, padx=5, pady=5)
        
        self.ButtonShuffle = ttk.Button(self.frame, text="Shuffle", style="Shuffle.TButton", command=self.shufflechange)
        self.ButtonShuffle.grid(row=5, column=1, padx=5, pady=5)

        self.break_button = ttk.Button(self.frame, text="Break", style="Break.TButton", command=self.breakTheProccess)
        self.break_button.grid(row=6, column=1, padx=5, pady=5)
        
        self.open_button = ttk.Button(self.frame, text="Open Files", style="Open.TButton", command=self.openPATH)
        self.open_button.grid(row=7, column=1, padx=5, pady=5)
        
        #self.reload_button = ttk.Button(self.frame, text="Reload", style="Open.TButton", command=self.reload)
        #self.reload_button.grid(row=8, column=1, padx=5, pady=5)
        self.reconfigure()

    def breakTheProccess(self):
        self.breaking = True
        print("Breaked")
        self.canvas.itemconfig(self.mini_circle, fill="red")
    
    def openPATH(self):
        subprocess.Popen(['explorer', "files"])
    
    def reload(self):
        print("reload")
        newoptions = self.getFiles()
        self.option_var = tkinter.StringVar()
        self.option_var.set(newoptions[0])

        menu = self.Option['menu']
        menu.delete(0, 'end')
            
        # Add the updated options
        for option in newoptions:
            menu.add_command(label=option, command=tkinter._setit(self.option_var, option))
        
        self.option_var.set(newoptions[0])
        self.options = None
        self.options = newoptions
    def shufflechange(self):
        self.shuffle = not self.shuffle
        if self.shuffle:
            self.style.configure("Shuffle.TButton", foreground = "green")
        else:
            self.style.configure("Shuffle.TButton", foreground = "darkred")

    
    def start(self):
        self.breaking = False

        self.canvas.itemconfig(self.mini_circle, fill="green")

        prefix = self.EntryPrefix.get()
        suffix = self.EntrySuffix.get() + "\n"
        selected_option = self.option_var.get()
        list = self.getList(selected_option)

        thread = threading.Thread(target=lambda: self.write(prefix, list, suffix))
        thread.start()
        

    def getFiles(self):
        path = "files"
        if not os.path.exists(path):
            os.mkdir(path)
        
        files = os.listdir(path)

        for i in range(len(files)):
            if files[i].endswith(".txt"):
                files[i] = files[i][:-4]
            else:
                files.remove(files[i])

        if len(files) == 0:
            with open("files/nothing.txt", 'w') as file:
                file.write('something here\n')
                file.write('something here\n')
            files.append("nothing")

        return files
        


            
    def mainloop(self):
        self.root.mainloop()

    def write(self, prefix, list, suffix):
        print("Started")
        self.Timing(1.5)
        print("Printing")

        if self.shuffle:
            random.shuffle(list)

        for i in range(len(list)):
            if self.breaking:
                return
            self.Timing(3)
            if self.breaking:
                return
            text = f"{prefix}{list[i]}{suffix}"
            pyautogui.typewrite(text, interval=0.001)
            print(text)
            if self.breaking:
                return

        self.canvas.itemconfig(self.mini_circle, fill="red")


    def Timing(self, tim):
        time.sleep(tim)

    def getList(self, list):
        list += ".txt"
        path = f"files/{list}"
        if os.path.exists(path):
            with open(path, 'r') as file:
                lines = file.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].strip()

            

            return lines
        else:
            return ["One", "Two"]
    def styles(self):
        self.style = ttk.Style()
        self.style.configure("Shuffle.TButton",
                        font=("Helvetica", 10),
                        foreground="darkred",
                        background="black",
                        padding=(5, 3))
        self.style.configure("Break.TButton",
                        font=("Helvetica", 10),
                        foreground="darkred",
                        background="black",
                        padding=(5, 3))
        self.style.configure("Open.TButton",
                        font=("Helvetica", 10),
                        foreground="green",
                        background="black",
                        padding=(5, 3))
        
        self.style.configure("Custom2.TButton",
                        font=("Helvetica", 14),
                        foreground="black",
                        background="black",
                        padding=(5, 3))
    def reconfigure(self):
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_rowconfigure(5, weight=1)
        self.frame.grid_rowconfigure(6, weight=1)
        self.frame.grid_rowconfigure(7, weight=1)
        self.frame.grid_rowconfigure(7, weight=1)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()