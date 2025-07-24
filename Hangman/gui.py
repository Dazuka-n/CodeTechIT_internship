
import tkinter as tk
from tkinter import messagebox
from logic import HangmanGame
import pygame
import threading


# Initialize pygame mixer globally
pygame.mixer.init()

# Sound effects dictionary
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

# Set volume for background tracks
sounds["bg_easy"].set_volume(0.7)
sounds["bg_medium"].set_volume(0.3)
sounds["bg_hard"].set_volume(0.3)


def play_intro_sound():
    sounds["intro"].play(loops=-1)  # loop until difficulty is selected


def stop_intro_sound():
    sounds["intro"].stop()


def play_button_click():
    sounds["click"].play()


def play_background_music(level):
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

    label = tk.Label(splash, text="🎮 Hangman Game 🎮", font=("Arial", 22, "bold"), fg="white", bg="#333")
    label.pack(expand=True)

    splash.after(2000, splash.destroy)


class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎮")
        self.root.geometry("600x500")
        self.root.configure(bg="#898AC4")
        self.root.resizable(True, True)
        self.game = None
        self.start_screen()

    def start_screen(self):
     self.clear_screen()

     tk.Label(
        self.root,
        text="🎉 Welcome to Hangman 🎉",
        font=("Times", 45, "bold"),
        fg="black",
        bg="#898AC4"
     ).pack(pady=40)

     tk.Label(
        self.root,
        text="~ Choose Difficulty Level ~",
        font=("Georgia", 28),
        fg="black",
        bg="#898AC4"
     ).pack(pady=15)

     levels = [
        ("Easy", "#DDEB9D", "#A0C878"),
        ("Medium", "#FADA7A", "#FF9B45"),
        ("Hard", "#FFAAAA", "#EA5B6F")
     ]

     for level_name, normal_color, hover_color in levels:
        btn = tk.Button(
            self.root,
            text=level_name,
            font=("Gerogia", 25),
            width=16,
            pady=20,
            bg=normal_color,
            fg="black",
            activebackground=hover_color,
            cursor="hand2",
            command=lambda l=level_name.lower(): self.start_game(l)
        )
        btn.pack(pady=20)

        # Add hover effect
        def on_enter(e, b=btn, c=hover_color): b.config(bg=c)
        def on_leave(e, b=btn, c=normal_color): b.config(bg=c)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def start_game(self, difficulty):
        play_button_click()
        stop_intro_sound()
        stop_background_music()
        play_background_music(difficulty)

        self.game = HangmanGame(difficulty=difficulty)
        self.clear_screen()

        self.word_label = tk.Label(self.root, text=self.game.get_display_word(), font=("Courier", 32, "bold"), bg="#898AC4")
        self.word_label.pack(pady=30)

        self.lives_label = tk.Label(self.root, text=f"Lives Left: {self.game.get_lives()}", font=("Arial", 16, "bold"), bg="#898AC4", fg="#e84118")
        self.lives_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 20), width=3, justify="center", bg="white", fg="black", relief="sunken")
        self.entry.pack(pady=15)
        self.entry.focus()

        tk.Button(
            self.root,
            text="Guess",
            font=("Arial", 14),
            bg="#273c75",
            fg="white",
            padx=10,
            pady=5,
            command=self.make_guess
        ).pack(pady=10)

        self.guessed_label = tk.Label(self.root, text="Guessed: ", font=("Arial", 14), bg="#898AC4", fg="#2f3640")
        self.guessed_label.pack(pady=20)

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
                if self.game.get_lives() == 0:
                    self.word_label.config(fg="red")
                    sounds["lost"].play()
                else:
                    self.word_label.config(fg="green")
                    sounds["won"].play()
                messagebox.showinfo("Game Over", message)
                self.start_screen()

    def update_ui(self):
        self.word_label.config(text=self.game.get_display_word())
        self.lives_label.config(text=f"Lives Left: {self.game.get_lives()}")
        guessed = ', '.join(self.game.get_guessed_letters())
        self.guessed_label.config(text=f"Guessed: {guessed}")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # Start intro music in separate thread
    threading.Thread(target=play_intro_sound).start()
    show_splash(root)

    root.after(2200, lambda: (
        root.deiconify(),
        HangmanGUI(root)
    ))

    root.mainloop()