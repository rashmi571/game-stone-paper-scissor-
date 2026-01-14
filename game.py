import tkinter as tk
import random

choices = ["stone", "paper", "scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result_text.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        status.set("🤝 Tie!")

    elif (
        (user_choice == "stone" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "stone")
    ):
        status.set("🎉 You win!")
        user_score += 1
    else:
        status.set("💻 Computer wins!")
        computer_score += 1

    score.set(f"Score → You: {user_score} | Computer: {computer_score}")

# ---------------- GUI PART ----------------

root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("400x350")

tk.Label(
    root,
    text="Stone Paper Scissors",
    font=("Arial", 18, "bold")
).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack()

status = tk.StringVar()
tk.Label(root, textvariable=status, font=("Arial", 14)).pack(pady=5)

score = tk.StringVar()
score.set("Score → You: 0 | Computer: 0")
tk.Label(root, textvariable=score).pack(pady=5)

# Buttons
tk.Button(root, text="Stone 🗿", width=15, command=lambda: play("stone")).pack(pady=5)
tk.Button(root, text="Paper 📄", width=15, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors ✂️", width=15, command=lambda: play("scissors")).pack(pady=5)

root.mainloop()
