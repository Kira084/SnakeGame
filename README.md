# Snake Game 

A Snake game made with Python and pygame-ce, featuring hand-drawn graphics, two visual themes (neon and day) and background music.

Also available as a browser version written in JavaScript: [SnakeGame-Web](https://github.com/Kira084/SnakeGame-Web) (play it [here](https://kira084.github.io/SnakeGame-Web/)).

## Screenshots
[Day mode](screenshots/normal.png) | [Neon mode](screenshots/neon.png) 

## Features

- Classic Snake gameplay on a grid with a start menu
- Two hand-drawn themes: *neon* (default) and *day*, each with its own music
- Glowing trail behind the snake in the neon theme (can be switched off)
- The snake opens its mouth when an apple is two cells ahead
- Golden apple: gives 5 points and disappears after a few seconds
- Random obstacles in every round
- The game gets faster as your score grows
- Pause and restart
- High score saved to a file
- Sound effect when eating an apple

## Controls
Click *PLAY* or Space / Enter > Start the game 
Arrow keys > Move the snake 
T > Switch between the neon and day mode 
G > Glow trail on / off (neon mode only) 
P > Pause / resume 
Space > Restart after Game Over 

# How to play

### Option 1: In the browser

Play the JavaScript version here: https://kira084.github.io/SnakeGame-Web/

### Option 2: Windows executable

1. Go to the [latest release](https://github.com/Kira084/SnakeGame/releases/latest) and download the `.zip` file.
2. Unzip it and run `Snake.exe`.

Windows may show a "Windows protected your PC" warning because the file is not signed. Click *More info* > *Run anyway*.

### Option 3: Run from source

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

## What I practiced

- Python basics: functions, lists, tuples, dictionaries, loops and conditions
- Game loop, keyboard and mouse event handling with pygame-ce
- Working with images (loading, scaling, rotating, transparency) and sound
- Reading and writing files (high score) with error handling
- Packaging a Python project into a Windows .exe
- Porting the same game to JavaScript (HTML Canvas), see [SnakeGame-Web](https://github.com/Kira084/SnakeGame-Web)
- Git and GitHub: step-by-step commits, virtual environment, requirements file, releases

## Credits

*Graphics:* all sprites and backgrounds are hand-drawn by me (Kira Deriabina)

*Music:*

- "Pixelland" by Kevin MacLeod (incompetech.com)
  Licensed under Creative Commons: By Attribution 4.0 License
  http://creativecommons.org/licenses/by/4.0/
- "Funny Bit" (slow version) by David Renda
  Background music via https://www.FesliyanStudios.com
