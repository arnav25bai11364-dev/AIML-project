import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

moves = ["rock", "paper", "scissors"]
user_history = []
pattern_memory = {}

def get_counter(move):
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[move]

def predict_by_pattern():
    if len(user_history) < 2:
        return None
    pattern = tuple(user_history[-2:])
    if pattern in pattern_memory:
        return max(pattern_memory[pattern], key=pattern_memory[pattern].get)
    return None

def update_pattern_memory():
    if len(user_history) < 3:
        return
    pattern = tuple(user_history[-3:-1])
    next_move = user_history[-1]
    if pattern not in pattern_memory:
        pattern_memory[pattern] = {"rock": 0, "paper": 0, "scissors": 0}
    pattern_memory[pattern][next_move] += 1

def predict_by_frequency():
    if not user_history:
        return None
    freq = {"rock": 0, "paper": 0, "scissors": 0}
    for m in user_history:
        freq[m] += 1
    return max(freq, key=freq.get)

def get_ai_move():
    predicted = predict_by_pattern() or predict_by_frequency()
    if not predicted:
        return random.choice(moves)
    return get_counter(predicted) if random.random() < 0.8 else random.choice(moves)

def get_winner(user, ai):
    if user == ai:
        return "Draw"
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        return "You Win 🎉"
    else:
        return "AI Wins 🤖"

# ---------------- GUI ---------------- #

def play(user_move):
    user_history.append(user_move)
    update_pattern_memory()
    ai_move = get_ai_move()

    result = get_winner(user_move, ai_move)

    user_label.configure(text=f"You: {user_move}")
    ai_label.configure(text=f"AI: {ai_move}")
    result_label.configure(text=result)

# App window
app = ctk.CTk()
app.title("AI Rock Paper Scissors")
app.geometry("400x400")

title = ctk.CTkLabel(app, text="🎮 AI Rock Paper Scissors", font=("Arial", 20))
title.pack(pady=20)

user_label = ctk.CTkLabel(app, text="You: ", font=("Arial", 16))
user_label.pack(pady=5)

ai_label = ctk.CTkLabel(app, text="AI: ", font=("Arial", 16))
ai_label.pack(pady=5)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 18, "bold"))
result_label.pack(pady=10)

# Buttons
frame = ctk.CTkFrame(app)
frame.pack(pady=20)

rock_btn = ctk.CTkButton(frame, text="Rock", command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = ctk.CTkButton(frame, text="Paper", command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = ctk.CTkButton(frame, text="Scissors", command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

app.mainloop()