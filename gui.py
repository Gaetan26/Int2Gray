

import customtkinter as ctk
import os, int2gray, threading

from tkinterdnd2 import DND_FILES
from PIL import Image
from uuid import uuid4


ctk.set_default_color_theme("green")

window_width = 300
window_height = 300


#
def processFileDroped(path, output, format_):
    processed = int2gray.process(path, output, format_)
    
    if processed:
        image = Image.open(f"{output}.{format_}")
        width, height = image.size
        
        popup = ctk.CTkToplevel(gui)

        popup.title(f"{output}.{format_}")
        popup.geometry(f"{width}x{height}")
        popup.resizable(width=False, height=False)

        popup.rowconfigure(0, weight=1)
        popup.columnconfigure(0, weight=1)
        
        ctk.CTkLabel(
            popup, 
            image=ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(width, height)
            ), 
            text=""
        ) \
        .grid(row=0, column=0, sticky='nwse')
        
        popup.mainloop


def fileDroped(event):
    file_paths = event.data
    
    if file_paths:
        
        file_paths = file_paths.split(" ")
        i = 1
        
        for path in file_paths:
            path = path.replace("{", "").replace("}", "")
            
            if os.path.isfile(path):
                output, format_ = f"exports/{str(uuid4())}", "png"
                threading.Thread(target=processFileDroped, args=(path, output, format_)).start()
                i += 1
#


gui = ctk.CTk()

gui.title("Int2Gray")
gui.geometry(f"{window_width}x{window_height}")
gui.resizable(width=False, height=False)

gui.rowconfigure(0, weight=1)
gui.columnconfigure(0, weight=1)

draganddrop_frame = ctk.CTkFrame(gui)
draganddrop_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nwse')
draganddrop_frame.columnconfigure(0, weight=1)
draganddrop_frame.rowconfigure([0,1], weight=1)

ctk.CTkLabel(
    draganddrop_frame, 
    image=ctk.CTkImage(
        dark_image=Image.open("icons/drop1.png"), 
        light_image=Image.open("icons/drop2.png"), 
        size=(128, 128)
    ), 
    text=""
) \
.grid(row=0, column=0, pady=(15, 0))

ctk.CTkLabel(
    draganddrop_frame,
    text="drag and drop your \nfile here",
    font=("Roboto", 20)
) \
.grid(row=1, column=0, pady=(0, 15))


draganddrop_frame.drop_target_register(DND_FILES)
draganddrop_frame.dnd_bind('<<Drop>>', fileDroped)

gui.mainloop()