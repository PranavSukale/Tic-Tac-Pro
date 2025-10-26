# main.py
import pygame, sys, time
from game import Game
from ai import choose_move
from tournament import Tournament
import ui

pygame.init()
WINDOW_H = ui.SCREEN_SIZE + 100  # extra space for text/buttons
screen = pygame.display.set_mode((ui.SCREEN_SIZE, WINDOW_H))
pygame.display.set_caption("Tic-Tac-Tournament")
clock = pygame.time.Clock()

# Buttons
NEXT_BUTTON = pygame.Rect(ui.SCREEN_SIZE - 180, ui.SCREEN_SIZE + 20, 160, 40)
RESTART_BUTTON = pygame.Rect(ui.SCREEN_SIZE - 180, ui.SCREEN_SIZE + 65, 160, 30)

def run():
    game = Game()
    tournament = Tournament(rounds=['easy', 'medium', 'hard'])
    player_turn = True  # player is always X and moves first for each round
    level = tournament.current_level()
    msg = f"Round 1: {level.title()}"

    win_animated = False  # flag to avoid repeating animation

    while True:
        ui.draw_grid(screen)
        ui.draw_marks(screen, game.board)

        # bottom info
        ui.draw_message(screen, f"{msg}  |  Score: {tournament.player_points}")
        ui.draw_submessage(screen, "Player: X  |  AI: O  | Click on a cell to play.")
        ui.draw_button(screen, NEXT_BUTTON, "Next Round" if tournament.finished() else "Skip Round")
        ui.draw_button(screen, RESTART_BUTTON, "Restart Tournament")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # handle buttons
                if NEXT_BUTTON.collidepoint(mx, my):
                    if tournament.finished():
                        tournament.reset()
                        game.reset()
                        level = tournament.current_level()
                        msg = f"Round {tournament.current_round_idx+1}: {level.title()}"
                        player_turn = True
                        win_animated = False
                        continue
                    else:
                        tournament.record_result('O')  # AI wins by skip
                        if tournament.finished():
                            msg = f"Tournament finished! Title: {tournament.get_title()}"
                        else:
                            game.reset()
                            level = tournament.current_level()
                            msg = f"Round {tournament.current_round_idx+1}: {level.title()}"
                        player_turn = True
                        win_animated = False
                    continue

                if RESTART_BUTTON.collidepoint(mx, my):
                    tournament.reset()
                    game.reset()
                    level = tournament.current_level()
                    msg = f"Round {tournament.current_round_idx+1}: {level.title()}"
                    player_turn = True
                    win_animated = False
                    continue

                # click on the board
                idx = ui.pos_to_index((mx, my))
                if idx != -1 and game.board[idx] is None and game.get_result() is None:
                    if player_turn:
                        game.make_move(idx, 'X')
                        ui.draw_marks(screen, game.board)  # Immediately draw the new mark
                        pygame.display.flip()  # Update the display
                        player_turn = False

        # AI move
        if not player_turn and game.get_result() is None:
            pygame.display.flip()
            pygame.time.delay(350)
            level = tournament.current_level()
            ai_move = choose_move(game, level)
            game.make_move(ai_move, 'O')
            ui.draw_marks(screen, game.board)  # Immediately draw the AI's mark
            pygame.display.flip()  # Update the display
            player_turn = True

        # check result
        result = game.get_result()

        if result is not None:
            # 🏁 Animate win/draw once
            if not win_animated:
                winner, line = game.get_winner_and_line()
                if winner and line:
                    (r1, c1), (r2, c2) = line
                    ui.animate_winning_line(screen, (r1, c1), (r2, c2))
                else:
                    ui.play_draw_sound()
                win_animated = True

            # record result
            if not tournament.finished():
                tournament.record_result(result)

            # message
            if tournament.finished():
                msg = f"Tournament finished! Title: {tournament.get_title()} | Points: {tournament.player_points}"
                # Stop all sounds when tournament is finished
                pygame.mixer.stop()
            else:
                next_level = tournament.current_level()
                msg = f"Round {tournament.current_round_idx}: Complete. Next: {next_level.title()}"

            # show board for a second before moving
            pygame.display.flip()
            pygame.time.delay(900)

            # auto-reset if not finished
            if not tournament.finished():
                game.reset()
                level = tournament.current_level()
                msg = f"Round {tournament.current_round_idx+1}: {level.title()}"
                player_turn = True
                win_animated = False

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    run()
