import pyautogui
import tkinter
import time
import threading
import os
import random

class App:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Window")

        self.frame = tkinter.ttk.Frame(self.root, padding=10)
        self.frame.grid(row=0, column=0)
        
        self.shuffle = False
        self.styles()

        self.options = self.getFiles()
        self.option_var = tkinter.StringVar()
        self.option_var.set(self.options[0])  # Set the default selected option

        self.LabelStatusS = tkinter.Label(self.frame, text="Status: ")
        self.LabelStatusS.grid(row=0, column=0, padx=5, pady=5)
        self.LabelStatus = tkinter.Label(self.frame, text="Not Working")
        self.LabelStatus.grid(row=0, column=1, padx=5, pady=5)

        self.LabelPrefix = tkinter.Label(self.frame, text="Prefix:")
        self.LabelPrefix.grid(row=1, column=0, padx=5, pady=5)
        self.EntryPrefix = tkinter.Entry(self.frame)
        self.EntryPrefix.grid(row=1, column=1, padx=5, pady=5)
        
        self.LabelOption = tkinter.Label(self.frame, text="Option:")
        self.LabelOption.grid(row=3, column=0, padx=5, pady=5)
        self.Option = tkinter.OptionMenu(self.frame, self.option_var, *self.options)
        self.Option.grid(row=3, column=1, padx=5, pady=5)

        self.LabelSuffix = tkinter.Label(self.frame, text="Suffix:")
        self.LabelSuffix.grid(row=5, column=0, padx=5, pady=5)
        self.EntrySuffix = tkinter.Entry(self.frame)
        self.EntrySuffix.grid(row=5, column=1, padx=5, pady=5)

        self.LabelShuffle = tkinter.Label(self.frame, text="Shuffle: ")
        self.LabelShuffle.grid(row=7, column=0, padx=5, pady=5)
        self.ButtonShuffle = tkinter.ttk.Button(self.frame, text="Shuffle", style="Shuffle.TButton", command=self.shufflechange)
        self.ButtonShuffle.grid(row=7, column=1, padx=5, pady=5)


        self.submit_button = tkinter.ttk.Button(self.frame, text="Start", style="Custom2.TButton", command=self.start)
        self.submit_button.grid(row=9, column=1, padx=5, pady=5)
    
    def shufflechange(self):
        self.shuffle = not self.shuffle
        if self.shuffle:
            self.style.configure("Shuffle.TButton", foreground = "green")
        else:
            self.style.configure("Shuffle.TButton", foreground = "darkred")

    
    def start(self):

        self.LabelStatus.config(text=f"Working")

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
            self.Timing(3)
            text = f"{prefix}{list[i]}{suffix}"
            pyautogui.typewrite(text, interval=0.001)
            print(text)
        
        self.LabelStatus.config(text=f"Not Working")


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
        self.style = tkinter.ttk.Style()
        self.style.configure("Shuffle.TButton",
                        font=("Helvetica", 10),
                        foreground="darkred",
                        background="black",
                        padding=(5, 3))
        
        self.style.configure("Custom2.TButton",
                        font=("Helvetica", 14),
                        foreground="black",
                        background="black",
                        padding=(5, 3))

if __name__ == "__main__":
    app = App()
    app.mainloop()