Auto File Organizer
Automatically organizes a folder full of files by sorting them into subfolders based on file type (images, videos, documents, audio, archives, etc.).

Usage
bash
python organizer.py "C:/Users/YourUser/Downloads"
Features
Detects file types automatically

Creates folders dynamically

Moves files without overwriting

Generates a log with all operations

Works on Windows, macOS and Linux

Simple and clean CLI interface

Example Output Structure
Código
Downloads/
│
├── images/
├── videos/
├── documents/
├── audio/
├── archives/
├── others/
└── organizer_log.txt
Ideal For
Cleaning messy Downloads folders

Organizing desktops

USB drives

Mixed project folders

Automating repetitive file‑sorting tasks

How It Works
The script scans all files in the target folder, determines their category based on extension, creates the necessary subfolders, and moves each file accordingly. A log file is generated with all actions performed.