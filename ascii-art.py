import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
import os
import shutil
import time
import threading
import PIL
from PIL import Image, ImageColor, ImageFilter

SHADING = {
    "10": "░",
    "50": "▒",
    "100": "▓",
    "150": "█",
    "200": "▓",
    "255": "█",
}

def fileDialog():
    FILE_SELECT = filedialog.askopenfile(mode="r")
    TEMP_IMAGE = Image.open(str(FILE_SELECT.name))
    ORIGINAL_IMAGE = TEMP_IMAGE.convert("RGB")
    PIXELATED_IMAGE = ORIGINAL_IMAGE.resize((int(ORIGINAL_IMAGE.width / int(QUALITY.get())), int(ORIGINAL_IMAGE.height / int(QUALITY.get()))), resample=Image.Resampling.LANCZOS)
    LIST_OUTPUT = []
    for Y_PIXEL in range(int(PIXELATED_IMAGE.height)):
        LIST_OUTPUT.append("\n")
        for X_PIXEL in range(int(PIXELATED_IMAGE.width)):
            R, G, B = PIXELATED_IMAGE.getpixel((X_PIXEL, Y_PIXEL))
            BRIGHTNESS = int(sum([R,G,B]) / 3)
            for KEY in dict(SHADING).keys():
                if int(KEY) >= BRIGHTNESS:
                    LIST_OUTPUT.append(SHADING[str(KEY)])
                    break
    with open("{}/output.txt".format(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')), "w", encoding="utf-8") as file:
        file.write("".join(LIST_OUTPUT))
        file.close()
    os.system("start {}/output.txt".format(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')))
    
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        global QUALITY
        
        COLUMN_COUNT = 3
        ROW_COUNT = 5
        QUALITY = ctk.IntVar(
            name="QUALITY", 
            value=10
        )
        
        self.geometry("600x400")
        self.title("Image to ASCII Art")
        self.resizable(False, False)
        self.rootFrame = ctk.CTkFrame(
            master=self, 
            width=self.winfo_width(), 
            height=self.winfo_height()
        )
        self.rootFrame.grid(
            row=0, 
            column=0, 
            sticky="nsew"
        )
        for _ in range(COLUMN_COUNT):
            self.rootFrame.columnconfigure(index=int(_), weight=1)
        for _ in range(ROW_COUNT):
            self.rootFrame.rowconfigure(index=int(_), weight=1)
        
        self.FILE_SELECT_BUTTON = ctk.CTkButton(
            master=self.rootFrame,
            text="Select File",
            command=fileDialog
        )
        self.FILE_SELECT_BUTTON.grid(
                column=1,
                row=4
            )
        self.TEXT = ctk.CTkLabel(
            master=self.rootFrame, 
            textvariable=QUALITY
        )
        self.TEXT.grid(
            column=1,
            row=3
        )
        self.QUALITY_SLIDER = ctk.CTkSlider(
            master=self.rootFrame, 
            from_=10, 
            to=80, 
            number_of_steps=7,
            variable=QUALITY
        )
        self.QUALITY_SLIDER.grid(
            column=1,
            row=2
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()