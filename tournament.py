# tournament.py
from typing import List, Dict

# Scoring: win=2, draw=1, loss=0
SCORES = {'win': 2, 'draw': 1, 'loss': 0}

class Tournament:
    def __init__(self, rounds: List[str] = None):
        # list of levels in order
        self.rounds = rounds or ['easy', 'medium', 'hard']
        self.current_round_idx = 0
        self.player_points = 0
        self.history: Dict[int, Dict] = {}  # round -> details

    def current_level(self) -> str:
        return self.rounds[self.current_round_idx]

    def record_result(self, result: str):
        # result: 'X' or 'O' or 'draw' ('X' player, 'O' ai)
        level = self.current_level()
        round_no = self.current_round_idx + 1
        if result == 'X':
            pts = SCORES['win']
            outcome = 'player_win'
        elif result == 'draw':
            pts = SCORES['draw']
            outcome = 'draw'
        else:
            pts = SCORES['loss']
            outcome = 'ai_win'
        self.player_points += pts
        self.history[round_no] = {'level': level, 'outcome': outcome, 'points_awarded': pts}
        self.current_round_idx += 1

    def finished(self) -> bool:
        return self.current_round_idx >= len(self.rounds)

    def reset(self):
        self.current_round_idx = 0
        self.player_points = 0
        self.history = {}

    def get_title(self) -> str:
        pts = self.player_points
        max_pts = len(self.rounds) * 2
        pct = pts / max_pts
        if pct == 1.0:
            return "Grand Master"
        if pct >= 0.75:
            return "Champion"
        if pct >= 0.5:
            return "Strategist"
        if pct >= 0.25:
            return "Rising Player"
        return "Beginner"
