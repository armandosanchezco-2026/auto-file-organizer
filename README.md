# Auto File Organizer

A lightweight Python tool that automatically organizes a folder full of files by sorting them into subfolders based on file type (images, videos, documents, audio, archives, etc.). Ideal for keeping your Downloads folder clean and structured.

## 🚀 Features
- Automatically detects file types
- Creates subfolders dynamically
- Moves files safely without overwriting
- Generates a detailed log of all operations
- Works on Windows, macOS, and Linux
- Simple and clean command‑line interface

## 📦 Installation
Clone the repository:

git clone https://github.com/armandosanchezco-2026/auto-file-organizer.git
cd auto-file-organizer

No external dependencies are required — the script uses only Python’s standard library.

## 🧭 Usage
Run the script and pass the folder you want to organize:

python organizer.py "C:/Users/YourUser/Downloads"

You can target any folder on your system.

## 📁 Example Output Structure
After running the script, your folder may look like this:

Downloads/  
├── images/  
├── videos/  
├── documents/  
├── audio/  
├── archives/  
├── others/  
└── organizer_log.txt  

## 🛠 How It Works
1. The script scans all files in the target directory.
2. It determines each file’s category based on its extension.
3. It creates the necessary subfolders (if they don’t already exist).
4. Files are moved into their corresponding category folders.
5. A log file is generated with timestamps and actions performed.

## 📌 Ideal For
- Cleaning messy Downloads folders
- Organizing desktops
- USB drives
- Mixed project folders
- Automating repetitive file‑sorting tasks

## 📄 License
This project is released under the MIT License. You are free to use, modify, and distribute it.
