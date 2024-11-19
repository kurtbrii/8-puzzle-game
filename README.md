# 8-Puzzle Game

## Description
8-puzzle game that uses BFS, DFS, and A-Star Algorithms

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)

## Installation
1. Clone the repo: `git clone git@github.com:kurtbrii/8-puzzle-game.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Make sure [rye](https://rye.astral.sh/) is installed
4. `rye sync` 

## Usage
Run the app with `rye run start`. Use the interface to click/move the tiles. You can select between BFS, DFS, or A-Star to solve the puzzle.

## Features
- Solving Puzzle manually
- Using BFS, DFS, or A-Star to solve the puzzle
- Detect if the puzzle is solvable or not

## Screenshots
### Base Game
![ScreenShot](/src/assets/screenshots/puzzle.png)

### BFS/DFS
![ScreenShot](/src/assets/screenshots/bfs-dfs.png)

### A-Star
![ScreenShot](/src/assets/screenshots/a-star.png)
