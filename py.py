import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Define the download function using yt-dlp
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a video URL.")
        return

    # Prompt the user to select a download location
    filepath = filedialog.askdirectory()
    if not filepath:
        messagebox.showwarning("Warning", "No download directory selected.")
        return

    # yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality
        'outtmpl': f"{filepath}/%(title)s.%(ext)s",  # Output template for filename
    }

    # Download video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Initialize Tkinter
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

# GUI Layout
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

root.mainloop()
