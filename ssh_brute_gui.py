import tkinter as tk
from tkinter import filedialog, scrolledtext
from threading import Thread
from subprocess import Popen, PIPE, STDOUT
import os
import signal

process_ref = None  # Global reference to subprocess

def browse_file(var):
    filename = filedialog.askopenfilename()
    if filename:
        var.set(filename)

def run_bruteforce():
    output_area.delete(1.0, tk.END)  # Clear previous output

    host = host_var.get()
    userlist = user_file_path.get()
    passlist = pass_file_path.get()
    threads = thread_count.get()
    delay_val = delay.get()
    max_user = max_retries.get()
    output = output_file_path.get()

    if not (host and userlist and passlist):
        output_area.insert(tk.END, "❌ Error: Please fill all required fields.\n", "error")
        return

    cmd = [
        "python",
        "advance_ssh_brute.py",
        host,
        "-U", userlist,
        "-P", passlist,
        "--threads", str(threads),
        "--delay", str(delay_val),
        "--max-user-retries", str(max_user),
        "--output", output
    ]

    def read_output():
        global process_ref
        process_ref = Popen(cmd, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        for line in process_ref.stdout:
            tag = "normal"
            if "[+]" in line:
                tag = "success"
            elif "[-]" in line:
                tag = "fail"
            elif "[!]" in line:
                tag = "warn"
            output_area.insert(tk.END, line, tag)
            output_area.see(tk.END)
        process_ref.wait()
        process_ref = None

    Thread(target=read_output).start()

def stop_bruteforce():
    global process_ref
    if process_ref:
        process_ref.terminate()
        output_area.insert(tk.END, "\n⛔ Brute force manually stopped.\n", "warn")
        process_ref = None

# GUI setup
root = tk.Tk()
root.title("SSH Brute Force GUI")
root.geometry("850x650")
root.config(bg="#1e1e1e")

# Variables
host_var = tk.StringVar()
user_file_path = tk.StringVar()
pass_file_path = tk.StringVar()
output_file_path = tk.StringVar(value="results.txt")
thread_count = tk.IntVar(value=4)
max_retries = tk.IntVar(value=99)
delay = tk.DoubleVar(value=1)

# Top Frame - Inputs
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(padx=10, pady=10)

def add_label_entry(label_text, var, width=50):
    tk.Label(input_frame, text=label_text, fg="white", bg="#1e1e1e").pack()
    tk.Entry(input_frame, textvariable=var, width=width).pack()

add_label_entry("Target Host:", host_var)
add_label_entry("User List File:", user_file_path)
tk.Button(input_frame, text="Browse", command=lambda: browse_file(user_file_path)).pack()

add_label_entry("Password List File:", pass_file_path)
tk.Button(input_frame, text="Browse", command=lambda: browse_file(pass_file_path)).pack()

add_label_entry("Threads:", thread_count)
add_label_entry("Delay (s):", delay)
add_label_entry("Max Retries/User:", max_retries)
add_label_entry("Output File:", output_file_path)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="▶ Start Brute Force", bg="#007acc", fg="white", command=run_bruteforce, width=20).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="■ Stop", bg="#cc0000", fg="white", command=stop_bruteforce, width=10).pack(side=tk.LEFT)

# Output Frame
output_frame = tk.Frame(root, bg="#1e1e1e")
output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

output_area = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, bg="black", fg="#d4d4d4", font=("Consolas", 10))
output_area.pack(fill=tk.BOTH, expand=True)

# Color tags
output_area.tag_config("success", foreground="green")
output_area.tag_config("fail", foreground="red")
output_area.tag_config("warn", foreground="yellow")
output_area.tag_config("error", foreground="orange")
output_area.tag_config("normal", foreground="#d4d4d4")

root.mainloop()
