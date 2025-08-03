# Encyclopedic Board Game

Welcome to the **Encyclopedic Board Game**, a two-player trivia and dice game where players race from the start to the end of a 128-cell board by answering questions and rolling dice.

---

## Table of Contents
- [Game Description](#game-description)
- [Game Logic](#game-logic)
- [Setup and Installation](#setup-and-installation)
- [Running the Game](#running-the-game)
  - [Arcade Desktop Version](#arcade-desktop-version)
  - [Streamlit Web Version](#streamlit-web-version)
- [Project Structure](#project-structure)
- [Assets](#assets)
- [License](#license)

---

## Game Description

Two players start at the bottom-left corner of a 16x8 board (cell 1). Players take turns answering encyclopedic questions and rolling dice to move forward. The first player to reach cell 128 (top-right) wins!

---

## Game Logic

- Players begin at cell 1.
- On their turn, a player must correctly answer the question on their current cell.
- If correct, they roll a dice (1–6) and move forward that many cells.
- The other player judges the answer correctness.
- Turns alternate until one player reaches or exceeds cell 128.
- Movement and dice rolls are animated (Arcade) or interactive (Streamlit).
- Sounds play on dice roll, movement, and winning.

---

## Setup and Installation

### Requirements

- Python 3.8+
- `arcade` (for desktop version)
- `streamlit` (for web version)

### Install dependencies

```bash
pip install arcade streamlit
