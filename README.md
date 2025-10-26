Tic-Tac-Pro

A Python-based Tic-Tac-Toe game with AI featuring a tournament format, fair AI, and interactive UI built with Pygame. Play against an AI opponent across multiple difficulty levels, complete rounds, and experience animations and sound effects that make gameplay engaging.

🔹Features:

Tournament Mode: Play multiple rounds with different AI difficulty levels (Easy, Medium, Hard).
Fair AI: AI is designed to win sometimes but also allows the player to win, making the game competitive yet enjoyable.
Interactive UI: Built using Pygame with clear board visuals, buttons, and score tracking.
Animations & Sound Effects:
Winning line animation
Click, win, and draw sound effects
Optional looping background music
Scoring & Round Management: Tracks points per round and announces tournament titles.
Modular Code Structure: Clean separation of UI, game logic, AI, and tournament flow for easy maintenance and upgrades.

🛠️ Technologies Used

Python 3.x
Pygame (UI, animations, sound)
Object-Oriented Programming (Game & AI logic)

📁 Folder Structure
tic_tac_tournament/
├── assets/                # Sounds & images
│   ├── click.wav
│   ├── win.wav
│   ├── draw.wav
│   └── bg_music.mp3
├── ai.py                  # AI strategies & difficulty levels
├── game.py                # Board state, rules, win detection
├── tournament.py          # Tournament flow & scoring
├── ui.py                  # Frontend: Pygame rendering & animations
├── main.py                # Starts the game (UI + flow)
├── requirements.txt
└── README.md

⚡ How to Run

Clone the repository

git clone https://github.com/<your-username>/tic-tac-tournament.git
cd tic-tac-tournament

Install dependencies

pip install -r requirements.txt

Run the game

python main.py

🎮 How to Play

Player always plays as X; AI plays as O.
Click on a cell to place your mark.
Complete all rounds to finish the tournament.
Track your score and tournament title displayed below the board.
Use buttons to Skip Round or Restart Tournament.

🏆 Game Flow

Player Turn → Click to place X.
AI Turn → AI moves automatically based on difficulty.
Check Result → Win/draw detection triggers animation & sounds.
Next Round / Tournament → Automatically advances or wait for user action.

💡 Unique Features

Tournament Mode: Multiple rounds with increasing difficulty.
Balanced AI: AI does not always win; ensures fair competition.
Audio-Visual Feedback: Sounds and animations for clicks, wins, draws.
Expandable Code: Easy to add new AI levels, board sizes, or animations.

🛠️ Future Improvements

Add online multiplayer mode.
Introduce custom board sizes (4x4, 5x5).
Add power-ups or bonus rounds in tournament mode.
Integrate leaderboard and stats to track player performance.

📝 References

Pygame Documentation
Free sound effects from Freesound.org

👨‍💻 Author

Pranav Sukale – Engineering Student, AI/Game Enthusiast
