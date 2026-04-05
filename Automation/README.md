<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=4,14,24&height=200&section=header&text=File%20Organizer%20Tool&fontSize=58&fontColor=ffffff&fontAlignY=50&desc=%F0%9F%97%82%EF%B8%8F%20Clutter%20in.%20%20Order%20out.%20%20Every%20time.&descAlignY=70&descSize=17&animation=blinking" width="100%"/>

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Automation](https://img.shields.io/badge/Type-Task_Automation-8B5CF6?style=for-the-badge)](.)
[![Status](https://img.shields.io/badge/Status-Completed_✓-22C55E?style=for-the-badge)](.)
[![Live App](https://img.shields.io/badge/Live-task--automation.streamlit.app-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://task-automation.streamlit.app)

</div>

---

## 🧹 What It Does

**File Organizer Tool** is a lightweight automation utility that takes a messy, cluttered directory and sorts every file into the right folder — automatically — with zero manual effort.

Point it at any folder. Click organize. Done.

```
📁 Downloads/  (before)              📁 Downloads/  (after)
├── resume.pdf                       ├── 📄 Documents/
├── photo.jpg                        │   └── resume.pdf
├── video.mp4                        ├── 🖼️ Images/
├── script.py                        │   └── photo.jpg
├── archive.zip                      ├── 🎬 Videos/
└── song.mp3                         │   └── video.mp4
                                     ├── 💻 Scripts/
                                     │   └── script.py
                                     ├── 📦 Archives/
                                     │   └── archive.zip
                                     └── 🎵 Audio/
                                         └── song.mp3
```

Empty folders left behind? Automatically detected and deleted.

---

## 📂 File Categories

<div align="center">

| Category | Extensions |
|:---:|---|
| 🖼️ Images | `.jpg` `.png` `.gif` `.bmp` `.svg` `.webp` |
| 📄 Documents | `.pdf` `.docx` `.txt` `.xlsx` `.pptx` `.csv` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` `.mov` `.wmv` |
| 🎵 Audio | `.mp3` `.wav` `.aac` `.flac` `.ogg` |
| 📦 Archives | `.zip` `.rar` `.7z` `.tar` `.gz` |
| ⚙️ Executables | `.exe` `.msi` `.dmg` |
| 💻 Scripts | `.py` `.js` `.html` `.css` `.ts` `.sh` |
| 📁 Others | Everything else |

</div>

---

## 🏗️ How It Works

```mermaid
flowchart LR
    IN([📁 Input Directory\nor Uploaded Files]) --> BE

    subgraph BE [🔧 Backend — logic.py]
        direction TB
        SC[Scan files\ndetect extensions]
        SC --> CAT[Map to category\nImages / Docs / Video ...]
        CAT --> MV[Move files\nshutil.move]
        MV --> CLN[Delete empty\nfolders]
    end

    subgraph FE [🖥️ Frontend — app.py]
        direction TB
        DI[Directory path input]
        UL[Multiple file upload]
        LG[Real-time log viewer]
    end

    FE --> BE
    BE --> LG
    CLN --> OUT([✅ Organized\nDirectory])

    style BE fill:#1a2d4e,stroke:#3B82F6,color:#ffffff
    style FE fill:#1a3a2a,stroke:#22C55E,color:#ffffff
```

---

## 🗂️ Project Structure

```
Task_Automation/
├── app.py          ← Streamlit web interface
├── logic.py        ← File detection, moving, cleanup logic
├── requirements.txt
└── screenshots/
    ├── unorganised-folder.jpg
    ├── Terminal-Command-1.jpg
    ├── Terminal-Command-2.jpg
    ├── Streamlit-Browser.jpg
    ├── Upload-files-1.jpg
    ├── Upload-files-2.jpg
    └── organised-folder.jpg
```

---

## 🛠️ Tech Stack

<div align="center">

[![Python](https://skillicons.dev/icons?i=python)](https://python.org)

| Tool | Role |
|---|---|
| **Python** | Core language |
| **Streamlit** | Web-based UI — directory input, file upload, log display |
| **os** | Directory traversal and path handling |
| **shutil** | File move operations |

</div>

---

## 🚀 Getting Started

### 1️⃣ Install

```bash
pip install streamlit
```

### 2️⃣ Run

```bash
streamlit run app.py
```

✅ Opens at `http://localhost:8501`

---

## ✨ Features

| Feature | Description |
|---|---|
| 📁 **Directory Input** | Paste any local path to organize an existing folder |
| 📤 **File Upload** | Upload multiple files directly via the browser |
| 🚀 **One-Click Organize** | Single button triggers full sort + cleanup |
| 🧾 **Live Log Viewer** | Real-time action log — see every file move as it happens |
| 🧹 **Empty Folder Cleanup** | Automatically removes leftover empty directories |
| 🎨 **Dark Mode UI** | Clean, minimal dark-themed interface |

---

## 🎨 Screenshots

### 📂 Before — Unorganized Folder
<p align="center">
  <img src="screenshots/unorganised-folder.jpg" width="700"/>
</p>

---

### 🖥️ Running the App
<p align="center">
  <img src="screenshots/Terminal-Command-1.jpg" width="450"/>
  &nbsp;
  <img src="screenshots/Terminal-Command-2.jpg" width="450"/>
</p>

---

### 🌐 Streamlit Interface
<p align="center">
  <img src="screenshots/Streamlit-Browser.jpg" width="700"/>
</p>

---

### 📤 File Upload in Action
<p align="center">
  <img src="screenshots/Upload-files-1.jpg" width="450"/>
  &nbsp;
  <img src="screenshots/Upload-files-2.jpg" width="450"/>
</p>

---

### ✅ After — Organized Folder
<p align="center">
  <img src="screenshots/organised-folder.jpg" width="700"/>
</p>

> 🗑️ Empty folders are automatically detected and deleted after organization.

---

## 💡 Key Learnings

- File system automation with Python (`os`, `shutil`)
- Directory traversal and recursive cleanup logic
- Building user-friendly tools with Streamlit
- Handling edge cases — locked files, duplicates, unknown extensions

---

## 📌 Roadmap

- [ ] Custom category creation by user
- [ ] Undo / rollback last organization
- [ ] Scheduled automation (cron / task scheduler)
- [ ] Cloud storage support (Google Drive, Dropbox)
- [ ] Drag-and-drop file interface

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=4,14,24&height=80&section=footer" width="100%"/>

**Krishna** · Python Programming Intern · CodeTech IT Solutions

[![Live App](https://img.shields.io/badge/Try_it_Live-task--automation.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://task-automation.streamlit.app)

⭐ Found this useful? Give it a star!

</div>
