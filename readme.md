# 🔍 Python Port Scanner

This is a beginner-friendly network port scanner built with Python. It scans a range of ports on a target IP address to check whether each port is open or closed.

## ✅ Features

- Scans a **custom port range** (with validation)
- Shows **real-time progress** for each port
- Saves results to a **timestamped `.txt` file**
- Displays total **scan duration**
- Fully built using only the Python standard library

## Requirements

No external libraries needed — works with Python 3+

## How to Run

1. Download or clone the repository
2. Run the script in a terminal:

```bash
python port_scanner.py


Enter:

Target IP (e.g., 127.0.0.1)

Starting port (e.g., 20)

Ending port (e.g., 80)

Results will be printed on screen and saved to a file like:

Copy
Edit
port_scan_2025-05-06_15-20-55.txt
📄 Example Output
vbnet
Copy
Edit
=== Python Port Scanner ===
Target: 127.0.0.1
Scanning ports 20 to 80

Scanning port 22...
Port 22 is closed.
...
Scan completed in 4.32 seconds
💡 What I Learned
Basics of network protocols (TCP/IP)

How to use Python’s socket and time modules

Input validation and user-friendly design

Writing clean, real-world CLI tools

📁 Project by: [Lowluds]
🔗 GitHub: https://github.com/yourusername/python-port-scanner