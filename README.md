# 🔐 Advanced SSH Brute Force Tool with GUI

A powerful and customizable Python-based SSH brute-force tool with an intuitive GUI built using `Tkinter`. This tool supports multi-threading, delay/retry control, real-time logging, and color-coded output highlighting. Designed for cybersecurity research and educational penetration testing.

---

## 📌 Features

- GUI interface for easier operation (start/stop with input fields).
- Multi-threaded brute-force attacks.
- Retry mechanism for unstable connections.
- Password generation mode (optional).
- Color-coded live console output.
- Result logging and failed attempt saving.

---

## 🖥️ GUI Preview

> Simple and clean interface powered by `Tkinter`  
> Start and stop buttons, file pickers, and real-time output view.

![Screenshot](https://raw.githubusercontent.com/shivakasula48/Advanced-SSH-Brute-Force-Tool/main/assets/screenshot.png) <!-- Update with your actual screenshot path -->

---

## ⚙️ Requirements

Ensure you have Python 3.7+ installed.

Install dependencies:

```bash
pip install paramiko colorama
```
## 🚀 How to Use

### 🔧 Command-line Mode:

```bash
python advance_ssh_brute.py <target-ip> -U userlist.txt -P passlist.txt --threads 4 --delay 1 --max-user-retries 5 --output results.txt
```
