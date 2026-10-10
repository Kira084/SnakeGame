# Snake Game 
A Snake game made with Python and pygame-ce, featuring hand-drawn graphics, two visual themes (normal and neon) and background music.

# Screenshots

[Normal theme](screenshots/normal.png) | [Neon theme](screenshots/neon.png) |

# Features

- Classic Snake gameplay on a grid with a start menu
- Two hand-drawn themes: *normal* and *neon*, each with its own music
- The snake opens its mouth when an apple is two cells ahead
- Golden apple: gives 5 points and disappears after a few seconds
- Random obstacles in every round
- The game gets faster as your score grows
- Pause and restart
- High score saved to a file
- Sound effect when eating an apple

# Controls

Click *PLAY* or Space / Enter to Start the game 
Arrow keys > Move the snake 
T > Switch between normal and neon theme 
P > Pause / resume 
Space > Restart after Game Over 


# How to play play

### Option 1: Windows executable

1. Go to the [latest release](https://github.com/Kira084/SnakeGame/releases/latest) and download `SnakeGame.zip`.
2. Unzip it and run `main.exe`.

Windows may show a "Windows protected your PC" warning because the file is not signed. Click *More info* > *Run anyway*.

### Option 2: Run from source

You need Python 3 installed (developed and tested with Python 3.14).

*Windows (Command Prompt):*
```
git clone https://github.com/Kira084/SnakeGame.git
cd SnakeGame
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

*macOS / Linux:*

```
git clone https://github.com/Kira084/SnakeGame.git
cd SnakeGame
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

# What I practiced

- Python basics: functions, lists, tuples, dictionaries, loops and conditions
- Game loop, keyboard and mouse event handling with pygame-ce
- Working with images (loading, scaling, rotating) and sound
- Reading and writing files (high score) with error handling
- Packaging a Python project into a Windows .exe
- Git and GitHub: step-by-step commits, virtual environment, requirements file, releases

# Credits
*Graphics:* all sprites and backgrounds are hand-drawn by me (Kira Deriabina)

*Music:*

- "Pixelland" by Kevin MacLeod (incompetech.com)
  Licensed under Creative Commons: By Attribution 4.0 License
  http://creativecommons.org/licenses/by/4.0/
- "Funny Bit" (slow version) by David Renda
  Background music via https://www.FesliyanStudios.com
