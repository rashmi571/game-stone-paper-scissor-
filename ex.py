import tkinter as tk
import random

choices = ["stone🪨","paper📄","secissor✂️"]

user_score=0
computer_score=0

def play(user_choice):
    global user_score ,computer_score
    
    computer_choice=random.choice(choices)
    result.set(f"computer choice : {computer_choice}")
    
    if user_choice == computer_choice:
        status.set("🤝Tie")
        status_label.config(fg="orange",font=("Arial",30,"bold"))
    
    elif (
        (user_choice == "stone🪨" and computer_choice == "secissor✂️")or
        (user_choice == "paper📄" and computer_choice == "stone🪨") or
        (user_choice == "secissor✂️" and computer_choice == "paper📄")
    ):    
        status.set("🎉you win!")
        user_score += 1
        status_label.config(fg="orange",font=("Arial",30,"bold"))
    else:
        status.set("💻computer win!")
        computer_score += 1
        status_label.config(fg="lightgreen",font=("Arial",30,"bold"))
            
    score.set(f"⭐score -> 🧑You : {user_score} | 🤖computer : {computer_score}")
 
 #---------------------gui part--------------------   
root=tk.Tk()
root.title("🎮stone paper secissor")
root.geometry("400x350")
root.configure(bg="#1e1e2f")   # dark blue
    
tk.Label(
    root,
    text="🎮stone paper secissor",
    font=("Arial",50,"bold"),
    bg="#1e1e2f"
).pack(pady=10)
    
result=tk.StringVar()
tk.Label(root ,textvariable=result,fg="red",bg="#1e1e2f",font=("Arial",30,"bold")).pack()
    
status=tk.StringVar()
status_label = tk.Label(
    root,
    textvariable=status,
    fg="red",
    bg="#1e1e2f",
    font=("Arial",14)
)
status_label.pack(pady=5)

    
score=tk.StringVar()
score.set(f"⭐score -> 🧑You : 0 | 🤖computer : 0")
tk.Label(root ,textvariable=score,bg="yellow",width=50,height=3,font=("Arial",20)).pack(pady=5)
    
# Create a frame to hold buttons horizontally
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)

# Stone button
tk.Button(button_frame, text="stone🪨", width=10, height=3, bg="#1A0D0D", fg="white",
          font=("Arial",20,"bold"), activebackground="#ff3b2f", command=lambda: play("stone🪨")).pack(side="left", padx=5)

# Paper button
tk.Button(button_frame, text="paper📄", width=10, height=3, bg="#0D66AA", fg="white",
          font=("Arial",20,"bold"), activebackground="#ff3b2f", command=lambda: play("paper📄")).pack(side="left", padx=5)

# Scissor button
tk.Button(button_frame, text="secissor✂️", width=10, height=3, bg="#ff6f61", fg="white",
          font=("Arial",20,"bold"), activebackground="#ff3b2f", command=lambda: play("secissor✂️")).pack(side="left", padx=5)

root.mainloop()