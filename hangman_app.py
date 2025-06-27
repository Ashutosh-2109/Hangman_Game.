import tkinter as tk
from tkinter import messagebox
import random

# Initialize main app window
app = tk.Tk()
app.title("Ashu Hangman Game")
app.geometry("300x400")

# Word choice
arr_words=[
    "apple", "banana", "orange", "grape", "mango", "peach", "lemon", "cherry", "melon", "berry",
    "house", "chair", "table", "window", "door", "floor", "roof", "wall", "garden", "kitchen",
    "happy", "sad", "angry", "tired", "excited", "scared", "nervous", "calm", "brave", "shy",
    "dog", "cat", "fish", "bird", "horse", "cow", "sheep", "goat", "lion", "tiger",
    "blue", "red", "green", "yellow", "pink", "purple", "black", "white", "brown", "orange",
    "summer", "winter", "spring", "autumn", "morning", "evening", "night", "noon", "sunrise", "sunset",
    "water", "fire", "earth", "air", "sky", "cloud", "rain", "snow", "wind", "storm",
    "school", "teacher", "student", "book", "pencil", "paper", "desk", "board", "lesson", "homework",
    "car", "bus", "train", "plane", "boat", "bike", "truck", "taxi", "subway", "scooter",
    "music", "song", "dance", "guitar", "piano", "drum", "violin", "flute", "trumpet", "singer"
  ]

word=arr_words[random.randint(0, len(arr_words)-1)].upper()

# Game variables
display = ["_"] * len(word)
lives = 0

# UI Elements
label_word = tk.Label(app, text=" ".join(display), font=("Arial", 24))
label_word.pack(pady=20)

entry_guess = tk.Entry(app, font=("Arial", 16))
entry_guess.pack()

label_status = tk.Label(app, text="", font=("Arial", 14))
label_status.pack(pady=10)

label_drawing = tk.Label(app, text="", font=("Courier", 14), justify="left")
label_drawing.pack()

# Hangman drawings
def get_hangman_drawing(life):
    drawings = [
        "",
        "|\n|\n|\n|",
        "_\n|   |\n|\n|\n|",
        "_\n|   |\n|  O\n|\n|",
        "_\n|   |\n|  O\n|  | \n|",
        "_\n|   |\n|  O\n| /|\\ \n|",
        "_\n|   |\n|  O\n| /|\\ \n| / \\"
    ]
    return drawings[life]

# Guess logic
def submit_guess():
    global lives
    guess = entry_guess.get().upper()
    entry_guess.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        label_status.config(text="Enter a single letter.")
        return
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        label_word.config(text=" ".join(display))
        if display == list(word):
            messagebox.showinfo("You Win!", "Congratulations, you guessed the word!")
            app.quit()
    else:
        lives += 1
        label_drawing.config(text=get_hangman_drawing(lives))
        if lives == 6:
            messagebox.showerror("Game Over", "You've been hanged!\nThe word was: " + "".join(word))
            app.quit()

# Button
btn_submit = tk.Button(app, text="Submit Guess", command=submit_guess, font=("Arial", 14))
btn_submit.pack(pady=10)

# Start game
app.mainloop()
