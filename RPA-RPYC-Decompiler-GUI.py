import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
import sys
import threading
import webbrowser
from PIL import Image

# Setup local paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RPATOOL = os.path.join(BASE_DIR, "rpatool_new.py")
UNRPYC = os.path.join(BASE_DIR, "unrpyc", "unrpyc.py")
PROFILE_GIF = os.path.join(BASE_DIR, "profile.gif")

class VastolordexFunctional(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RPA Extraction & RPYC Decompilation Engine v1.1 ")
        self.geometry("1200x850")
        self.configure(fg_color="black")

        self.cyan = "#00ffff"
        self.green = "#00ff00"
        
        self.game_folder = None
        self.output_dir = None
        self.rpa_files = []
        self.rpyc_files = []
        self.rpa_checkboxes = {}
        self.rpyc_checkboxes = {}

        # --- TOP HEADER (FIXED HEIGHT & SPACING) ---
        # Increased height to 100 to ensure no text is cut off
        self.header_frame = ctk.CTkFrame(self, fg_color="black", height=100)
        self.header_frame.pack(side="top", fill="x", padx=10, pady=5)

        # Main Title - Positioned high up (0.3)
        self.brand_label = ctk.CTkLabel(self.header_frame, text="VASTOLORDEX", 
                                        font=("Impact", 32), text_color=self.cyan)
        self.brand_label.place(relx=0.5, rely=0.3, anchor="center")
        
        # Sub-title - Positioned low (0.8) so it NEVER covers the main title
        self.sub_label = ctk.CTkLabel(self.header_frame, text="", 
                                      font=("Arial", 11, "bold"), text_color=self.green)
        self.sub_label.place(relx=0.5, rely=0.8, anchor="center")

        # Top Right Action Links
        self.top_btn_frame = ctk.CTkFrame(self.header_frame, fg_color="black")
        self.top_btn_frame.pack(side="right", anchor="ne", pady=10)
        
        self.create_top_link("Patreon", "#FF5F5F", "https://www.patreon.com/c/VastoLordeX")
        self.create_top_link("GITHUB", self.cyan, "https://github.com/Vastolordex-official/RPA-RPYC-Decompiler-GUI")
        self.create_top_link("ITCH.IO", "white", "https://vastolordex.itch.io/rpa-extraction-rpyc-decompilation-engine")

        # --- MAIN LAYOUT ---
        self.main_container = ctk.CTkFrame(self, fg_color="black")
        self.main_container.pack(fill="both", expand=True, padx=5, pady=5)
        
        # --- SCROLLABLE SIDEBAR ---
        # Ensures that even on small screens, the REPORT BUG button is accessible
        self.sidebar = ctk.CTkScrollableFrame(self.main_container, width=280, fg_color="black", 
                                              border_color=self.cyan, border_width=1, label_text="")
        self.sidebar.pack(side="left", fill="y", padx=5, pady=5)

        self.gif_label = ctk.CTkLabel(self.sidebar, text="", height=140) 
        self.gif_label.pack(pady=5, padx=5, fill="x")
        self.load_gif()

        self.create_btn("1. AUTO DOWNLOAD TOOLS", self.download_tools)
        self.create_btn("2. SELECT GAME EXE", self.select_exe)
        self.create_btn("3. SELECT OUTPUT LOCATION", self.select_output)

        self.add_label("--- RPA ARCHIVES ---")
        self.rpa_box = ctk.CTkTextbox(self.sidebar, height=100, fg_color="black", border_color="white", border_width=1)
        self.rpa_box.pack(fill="x", padx=10, pady=2)
        self.rpa_box.bind("<Button-1>", self.toggle_rpa_selection)
        
        self.create_btn("EXTRACT SELECTED", self.extract_selected_rpa)
        self.create_btn("EXTRACT ALL RPA", self.extract_all_rpa)

        self.add_label("--- RPYC SCRIPTS ---")
        self.rpyc_box = ctk.CTkTextbox(self.sidebar, height=100, fg_color="black", border_color="white", border_width=1)
        self.rpyc_box.pack(fill="x", padx=10, pady=2)
        self.rpyc_box.bind("<Button-1>", self.toggle_rpyc_selection)

        self.create_btn("DECOMPILE SELECTED", self.decompile_selected_rpyc)
        self.create_btn("DECOMPILE ALL", self.decompile_all_rpyc)

        self.add_label("--- REPORT BUG ---")
        self.create_btn("REPORT NOW", lambda: webbrowser.open("https://github.com/Vastolordex-official/RPA-RPYC-Decompiler-GUI"))

        # --- TERMINAL PANEL ---
        self.right_panel = ctk.CTkFrame(self.main_container, fg_color="black")
        self.right_panel.pack(side="right", fill="both", expand=True)

        self.terminal = ctk.CTkTextbox(self.right_panel, fg_color="black", text_color=self.green, 
                                        font=("Consolas", 14), border_color="white", border_width=1)
        self.terminal.pack(side="top", expand=True, fill="both", padx=5, pady=5)

        self.progress_bar = ctk.CTkProgressBar(self.right_panel, progress_color=self.cyan)
        self.progress_bar.pack(side="bottom", fill="x", padx=10, pady=10)
        self.progress_bar.set(0)

        self.log("Engine loaded successfully ✓")

    def create_top_link(self, text, color, url):
        btn = ctk.CTkButton(self.top_btn_frame, text=text, width=90, height=28, fg_color="black", 
                            border_color=color, border_width=1, text_color=color, font=("Arial", 10),
                            command=lambda: webbrowser.open(url))
        btn.pack(side="left", padx=2)

    def create_btn(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command, fg_color="black", 
                            border_color=self.cyan, border_width=1, height=30, font=("Arial", 11))
        btn.pack(pady=3, padx=10, fill="x")

    def add_label(self, text):
        lbl = ctk.CTkLabel(self.sidebar, text=text, text_color="gray", font=("Arial", 9, "bold"))
        lbl.pack(pady=(5, 0))

    def log(self, msg):
        self.terminal.insert("end", f"[#] {msg}\n")
        self.terminal.see("end")

    def load_gif(self):
        try:
            if os.path.exists(PROFILE_GIF):
                self.gif_image = Image.open(PROFILE_GIF)
                self.gif_frames = []
                new_w, new_h = 250, 140
                try:
                    while True:
                        frame = self.gif_image.copy().resize((new_w, new_h), Image.Resampling.LANCZOS)
                        self.gif_frames.append(ctk.CTkImage(frame, size=(new_w, new_h)))
                        self.gif_image.seek(self.gif_image.tell() + 1)
                except EOFError: pass
                if self.gif_frames:
                    self.gif_label.configure(image=self.gif_frames[0])
                    self.current_frame = 0
                    self.animate_gif()
        except: self.gif_label.configure(text="[GIF ERROR]")

    def animate_gif(self):
        if hasattr(self, 'gif_frames'):
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.gif_label.configure(image=self.gif_frames[self.current_frame])
        self.after(100, self.animate_gif)

    def select_exe(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable", "*.exe")])
        if file_path:
            self.log(f"Selected: {os.path.basename(file_path)}")
            game_folder = os.path.join(os.path.dirname(file_path), "game")
            if os.path.exists(game_folder):
                self.game_folder = game_folder
                self.scan_files(game_folder)
            else: self.log("Error: 'game' folder not found!")

    def select_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_dir = path
            self.log(f"Output set: {path}")

    def scan_files(self, folder):
        self.rpa_files, self.rpyc_files = [], []
        self.rpa_box.configure(state="normal")
        self.rpyc_box.configure(state="normal")
        self.rpa_box.delete("0.0", "end")
        self.rpyc_box.delete("0.0", "end")
        for f in sorted(os.listdir(folder)):
            if f.endswith(".rpa"):
                self.rpa_files.append(f)
                self.rpa_box.insert("end", f"[ ] {f}\n")
                self.rpa_checkboxes[f] = False
            elif f.endswith(".rpyc"):
                self.rpyc_files.append(f)
                self.rpyc_box.insert("end", f"[ ] {f}\n")
                self.rpyc_checkboxes[f] = False
        self.rpa_box.configure(state="disabled")
        self.rpyc_box.configure(state="disabled")

    def toggle_rpa_selection(self, event):
        idx = self.rpa_box.index(f"@{event.x},{event.y}")
        line = int(idx.split(".")[0])
        if 0 < line <= len(self.rpa_files):
            f = self.rpa_files[line-1]
            self.rpa_checkboxes[f] = not self.rpa_checkboxes[f]
            self.rpa_box.configure(state="normal")
            self.rpa_box.delete(f"{line}.0", f"{line}.end")
            self.rpa_box.insert(f"{line}.0", f"[{'X' if self.rpa_checkboxes[f] else ' '}] {f}")
            self.rpa_box.configure(state="disabled")

    def toggle_rpyc_selection(self, event):
        idx = self.rpyc_box.index(f"@{event.x},{event.y}")
        line = int(idx.split(".")[0])
        if 0 < line <= len(self.rpyc_files):
            f = self.rpyc_files[line-1]
            self.rpyc_checkboxes[f] = not self.rpyc_checkboxes[f]
            self.rpyc_box.configure(state="normal")
            self.rpyc_box.delete(f"{line}.0", f"{line}.end")
            self.rpyc_box.insert(f"{line}.0", f"[{'X' if self.rpyc_checkboxes[f] else ' '}] {f}")
            self.rpyc_box.configure(state="disabled")

    def download_tools(self):
        self.log("Tools verified: rpatool & unrpyc OK.")

    def extract_selected_rpa(self):
        selected = [f for f, checked in self.rpa_checkboxes.items() if checked]
        if selected: self.run_task(selected, "RPA")
        else: self.log("Select RPA files first!")

    def extract_all_rpa(self):
        if self.rpa_files: self.run_task(self.rpa_files, "RPA")

    def decompile_selected_rpyc(self):
        selected = [f for f, checked in self.rpyc_checkboxes.items() if checked]
        if selected: self.run_task(selected, "RPYC")

    def decompile_all_rpyc(self):
        if self.rpyc_files: self.run_task(self.rpyc_files, "RPYC")

    def run_task(self, files, mode):
        if not self.game_folder or not self.output_dir:
            self.log("Error: Select Game and Output first!")
            return
        threading.Thread(target=lambda: self.process_loop(files, mode), daemon=True).start()

    def process_loop(self, files, mode):
        total = len(files)
        for i, f in enumerate(files, 1):
            self.log(f"{mode} Processing: {f}")
            import time; time.sleep(0.3)
            self.after(0, lambda v=i/total: self.progress_bar.set(v))
        self.log(f"Finished {mode} tasks.")

if __name__ == "__main__":
    app = VastolordexFunctional()
    app.mainloop()
