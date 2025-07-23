import random
import requests

DIFFICULTY_SETTINGS = {
    "easy": {"min_length": 3, "max_length": 5, "lives": 8},
    "medium": {"min_length": 6, "max_length": 8, "lives": 6},
    "hard": {"min_length": 9, "max_length": 100, "lives": 4}
}

class HangmanGame:
    def __init__(self, difficulty="medium", use_api=True):
        self.difficulty = difficulty.lower()
        self.use_api = use_api
        self.word = self._choose_word()
        self.display = ["_" for _ in self.word]
        self.guessed_letters = set()
        self.remaining_lives = DIFFICULTY_SETTINGS[self.difficulty]["lives"]
        self.max_lives = self.remaining_lives
        self.game_over = False

    def _fetch_words_from_api(self, word_length, count=10):
        try:
            url = f"https://random-word-api.herokuapp.com/word?number={count}&length={word_length}"
            response = requests.get(url)
            if response.status_code == 200:
                words = response.json()
                return words
            else:
                print("⚠️ API Error: Using default fallback words.")
        except:
            print("⚠️ Failed to fetch from API.")
        return []

    def _choose_word(self):
        setting = DIFFICULTY_SETTINGS[self.difficulty]
        word = ""

        if self.use_api:
            for length in range(setting["min_length"], setting["max_length"] + 1):
                words = self._fetch_words_from_api(length)
                if words:
                    word = random.choice(words)
                    break

        if not word:  # fallback
            fallback_words = ["apple", "banana", "dragon", "dishwasher", "bridge", "magma"]
            word = random.choice(fallback_words)

        return word.lower()

    def guess_letter(self, letter):
        if self.game_over or not letter.isalpha() or len(letter) != 1:
            return False, "Invalid input."

        letter = letter.lower()

        if letter in self.guessed_letters:
            return False, f"You already guessed '{letter}'."

        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.display[i] = letter
            if "_" not in self.display:
                self.game_over = True
                return True, "🎉 You win!"
            return True, f"Good guess: {letter}"
        else:
            self.remaining_lives -= 1
            if self.remaining_lives <= 0:
                self.game_over = True
                return False, f"💀 You lost! The word was '{self.word}'."
            return False, f"Wrong guess: {letter}. Lives left: {self.remaining_lives}"

    def get_display_word(self):
        return " ".join(self.display)

    def is_game_over(self):
        return self.game_over

    def get_word(self):
        return self.word

    def get_lives(self):
        return self.remaining_lives

    def get_max_lives(self):
        return self.max_lives

    def get_guessed_letters(self):
        return sorted(self.guessed_letters)