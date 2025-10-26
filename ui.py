import pygame
import os
import random
from typing import Tuple

pygame.init()
pygame.mixer.init()

# 🎨 Colors
WHITE = (245, 245, 245)
BLACK = (10, 10, 10)
LINE_COLOR = (30, 30, 30)
X_COLOR = (30, 90, 200)
O_COLOR = (200, 40, 40)
BG_COLOR = (220, 220, 220)
BUTTON_COLOR = (70, 70, 70)
BUTTON_TEXT = (255, 255, 255)
HIGHLIGHT_COLOR = (0, 255, 0, 180)  # translucent green for win line animation

# 📏 Dimensions
SCREEN_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = SCREEN_SIZE // GRID_SIZE

# 🧠 Fonts
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# 🎵 Sound loading helper
def load_sound(name):
    path = os.path.join("assets", name)
    print(f"Attempting to load sound: {path}")
    if os.path.exists(path):
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(1.0)  # Set full volume
            print(f"Successfully loaded sound: {name}")
            return sound
        except Exception as e:
            print(f"Error loading sound {name}: {e}")
    else:
        print(f"Sound file not found: {path}")
    return None

# 🎧 Load sounds
click_sound = load_sound("click.mp3")
win_sound = load_sound("win.mp3")
draw_sound = load_sound("draw.mp3")

# 🎼 Optional background music
bg_music_path = os.path.join("assets", "bg_music.mp3")
if os.path.exists(bg_music_path):
    try:
        pygame.mixer.music.load(bg_music_path)
        pygame.mixer.music.play(-1)  # loop forever
        pygame.mixer.music.set_volume(0.3)
    except Exception as e:
        print(f"Music load failed: {e}")

# ─────────────────────────────────────────────

def draw_grid(screen):
    screen.fill(BG_COLOR)
    # vertical lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE), 4)
    # horizontal lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (SCREEN_SIZE, i * CELL_SIZE), 4)

def draw_marks(screen, board):
    for idx, mark in enumerate(board):
        row = idx // GRID_SIZE
        col = idx % GRID_SIZE
        center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
        if mark == 'X':
            draw_x(screen, center)
        elif mark == 'O':
            draw_o(screen, center)

def should_play_sounds():
    """Check if sounds should be played based on game state"""
    try:
        # Stop all sounds if tournament is finished
        if pygame.mixer.get_busy():
            pygame.mixer.stop()
        return True
    except:
        return False

def draw_x(screen, center):
    x, y = center
    offset = CELL_SIZE // 3
    pygame.draw.line(screen, X_COLOR, (x - offset, y - offset), (x + offset, y + offset), 8)
    pygame.draw.line(screen, X_COLOR, (x - offset, y + offset), (x + offset, y - offset), 8)
    if click_sound and should_play_sounds():
        click_sound.stop()  # Stop any previous playing
        click_sound.play(maxtime=300)  # Play for max 300ms

def draw_o(screen, center):
    x, y = center
    radius = CELL_SIZE // 3
    pygame.draw.circle(screen, O_COLOR, (x, y), radius, 8)
    if click_sound and should_play_sounds():
        click_sound.stop()  # Stop any previous playing
        click_sound.play(maxtime=300)  # Play for max 300ms

def draw_message(screen, text: str, y_offset=SCREEN_SIZE + 10):
    surf = FONT.render(text, True, BLACK)
    screen.blit(surf, (10, y_offset))

def draw_submessage(screen, text: str, y_offset=SCREEN_SIZE + 45):
    surf = SMALL_FONT.render(text, True, BLACK)
    screen.blit(surf, (10, y_offset))

def draw_button(screen, rect: pygame.Rect, text: str):
    pygame.draw.rect(screen, BUTTON_COLOR, rect, border_radius=6)
    surf = SMALL_FONT.render(text, True, BUTTON_TEXT)
    text_rect = surf.get_rect(center=rect.center)
    screen.blit(surf, text_rect)

def pos_to_index(pos: Tuple[int, int]) -> int:
    x, y = pos
    if x < 0 or y < 0 or x >= SCREEN_SIZE or y >= SCREEN_SIZE:
        return -1
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row * GRID_SIZE + col

# ─────────────────────────────────────────────
# 🟢 Win Animation

def animate_winning_line(screen, start_cell: Tuple[int, int], end_cell: Tuple[int, int]):
    """Fade-in animation for the winning line"""
    start_pos = (start_cell[1] * CELL_SIZE + CELL_SIZE // 2, start_cell[0] * CELL_SIZE + CELL_SIZE // 2)
    end_pos = (end_cell[1] * CELL_SIZE + CELL_SIZE // 2, end_cell[0] * CELL_SIZE + CELL_SIZE // 2)

    # Ensure the screen is updated with the final move before animation
    pygame.display.flip()
    pygame.time.delay(100)  # Short delay to ensure the mark is visible

    if win_sound and should_play_sounds():
        win_sound.stop()  # Stop any previous sounds
        win_sound.play()

    for alpha in range(0, 180, 20):
        # Redraw the game state to ensure marks remain visible
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.line(overlay, (0, 255, 0, alpha), start_pos, end_pos, 12)
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(60)

def play_draw_sound():
    if draw_sound and should_play_sounds():
        draw_sound.stop()  # Stop any previous sounds
        draw_sound.play()
