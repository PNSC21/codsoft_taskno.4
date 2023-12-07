import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors Game")
        self.window.geometry("400x300")
        self.window.configure(bg="#f0f0f0")

        self.max_rounds = 5
        self.choices = ['rock', 'paper', 'scissors']

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.score_var = tk.StringVar()
        self.computer_choice_var = tk.StringVar()
        self.chances_var = tk.StringVar()

        self.reset_game()

        self.create_widgets()

    def create_widgets(self):
        # Styling
        label_style = {"font": ("Helvetica", 12), "bg": "#f0f0f0"}
        result_label_style = {"font": ("Helvetica", 16, "bold"), "bg": "#f0f0f0"}
        button_style = {"font": ("Helvetica", 10), "bg": "#4CAF50", "fg": "white"}

        # User choice label and dropdown
        user_label = tk.Label(self.window, text="Your choice:", **label_style)
        user_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        user_dropdown = tk.OptionMenu(self.window, self.user_choice_var, *self.choices)
        user_dropdown.config(bg="#4CAF50", fg="white")
        user_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Play button
        play_button = tk.Button(self.window, text="Play", command=self.play_game, **button_style)
        play_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # Computer choice label
        computer_label = tk.Label(self.window, textvariable=self.computer_choice_var, **label_style)
        computer_label.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

        # Result label
        result_label = tk.Label(self.window, textvariable=self.result_var, **result_label_style)
        result_label.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

        # Score label
        score_label = tk.Label(self.window, textvariable=self.score_var, **label_style)
        score_label.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

        # Chances label
        chances_label = tk.Label(self.window, textvariable=self.chances_var, **result_label_style)
        chances_label.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")

        # Play again button
        play_again_button = tk.Button(self.window, text="Play Again", command=self.reset_game, **button_style)
        play_again_button.grid(row=5, column=1, pady=10, sticky="nsew")

        # Configure column weights for resizing
        for i in range(3):
            self.window.columnconfigure(i, weight=1)

        # Configure row weights for resizing
        for i in range(6):
            self.window.rowconfigure(i, weight=1)

    def play_game(self):
        user_choice = self.user_choice_var.get().lower()
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.computer_choice_var.set(f"Computer chose: {computer_choice.capitalize()}")
        self.result_var.set(result)
        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_score(self):
        self.rounds_played += 1
        self.chances_var.set(f"Chances left: {self.max_rounds - self.rounds_played}")
        self.score_var.set(f"Score - You: {self.user_score}, Computer: {self.computer_score}")

        if self.rounds_played == self.max_rounds:
            self.end_session()

    def reset_game(self):
        self.rounds_played = 0
        self.user_score = 0
        self.computer_score = 0
        self.user_choice_var.set('')
        self.result_var.set('')
        self.computer_choice_var.set('')
        self.chances_var.set(f"Chances left: {self.max_rounds}")
        self.score_var.set(f"Score - You: 0, Computer: 0")

    def end_session(self):
        winning_status = self.determine_winning_status()
        self.result_var.set("Game Over! " + winning_status)
        self.chances_var.set('')
        self.score_var.set(f"Final Score - You: {self.user_score}, Computer: {self.computer_score}")

    def determine_winning_status(self):
        if self.user_score > self.computer_score:
            return "Congratulations! You win!"
        elif self.user_score < self.computer_score:
            return "Sorry, you lose. Better luck next time!"
        else:
            return "It's a draw. Good game!"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
