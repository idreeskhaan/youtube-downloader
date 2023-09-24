#!/usr/bin/env python3

from pytube import YouTube
import tkinter as tk
import customtkinter as ctk
import os

def onprogress(stream, chunk, bytes_remaining):

    tot_bytes= stream.filesize
    down_frac= (tot_bytes - bytes_remaining)/tot_bytes
    progress_label.configure(text= f"{down_frac*100} %", text_color= 'white')
    progress_label.update()
    progress_bar.set(down_frac)

def download_callback(PRESETS, vid_var, audio_var):

    try:
        yt= YouTube(url.get(), on_progress_callback=onprogress)

        if audio_var.get()==1:
            video= yt.streams.get_by_resolution(resolution=PRESETS[vid_var.get()])
            url_label.configure(text= f"{yt.title} | {PRESETS[vid_var.get()]}", text_color='white')

        elif audio_var.get()==0:
            video= yt.streams.get_audio_only()
            url_label.configure(text= f"{yt.title} | audio", text_color='white')

        video.download()
        des_label.configure(text= f"Downloaded to: {os.getcwd()}", text_color='white')

    except Exception as e:
        des_label.configure(text= f"Error Downloading {e}", text_color= 'red')
    

#set theme
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

#create app object
app= ctk.CTk()
app.geometry('720x480')
app.title('Youtube Downloader')

#Add URL label
url_label= ctk.CTkLabel(app, text="Youtube URL")
url_label.pack(padx=5, pady=5)

#Add URL entry
url= tk.StringVar() #URL var
url_entry= ctk.CTkEntry(app, width=400, height=30, textvariable=url)
url_entry.pack(padx=5, pady=5)


#Audio and Video RadioButton
audio_frame= ctk.CTkFrame(app, width=100, height=30)
AUDIO= ["audio", "video"]
audio_var= tk.IntVar()
audio_radio= [ctk.CTkRadioButton(audio_frame, text=AUDIO[i], variable=audio_var, value=i).grid(row=0, column=i, sticky="W") for i in range(len(AUDIO))]
audio_frame.pack(padx=10, pady=10)

# Video Quality RadioButtons
quality_frame= ctk.CTkFrame(app, width=100, height=30)
PRESETS= ["144p", "240p", "360p", "480p", "720p"]
vid_var= tk.IntVar()
radio= [ctk.CTkRadioButton(quality_frame, text=PRESETS[i], variable=vid_var, value=i).grid(row=0, column=i, sticky="W") for i in range(len(PRESETS))]
quality_frame.pack()


#Dowload description
des_label= ctk.CTkLabel(app, text="")
des_label.pack(padx=5, pady=5)

#progress percentage
progress_label= ctk.CTkLabel(app, text="0%")
progress_label.pack(padx=5, pady=5)

#progress bar
progress_bar= ctk.CTkProgressBar(app, width=400)
progress_bar.set(0.0)
progress_bar.pack(padx=5, pady=5)


#Download button
down_btn= ctk.CTkButton(app, text="Download", command=lambda: download_callback(PRESETS, vid_var, audio_var))
down_btn.pack(padx=5, pady=5)

#Loop app
app.mainloop()






