# 🧠 Task Automation -- File Organizer Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-ff4b4b?logo=streamlit)
![Automation](https://img.shields.io/badge/Type-Task_Automation-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Internship](https://img.shields.io/badge/Internship-CodeTechIT%20Solutions-orange)

A smart and lightweight **File Organizer Tool** built using **Python**
and **Streamlit** that automatically organizes files in a selected
directory into categorized folders such as Images, Documents, Videos,
Audio, and more.

This project was developed as part of my **Python Programming Internship
at CodeTechIT Solutions**.

------------------------------------------------------------------------

## 🎯 Project Objective

The objective of this project is to:

-   📁 Automatically categorize files based on file extensions
-   🧹 Clean up cluttered directories efficiently
-   🗑 Delete empty folders after organization
-   🌐 Provide a simple web interface for non-technical users

------------------------------------------------------------------------

## 🚀 How It Works

The project consists of **two main components**:

### 🔧 Backend Logic (`logic.py`)

-   Detects file types using extensions
-   Moves files into appropriate category folders
-   Traverses subdirectories
-   Deletes empty folders after sorting

### 🖥 Frontend Interface (`app.py`)

-   Built with **Streamlit**
-   Allows directory path input
-   Supports multiple file uploads
-   Displays real-time logs of operations performed

------------------------------------------------------------------------

## 🧰 Technologies & Libraries Used

  Tool / Library   Purpose
  ---------------- ---------------------------
  Python           Core programming language
  Streamlit        Web-based UI
  os               Directory & path handling
  shutil           File moving operations

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Install Python

Download from: https://www.python.org/downloads/

### 2️⃣ Install Required Library

``` bash
pip install streamlit
```

### 3️⃣ Run the Application

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## ✨ Features

-   📁 **Directory Path Input**
-   📤 **Multiple File Uploads**
-   🚀 **One-Click File Organization**
-   🧾 **Log Viewer for Actions**
-   🧹 **Automatic Empty Folder Deletion**
-   🎨 **Clean, Dark-Mode UI**

------------------------------------------------------------------------

## 📂 File Categories

  Category      Extensions
  ------------- -----------------------
  Images        .jpg, .png, .gif
  Documents     .pdf, .docx, .txt
  Videos        .mp4, .mkv, .avi
  Audio         .mp3, .wav, .aac
  Archives      .zip, .rar, .7z
  Executables   .exe, .msi
  Scripts       .py, .js, .html, .css
  Others        Uncategorized files

------------------------------------------------------------------------

## 🎨 Screenshots

-   📂 Unorganized Folder
-   🖥 Terminal Command
-   🌐 Streamlit Interface
-   📤 File Upload
-   📁 Organized Folder
-   🗑 Deleted Empty Folders

*(Add screenshots here for better presentation)*

------------------------------------------------------------------------

## 💡 Learnings

-   File system automation with Python
-   Directory traversal and cleanup logic
-   Building user-friendly tools with Streamlit
-   Handling edge cases and errors gracefully

------------------------------------------------------------------------

## 📌 Future Enhancements

-   Custom category creation
-   Undo / rollback feature
-   Scheduling automation tasks
-   Cloud & cross-platform support
-   Drag-and-drop file support

------------------------------------------------------------------------

## 🧑‍💻 Author

**Krishna**\
Python Programming Intern -- CodeTechIT Solutions

------------------------------------------------------------------------

⭐ If you found this project useful, give it a star!
