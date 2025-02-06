import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg='#2C3E50')  # Dark blue background

# Style constants
BUTTON_FONT = ("Helvetica", 24, "bold")
LABEL_FONT = ("Helvetica", 16)
BUTTON_COLOR = "#34495E"
HOVER_COLOR = "#2980B9"
X_COLOR = "#E74C3C"  # Red
O_COLOR = "#2ECC71"  # Green
TEXT_COLOR = "#ECF0F1"  # Light gray

# Game Variables
board = [""] * 9
current_player = "X"
winner = None
buttons = []

def check_win():
    global winner
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "":
            winner = board[a]
            highlight_winning_combination(a, b, c)
            status_label.config(text=f"Winner: {winner}", fg=X_COLOR if winner == "X" else O_COLOR)
            return True
    if "" not in board:
        status_label.config(text="It's a Tie!", fg=TEXT_COLOR)
        return True
    return False

def highlight_winning_combination(a, b, c):
    win_color = "#F1C40F"  # Yellow
    for i in (a, b, c):
        buttons[i].config(bg=win_color)

def button_hover(event):
    event.widget.config(bg=HOVER_COLOR)

def button_leave(event):
    if event.widget['text'] == "":
        event.widget.config(bg=BUTTON_COLOR)

def player_move(index):
    global current_player
    if board[index] == "" and winner is None:
        board[index] = current_player
        buttons[index].config(
            text=current_player,
            fg=X_COLOR if current_player == "X" else O_COLOR
        )
        if check_win():
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            return
        current_player = "O"
        status_label.config(text="Computer's Turn", fg=O_COLOR)
        root.after(500, computer_move)

def computer_move():
    global current_player
    empty_cells = [i for i in range(9) if board[i] == ""]
    if empty_cells and winner is None:
        move = random.choice(empty_cells)
        board[move] = "O"
        buttons[move].config(text="O", fg=O_COLOR)
        if check_win():
            if winner:
                messagebox.showinfo("Game Over", "Computer wins!")
            return
        current_player = "X"
        status_label.config(text="Player X's Turn", fg=X_COLOR)

def reset_game():
    global board, current_player, winner
    board = [""] * 9
    current_player = "X"
    winner = None
    status_label.config(text="Player X's Turn", fg=X_COLOR)
    for button in buttons:
        button.config(text="", bg=BUTTON_COLOR, fg=TEXT_COLOR)

# Create main frame
game_frame = tk.Frame(root, bg='#2C3E50', padx=20, pady=20)
game_frame.pack(expand=True)

# Create UI Grid
for i in range(9):
    btn = tk.Button(
        game_frame,
        text="",
        font=BUTTON_FONT,
        width=3,
        height=1,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        relief=tk.RAISED,
        borderwidth=3,
        command=lambda i=i: player_move(i)
    )
    btn.grid(row=i//3, column=i%3, padx=3, pady=3)
    btn.bind('<Enter>', button_hover)
    btn.bind('<Leave>', button_leave)
    buttons.append(btn)

# Status label with improved styling
status_label = tk.Label(
    game_frame,
    text="Player X's Turn",
    font=LABEL_FONT,
    bg='#2C3E50',
    fg=X_COLOR,
    pady=15
)
status_label.grid(row=3, column=0, columnspan=3)

# Reset Button with improved styling
reset_button = tk.Button(
    game_frame,
    text="New Game",
    font=LABEL_FONT,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    command=reset_game,
    relief=tk.RAISED,
    borderwidth=3,
    padx=20
)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

# Set minimum size for the window
root.minsize(300, 400)

# Run the Tkinter loop
root.mainloop()