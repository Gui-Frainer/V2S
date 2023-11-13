#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#V2S - Video to sound
import os
import moviepy.editor as mp
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def show_info(message):
    messagebox.showinfo("Video2Sound 1.0 - Information", message)
    
def V2S ():
    folder = folder_path_entry.get()
    # Create a folder to store the audio files
    output_folder = folder + '/audios_from_videos/'
    os.makedirs(output_folder, exist_ok=True)

    # List all the files in the folder
    files = os.listdir(folder)

    # Loop through the files in the folder
    for filename in files:
        # Check if the file has a video extension (e.g., .mp4, .avi, .mkv)
        if filename.endswith((".mp4",".MP4", ".avi", ".mkv", ".mxf", ".MXF")):
            # Split the filename and extension
            name, extension = os.path.splitext(filename)

            # Create a VideoFileClip object
            video_file = os.path.join(folder, filename)
            my_clip = mp.VideoFileClip(video_file)

            # Extract the audio and save it as a .wav file
            audio_output_path = os.path.join(output_folder, name + "_audio.wav")
            my_clip.audio.write_audiofile(audio_output_path)

    print("Audio extraction complete.")
    
app = tk.Tk()
app.title("V2S 1.0")
app.geometry("400x210")

folder_label = tk.Label(app, text="Select a folder with video files:")
folder_label.pack(pady=10)

folder_path_entry = tk.Entry(app, width=40)
folder_path_entry.pack()

browse_button = tk.Button(app, text="Browse", command=browse_folder)
browse_button.pack()

convert_button = tk.Button(app, text="Convert V2S", command=V2S)
convert_button.pack(pady=10)

created_by_label = tk.Label(app, text=" ©GFrainer2023")
created_by_label.pack(side="bottom", padx=10, pady=10)

source_code_label = tk.Label(app, text="github.com/Gui-Frainer/V2S-1.0")
source_code_label.pack(side="bottom", padx=10, pady=10)

app.mainloop()

