# game.py
from typing import List, Optional

class Game:
    def __init__(self):
        # board indexes 0..8, values: 'X', 'O', or None
        self.reset()

    def reset(self):
        self.board: List[Optional[str]] = [None]*9
        self.current_winner: Optional[str] = None

    def make_move(self, idx: int, player: str) -> bool:
        if self.board[idx] is None:
            self.board[idx] = player
            self.current_winner = self.check_winner()
            return True
        return False

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def is_full(self) -> bool:
        return all(v is not None for v in self.board)

    def check_winner(self) -> Optional[str]:
        b = self.board
        lines = [
            (0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # cols
            (0,4,8), (2,4,6)            # diagonals
        ]
        for a,b_idx,c in lines:
            if self.board[a] and self.board[a] == self.board[b_idx] == self.board[c]:
                return self.board[a]
        return None

    def get_result(self):
        """Return 'X' if X wins, 'O' if O wins, 'draw' if draw, None if ongoing."""
        winner = self.check_winner()
        if winner:
            return winner
        if self.is_full():
            return 'draw'
        return None

    def get_winner_and_line(self):
        """Returns (winner, winning_line) where winning_line is tuple of (row1,col1), (row2,col2)"""
        b = self.board
        lines = [
            ((0,0), (0,2)), # top row
            ((1,0), (1,2)), # middle row
            ((2,0), (2,2)), # bottom row
            ((0,0), (2,0)), # left column
            ((0,1), (2,1)), # middle column
            ((0,2), (2,2)), # right column
            ((0,0), (2,2)), # diagonal
            ((0,2), (2,0))  # diagonal
        ]
        
        for start, end in lines:
            r1, c1 = start
            r2, c2 = end
            idx1 = r1 * 3 + c1
            idx2 = r2 * 3 + c2
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            idx_mid = mid_r * 3 + mid_c
            
            if (b[idx1] and b[idx1] == b[idx_mid] == b[idx2]):
                return b[idx1], (start, end)
                
        return None, None
