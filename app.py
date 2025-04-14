# Use togheter witch Free Cam player to convert videos quickly
import tkinter as tk
from tkinter import filedialog, ttk
from typing import Optional
from moviepy import VideoFileClip
import os
import sys
import subprocess

class FileConversor(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Conversor de Arquivo")
        self.geometry("400x400")
        self.configure(bg="#e6f0fa")
        self._setup_style()
        self._setup_widgets()

    def _setup_style(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Modern.TLabel",
            font=("Segoe UI", 10),
            foreground="#2e2e2e",
            background="#e6f0fa",
            padding=5,
        )

        style.configure(
            "Modern.TEntry",
            font=("Segoe UI", 10),
            padding=6,
            relief="flat"
        )

        style.configure(
            "Modern.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=10,
            background="#4a90e2",
            foreground="white",
            relief="flat"
        )

        style.map(
            "Modern.TButton",
            background=[("active", "#357ABD")],
            foreground=[("disabled", "#d9d9d9")]
        )

        style.configure(
            "Success.TLabel",
            font=("Segoe UI", 10, "bold"),
            background="#d4edda",  # verde claro
            foreground="#155724",
            padding=10
        )

    def _setup_widgets(self) -> None:
        self.file_path_var = tk.StringVar()

        label = ttk.Label(self, text="Select a file:", style="Modern.TLabel")
        label.pack(pady=(20, 0))

        entry = ttk.Entry(self, textvariable=self.file_path_var, width=50, style="Modern.TEntry")
        entry.pack(pady=10, padx=20)

        button = ttk.Button(self, text="Browse...", command=self._select_file, style="Modern.TButton")
        button.pack(pady=5)

        button = ttk.Button(self, text="Converter", command=self._convert_file, style="Modern.TButton")
        button.pack(pady=5)

        open_result = ttk.Button(self, text="Abrir Vídeo Convertido", command=self._open_video, style="Modern.TButton")
        open_result.pack(pady=15)

    def _select_file(self) -> None:
        file_path: Optional[str] = filedialog.askopenfilename()
        if file_path:
            self.file_path_var.set(file_path)

    def _convert_file(self) -> None:
        output_path = r"./outputs/output.mp4"
        clip = VideoFileClip(self.file_path_var.get())
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        label_final = ttk.Label(self, text="CONVERSÃO CONCLUÍDA!!!", style="Success.TLabel")
        label_final.pack(pady=(10, 0))

    def _open_video(self) -> None:
        video_path = os.path.abspath("outputs/output.mp4")
        if not os.path.exists(video_path):
            print("Arquivo não encontrado.")
            return

        try:
            if sys.platform.startswith("win"):
                os.startfile(video_path)
            elif sys.platform.startswith("darwin"):
                subprocess.run(["open", video_path])
            else:
                subprocess.run(["xdg-open", video_path])
        except Exception as e:
            print(f"Erro ao abrir o vídeo: {e}")

if __name__ == "__main__":
    app = FileConversor()
    app.mainloop()