import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
from pytube import YouTube

path = ""
to_download = ""


def download():
    global to_download
    quality = qualityDropDown.get()
    link = linkBox.get()
    if len(link) > 1:
        video = YouTube(link)

        if quality == qualityOptions[0]:
            to_download = video.streams.filter(progressive=True).first()
        elif quality == qualityOptions[1]:
            to_download = video.streams.filter(only_audio=True).first()

        to_download.download(path)


gui = tk.Tk()

gui.title("")
gui.configure(bg="black")
gui.geometry("250x300")
gui.columnconfigure(0, weight=1)

title = tk.Label(gui, bg="black", fg="red", text="YouTube Downloader", font=("Helvetica", 16))
title.grid(pady=5)

linkLabel = tk.Label(gui, bg="black", fg="white", text="Paste Link to Video")
linkLabel.grid(pady=10)

linkBoxVar = tk.StringVar()
linkBox = tk.Entry(gui, width=25, textvariable=linkBoxVar)
linkBox.grid()


def folder():
    global path
    path = filedialog.askdirectory()


locationButton = tk.Button(gui, width=10, bg="blue", fg="white", text="Choose folder", command=folder)
locationButton.grid(pady=20)

locationLabel = tk.Label(gui, bg="black", fg="white")
locationLabel.grid()

qualityLabel = tk.Label(gui, bg="black", fg="white", text="Choose Option")
qualityLabel.grid()

qualityOptions = ["Video with Audio", "Audio Only"]
qualityDropDown = ttk.Combobox(gui, values=qualityOptions)
qualityDropDown.grid()

downloadButton = tk.Button(gui, width=10, bg="white", fg="black", text="Download", command=download)
downloadButton.grid(pady=30)

gui.mainloop()
