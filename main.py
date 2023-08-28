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
        
        self.shuffle = False

        self.options = self.getFiles()
        self.option_var = tkinter.StringVar()
        self.option_var.set(self.options[0])  # Set the default selected option

        self.LabelStatus = tkinter.Label(self.root, text="Status: Not Working")
        self.LabelStatus.pack()

        self.LabelPrefix = tkinter.Label(self.root, text="Prefix:")
        self.LabelPrefix.pack()
        self.EntryPrefix = tkinter.Entry(self.root)
        self.EntryPrefix.pack()
        
        self.LabelOption = tkinter.Label(self.root, text="Option:")
        self.LabelOption.pack()
        self.Option = tkinter.OptionMenu(self.root, self.option_var, *self.options)
        self.Option.pack()

        self.LabelSuffix = tkinter.Label(self.root, text="Suffix:")
        self.LabelSuffix.pack()
        self.EntrySuffix = tkinter.Entry(self.root)
        self.EntrySuffix.pack()

        self.LabelShuffle = tkinter.Label(self.root, text="Shuffle: No")
        self.LabelShuffle.pack()
        self.ButtonShuffle = tkinter.Button(self.root, text="Shuffle", command=self.shufflechange)
        self.ButtonShuffle.pack()


        self.submit_button = tkinter.Button(self.root, text="Start", command=self.start)
        self.submit_button.pack()
    
    def shufflechange(self):
        self.shuffle = not self.shuffle
        if self.shuffle:
            self.LabelShuffle.config(text="Shuffle: Yes")
        else:
            self.LabelShuffle.config(text="Shuffle: No")

    
    def start(self):

        self.LabelStatus.config(text=f"Status: Working")

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
        
        self.LabelStatus.config(text=f"Status: Not Working")


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

if __name__ == "__main__":
    app = App()
    app.mainloop()