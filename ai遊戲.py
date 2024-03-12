import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("井字遊戲")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"  # "X" 玩家開始
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text=" ", font=('normal', 40), height=2, width=5,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        self.update_status()

    def on_button_click(self, i):
        if self.board[i] == " " and self.current_player == "X":
            self.board[i] = "X"
            if self.check_for_win("X"):
                self.game_over("X")
                return
            self.update_board()
            self.ai_move()

    def ai_move(self):
        # 檢查AI能否贏
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_for_win("O"):
                    self.update_board()
                    self.game_over("O")
                    return
                else:
                    self.board[i] = " "
        
        # 阻止玩家勝利
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_for_win("X"):
                    self.board[i] = "O"
                    self.update_board()
                    return
                else:
                    self.board[i] = " "

        # 佔據中心
        if self.board[4] == " ":
            self.board[4] = "O"
            self.update_board()
            return

        # 佔據角落
        for i in [0, 2, 6, 8]:
            if self.board[i] == " ":
                self.board[i] = "O"
                self.update_board()
                return

        # 佔據邊
        for i in [1, 3, 5, 7]:
            if self.board[i] == " ":
                self.board[i] = "O"
                self.update_board()
                return

    def update_board(self):
        for i, button in enumerate(self.buttons):
            button['text'] = self.board[i]
        if " " not in self.board:
            self.game_over("Nobody")
        self.update_status()

    def check_for_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def game_over(self, winner):
        if winner != "Nobody":
            messagebox.showinfo("遊戲結束", f"玩家 {winner} 贏了!")
        else:
            messagebox.showinfo("遊戲結束", "平局!")
        self.reset_board()

    def update_status(self):
        self.window.title("井字遊戲")

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        self.update_board()

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
