import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps
from logic import HangmanGame
import pygame
import threading
import os

# Initialize pygame mixer
pygame.mixer.init()

# Sound effects
sounds = {
    "intro": pygame.mixer.Sound("sounds/intro.wav"),
    "click": pygame.mixer.Sound("sounds/button_click.wav"),
    "correct": pygame.mixer.Sound("sounds/correct_guess.wav"),
    "wrong": pygame.mixer.Sound("sounds/wrong_guess.wav"),
    "won": pygame.mixer.Sound("sounds/game_won.wav"),
    "lost": pygame.mixer.Sound("sounds/game_lost.wav"),
    "bg_easy": pygame.mixer.Sound("sounds/bg_easy.wav"),
    "bg_medium": pygame.mixer.Sound("sounds/bg_medium.wav"),
    "bg_hard": pygame.mixer.Sound("sounds/bg_hard.wav"),
}

# Volume control
sounds["bg_easy"].set_volume(0.7)
sounds["bg_medium"].set_volume(0.3)
sounds["bg_hard"].set_volume(0.3)

def play_intro_sound():
    sounds["intro"].play(loops=-1)

def stop_intro_sound():
    sounds["intro"].stop()

def play_button_click():
    sounds["click"].play()

def play_background_music(level):
    stop_background_music()
    if level == "easy":
        sounds["bg_easy"].play(loops=-1)
    elif level == "medium":
        sounds["bg_medium"].play(loops=-1)
    elif level == "hard":
        sounds["bg_hard"].play(loops=-1)

def stop_background_music():
    for key in ["bg_easy", "bg_medium", "bg_hard"]:
        sounds[key].stop()

def show_splash(root):
    splash = tk.Toplevel(root)
    splash.geometry("400x300")
    splash.overrideredirect(True)
    splash.configure(bg="#333")
    tk.Label(splash, text="🎮 Hangman Game 🎮", font=("Arial", 22, "bold"), fg="white", bg="#333").pack(expand=True)
    splash.after(2000, splash.destroy)
class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎮")
        self.root.geometry("400x300")
        self.root.resizable(True, True)

        # Load background image (fixed size)
        bg_path = os.path.join("images", "bg.jpg")
        self.original_bg_image = Image.open(bg_path)
        self.bg_image = ImageTk.PhotoImage(self.original_bg_image)

        # Canvas Setup
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas_bg = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        self.widgets = []
        self.widget_refs = []  # Store (widget, relx, rely) for repositioning
        self.game = None

        self.root.bind("<Configure>", self.resize_bg)
        self.start_screen()

    def resize_bg(self, event):
        if event.widget != self.root:
            return

        new_width = event.width
        new_height = event.height

        # Resize background image
        resized = self.original_bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized)
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.itemconfig(self.canvas_bg, image=self.bg_image)

        # Reposition widgets relatively
        for (widget, relx, rely) in self.widget_refs:
            abs_x = int(new_width * relx)
            abs_y = int(new_height * rely)
            self.canvas.coords(widget, abs_x, abs_y)

    def clear_screen(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        self.canvas.delete("widget")

    def add_widget(self, widget, x, y):
        self.widgets.append(widget)
        self.canvas.create_window(x, y, window=widget, tags="widget")
        return widget

    def start_screen(self):
        self.clear_screen()

        self.add_widget(
            tk.Label(self.root, text="🎉 Welcome to Hangman 🎉", font=("Helvetica", 24, "bold"),
                     bg="#ffffff", fg="#2c3e50"), 300, 80
        )

        self.add_widget(
            tk.Label(self.root, text="Choose Difficulty Level", font=("Helvetica", 16),
                     bg="#ffffff"), 300, 130
        )

        levels = [("Easy", "#88d8b0"), ("Medium", "#fbc531"), ("Hard", "#e84118")]
        for i, (level, color) in enumerate(levels):
            btn = tk.Button(self.root, text=level, font=("Arial", 14), width=15,
                            bg=color, fg="white", relief="raised",
                            command=lambda l=level.lower(): self.start_game(l))
            self.add_widget(btn, 300, 180 + i * 60)

    def start_game(self, difficulty):
        play_button_click()
        stop_intro_sound()
        play_background_music(difficulty)

        self.game = HangmanGame(difficulty)
        self.clear_screen()

        self.word_label = self.add_widget(
            tk.Label(self.root, text=self.game.get_display_word(),
                     font=("Courier", 32, "bold"), bg="#ffffff"), 300, 80
        )

        self.lives_label = self.add_widget(
            tk.Label(self.root, text=f"Lives Left: {self.game.get_lives()}",
                     font=("Arial", 16, "bold"), bg="#ffffff", fg="#e84118"), 300, 140
        )

        self.entry = self.add_widget(
            tk.Entry(self.root, font=("Helvetica", 20), width=3, justify="center",
                     bg="#dcdde1", fg="black", relief="sunken"), 300, 190
        )
        self.entry.focus()

        self.add_widget(
            tk.Button(self.root, text="Guess", font=("Arial", 14),
                      bg="#273c75", fg="white", padx=10, pady=5,
                      command=self.make_guess), 300, 240
        )

        self.guessed_label = self.add_widget(
            tk.Label(self.root, text="Guessed: ", font=("Arial", 14),
                     bg="#ffffff", fg="#2f3640"), 300, 290
        )

    def make_guess(self):
        play_button_click()
        letter = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        valid, message = self.game.guess_letter(letter)
        self.update_ui()

        if not valid:
            sounds["wrong"].play()
            messagebox.showinfo("Oops!", message)
        else:
            if letter in self.game.word:
                sounds["correct"].play()

            if self.game.is_game_over():
                stop_background_music()
                end_sound = "lost" if self.game.get_lives() == 0 else "won"
                self.word_label.config(fg="red" if end_sound == "lost" else "green")
                sounds[end_sound].play()
                messagebox.showinfo("Game Over", message)
                self.start_screen()

    def update_ui(self):
        self.word_label.config(text=self.game.get_display_word())
        self.lives_label.config(text=f"Lives Left: {self.game.get_lives()}")
        guessed = ', '.join(self.game.get_guessed_letters())
        self.guessed_label.config(text=f"Guessed: {guessed}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    threading.Thread(target=play_intro_sound).start()
    show_splash(root)

    def launch_main_ui():
     root.deiconify()
     gui = HangmanGUI(root)
    
   

root.after(2200, launch_main_ui)


root.mainloop()
