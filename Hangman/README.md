# 🎮 Hangman Game --- Python Mini Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Pygame](https://img.shields.io/badge/Audio-Pygame-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Internship](https://img.shields.io/badge/Internship-CodeTechIT%20Solutions-red)

A fun and interactive **Hangman Game** built using **Python** and
**Tkinter**, featuring difficulty levels, real-time word fetching, audio
feedback, and a clean graphical interface.

This project was developed as part of my **Python Programming Internship
at CodeTechIT Solutions**.

------------------------------------------------------------------------

## 🧠 Objective

The objective of this project was to implement the classic **Hangman**
game while combining: - Backend game logic - GUI-based interaction - API
integration - Audio feedback

This project strengthened my understanding of **OOP**, **event-driven
programming**, **GUI design**, and **multithreading** in Python.

------------------------------------------------------------------------

## 🛠 Technologies & Libraries Used

  Component   Description
  ----------- -------------------------------------------
  Python      Core programming language
  Tkinter     GUI framework
  Pygame      Sound effects & background music
  Requests    Fetch random words from external API
  Threading   Prevent UI blocking during audio playback

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Hangman/
│── gui.py          # Main GUI application
│── logic.py        # Game logic & rules
│── sounds/         # Sound effects & music
│── assets/         # Images / UI assets (if any)
│── requirements.txt
│── README.md
```

------------------------------------------------------------------------

## ⚙️ Features

-   🎚 **Difficulty Levels** -- Easy, Medium, Hard (dynamic lives & word
    length)
-   🔊 **Audio Feedback** -- Correct/incorrect guess, win/loss sounds
-   🧠 **Smart Word Logic** -- API-based word fetch with offline
    fallback
-   💻 **Responsive GUI** -- Built with Tkinter widgets
-   🧵 **Multithreading** -- Smooth audio without freezing UI
-   ❌ **Robust Error Handling** -- Handles invalid input & API failures

------------------------------------------------------------------------

## 🔧 Setup Instructions

### 1️⃣ Install Python

Download from: https://www.python.org/

### 2️⃣ Install Required Libraries

``` bash
pip install pygame requests
```

> Note: `tkinter` comes pre-installed with most Python versions.

### 3️⃣ Run the Game

``` bash
python gui.py
```

------------------------------------------------------------------------

## 🎨 Screenshots

### 🖥 Terminal Command
<p align="center">
  <img src="screenshots/terminal-command.jpg" width="700">
</p>

---

### 🎬 Splash Screen
<p align="center">
  <img src="screenshots/splash-screen-1.jpg" width="700">
  <img src="screenshots/splash-screen-2.jpg" width="700">
  <img src="screenshots/splash-screen-3.jpg" width="700">
</p>

---

### 🎯 Right & Wrong Guess Feedback
<p align="center">
  <img src="screenshots/right-guess.jpg" width="450">
  <img src="screenshots/wrong-guess.jpg" width="450">
</p>

---

### 🏆 Win & ❌ Lose Screens
<p align="center">
  <img src="screenshots/win-screen.jpg" width="450">
  <img src="screenshots/lose-screen.jpg" width="450">
</p>

---

### ⚠️ Invalid Input Handling
<p align="center">
  <img src="screenshots/invalid-input.jpg" width="700">
  <img src="screenshots/invalid-input-2.jpg" width="700">
</p>

------------------------------------------------------------------------

## 💡 Key Learnings

-   Applied **OOP principles** in a real project
-   Designed interactive GUIs with **Tkinter**
-   Integrated **live API data**
-   Improved responsiveness using **threading**
-   Enhanced UX with **audio integration**

------------------------------------------------------------------------

## 📌 Future Improvements

-   🏆 Leaderboard / Score tracking
-   🎨 Enhanced UI with images & animations
-   📦 Convert into `.exe` using **PyInstaller**
-   🌐 Online multiplayer mode (stretch goal)

------------------------------------------------------------------------

## 🧑‍💻 Author

**Krishna**\
Python Programming Intern -- CodeTechIT Solutions

------------------------------------------------------------------------

⭐ If you enjoyed this project, feel free to give it a star!
