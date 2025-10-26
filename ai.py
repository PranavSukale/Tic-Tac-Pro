# ai.py
import random
from typing import List, Optional, Tuple
from game import Game

# Scores for minimax
SCORES = {'O': 1, 'X': -1, 'draw': 0}

def easy_move(game: Game) -> int:
    return random.choice(game.available_moves())

def minimax(game: Game, maximizing: bool) -> Tuple[int, Optional[int]]:
    """
    Returns (score, move_index)
    maximizing=True means AI (O) to play
    """
    result = game.get_result()
    if result is not None:
        # terminal
        return (SCORES[result], None)

    best_score = None
    best_move = None

    for move in game.available_moves():
        # simulate
        current_player = 'O' if maximizing else 'X'
        game.board[move] = current_player

        score, _ = minimax(game, not maximizing)

        # undo
        game.board[move] = None

        if best_score is None:
            best_score = score
            best_move = move
        else:
            if maximizing:
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

    return best_score, best_move

def best_move_minimax(game: Game) -> int:
    _, mv = minimax(game, True)
    # fallback
    if mv is None:
        return random.choice(game.available_moves())
    return mv

def medium_move(game: Game) -> int:
    # 50% chance strategic, else random
    if random.random() < 0.5:
        return best_move_minimax(game)
    return easy_move(game)

def hard_move(game: Game, randomness: float = 0.1) -> int:
    # randomness: chance to pick random move (to keep fair)
    if random.random() < randomness:
        return easy_move(game)
    return best_move_minimax(game)

def choose_move(game: Game, level: str) -> int:
    level = level.lower()
    if level == 'easy':
        return easy_move(game)
    elif level == 'medium':
        return medium_move(game)
    elif level == 'hard':
        # 10% randomness built-in
        return hard_move(game, randomness=0.1)
    else:
        return easy_move(game)
