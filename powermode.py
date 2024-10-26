import tkinter as tk
from tkinter import ttk
import subprocess

# Power plans GUIDs for common modes (these are system defaults)
POWER_MODES = {
    "Power Saver": "a1841308-3541-4fab-bc81-f71556f20b4a",
    "Balanced": "381b4222-f694-41f0-9685-ff5bb260df2e",
    "High Performance": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
}

def change_power_mode(mode):
    # Run the powercfg command with the selected power plan GUID
    plan_guid = POWER_MODES[mode]
    try:
        subprocess.run(["powercfg", "/S", plan_guid], check=True)
        status_label.config(text=f"Power mode changed to {mode}.", foreground="green")
    except subprocess.CalledProcessError:
        status_label.config(text="Failed to change power mode.", foreground="red")

# Create main window
root = tk.Tk()
root.title("Power Mode Selector")
root.geometry("350x300")
root.configure(bg="#2E3440")  # Dark background

# Define style
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12, "bold"),
                padding=10,
                background="#5E81AC",
                foreground="#000000",  # Always black text
                borderwidth=0)
style.map("TButton",
          background=[("active", "#81A1C1")])  # Only change the background on hover

# Title label
title_label = tk.Label(root, text="Select Your Power Mode", font=("Helvetica", 16, "bold"), bg="#2E3440", fg="#ECEFF4")
title_label.pack(pady=(20, 10))

# Create buttons for each power mode
button_frame = tk.Frame(root, bg="#2E3440")
button_frame.pack(pady=20)

for mode in POWER_MODES.keys():
    button = ttk.Button(button_frame, text=mode, command=lambda m=mode: change_power_mode(m))
    button.pack(fill="x", padx=20, pady=5)

# Status label for feedback
status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2E3440", fg="#D8DEE9")
status_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
