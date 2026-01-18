import tkinter as tk
from tkinter import font
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")
        
        # Scores
        self.player_score = 0
        
        self.computer_score = 0
        self.ties = 0
        
        # Title
        title = tk.Label(root, text="🎮 ROCK PAPER SCISSORS 🎮", 
                        font=("Arial", 24, "bold"), 
                        bg="#1a1a2e", fg="#00d4ff")
        title.pack(pady=20)
        
        # Score Frame
        score_frame = tk.Frame(root, bg="#16213e")
        score_frame.pack(pady=10, padx=20, fill="x")
        
        self.score_label = tk.Label(score_frame, 
                                    text=f"You: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.ties}",
                                    font=("Arial", 16, "bold"),
                                    bg="#16213e", fg="white", pady=10)
        self.score_label.pack()
        
        # Result Display
        self.result_label = tk.Label(root, text="Make your choice!", 
                                    font=("Arial", 18, "bold"),
                                    bg="#1a1a2e", fg="#ffd700", 
                                    pady=20, height=2)
        self.result_label.pack()
        
        # Choices Display
        choices_frame = tk.Frame(root, bg="#1a1a2e")
        choices_frame.pack(pady=10)
        
        self.player_choice_label = tk.Label(choices_frame, text="❓", 
                                           font=("Arial", 50),
                                           bg="#16213e", fg="white",
                                           width=4, height=2)
        self.player_choice_label.grid(row=0, column=0, padx=20)
        
        vs_label = tk.Label(choices_frame, text="VS", 
                          font=("Arial", 20, "bold"),
                          bg="#1a1a2e", fg="#ff6b6b")
        vs_label.grid(row=0, column=1, padx=10)
        
        self.computer_choice_label = tk.Label(choices_frame, text="❓", 
                                             font=("Arial", 50),
                                             bg="#16213e", fg="white",
                                             width=4, height=2)
        self.computer_choice_label.grid(row=0, column=2, padx=20)
        
        # Buttons Frame
        buttons_frame = tk.Frame(root, bg="#1a1a2e")
        buttons_frame.pack(pady=30)
        
        # Choice buttons
        choices = [
            ("🪨\nROCK", "rock", "#e74c3c"),
            ("📄\nPAPER", "paper", "#3498db"),
            ("✂️\nSCISSORS", "scissors", "#2ecc71")
        ]
        
        for i, (text, choice, color) in enumerate(choices):
            btn = tk.Button(buttons_frame, text=text,
                          font=("Arial", 14, "bold"),
                          bg=color, fg="white",
                          width=10, height=4,
                          bd=0, cursor="hand2",
                          command=lambda c=choice: self.play(c))
            btn.grid(row=0, column=i, padx=10)
        
        # Reset Button
        reset_btn = tk.Button(root, text="🔄 RESET GAME",
                            font=("Arial", 12, "bold"),
                            bg="#ff6b6b", fg="white",
                            width=20, height=2,
                            bd=0, cursor="hand2",
                            command=self.reset_game)
        reset_btn.pack(pady=20)
        
        # Emojis for choices
        self.emojis = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
    
    def play(self, player_choice):
        # Get computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Update display
        self.player_choice_label.config(text=self.emojis[player_choice])
        self.computer_choice_label.config(text=self.emojis[computer_choice])
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores
        if "You Win" in result:
            self.player_score += 1
            self.result_label.config(text=result, fg="#2ecc71")
        elif "Computer Wins" in result:
            self.computer_score += 1
            self.result_label.config(text=result, fg="#e74c3c")
        else:
            self.ties += 1
            self.result_label.config(text=result, fg="#ffd700")
        
        # Update score display
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.ties}")
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a Tie! 🤝"
        
        if (player == 'rock' and computer == 'scissors') or \
           (player == 'paper' and computer == 'rock') or \
           (player == 'scissors' and computer == 'paper'):
            return "You Win! 🎉"
        else:
            return "Computer Wins! 🤖"
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.ties}")
        self.result_label.config(text="Make your choice!", fg="#ffd700")
        self.player_choice_label.config(text="❓")
        self.computer_choice_label.config(text="❓")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()