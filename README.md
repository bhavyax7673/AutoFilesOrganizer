# 🗂️ AutoFilesOrganizer - Python Project

This project automatically organizes files in your Downloads folder by moving them into designated directories based on their file types. It's perfect for keeping your workspace clean and organized, managing various files like images, videos, documents, and audio files.

## 🔧 Built By

**Bhavya Padaliya**  
GitHub: [github.com/bhavyax7673](https://github.com/bhavyax7673)

## 🚀 Features

- **Automatic File Organization**: Moves files from your Downloads folder to appropriate directories based on their extensions.
- **Customizable Directories**: Easily specify any target folder for monitoring and corresponding destination folders.
- **Runs Continuously**: The script runs in the background, checking for new files every hour and sorting them automatically.

## 🛠️ Installation

### 1. Install Python

Ensure you have Python installed on your system. Download it from the official [Python website](https://www.python.org/downloads/). During installation, make sure to check the option to "Add Python to PATH."

### 2. Clone This Repository

Use Git to clone the repository to your local machine:

```bash
git clone https://github.com/bhavyax7673/file-organizer.git
cd file-organizer
```

### 3. Run the Script: Run the script manually or set it to run in the background.

1. Manually

```bash
python main.py
```

2. Set It In The Background

```bash
pythonw main.py
```

## ⚙️ How It Works

- The script monitors the specified Downloads folder.
- Every hour, it scans for new files and moves them to the appropriate folders:
    - Images to Pictures
    - Videos to Videos
    - Documents to Documents
    - Audio Files to Audio
- The process repeats continuously to keep your Downloads folder organized.

## 👤 About Me

- I'm Bhavya Padaliya, a passionate Computer Science student, continually working on projects to enhance my programming skills. The File Organizer is a simple yet effective tool to maintain an organized workspace. Check out my other projects on GitHub!
