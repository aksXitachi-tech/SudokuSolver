import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def get_board_from_ui():
    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            value = entry_widgets[row][col].get()
            current_row.append(int(value) if value else 0)
        board.append(current_row)
    return board


def display_solution(board):
    for row in range(9):
        for col in range(9):
            entry_widgets[row][col].delete(0, tk.END)
            entry_widgets[row][col].insert(0, str(board[row][col]))


def solve_sudoku():
    board = get_board_from_ui()
    if solve(board):
        display_solution(board)
    else:
        messagebox.showinfo("No Solution", "This Sudoku puzzle has no solution!")


def clear_board():
    for row in range(9):
        for col in range(9):
            entry_widgets[row][col].delete(0, tk.END)


def fill_3x3_boxes_with_color():
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            for i in range(3):
                for j in range(3):
                    entry_widgets[row + i][col + j].config(bg="lightgreen")


def draw_bold_grid_lines(canvas):
    canvas.create_line(179, 0, 179, 530, width=2, fill="black")  
    canvas.create_line(365, 0, 365, 530, width=2, fill="black")  

    canvas.create_line(0, 180, 540, 180, width=2, fill="black")  
    canvas.create_line(0, 360, 540, 360, width=2, fill="black")  


window = tk.Tk()
window.title("Sudoku Solver")
window.geometry("550x650")  

title_label = tk.Label(window, text="Sudoku Solver", font=("Arial", 24, "bold"), pady=20)
title_label.grid(row=0, column=0, columnspan=9)

frame = tk.Frame(window)
frame.grid(row=1, column=0, columnspan=9, padx=10, pady=10)

canvas = tk.Canvas(frame, width=540, height=540)
canvas.grid(row=0, column=0, rowspan=9, columnspan=9)
draw_bold_grid_lines(canvas) 

entry_widgets = []

for row in range(9):
    row_entries = []
    for col in range(9):
        entry = tk.Entry(frame, width=4, font=("Arial", 18), borderwidth=2, relief="solid", justify="center")
        entry.grid(row=row, column=col, padx=2, pady=2)  
        row_entries.append(entry)
    entry_widgets.append(row_entries)

fill_3x3_boxes_with_color()

solve_button = tk.Button(window, text="Solve", font=("Arial", 16), width=10, height=2, bg="#4CAF50", fg="white", command=solve_sudoku)
solve_button.grid(row=10, column=3, columnspan=3, pady=10)

clear_button = tk.Button(window, text="Clear", font=("Arial", 16), width=10, height=2, bg="#f44336", fg="white", command=clear_board)
clear_button.grid(row=10, column=6, columnspan=3, pady=10)

status_label = tk.Label(window, text="Enter a Sudoku puzzle to solve", font=("Arial", 14), pady=10)
status_label.grid(row=11, column=0, columnspan=9)

window.mainloop()
