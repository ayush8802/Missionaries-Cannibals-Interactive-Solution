# Missionaries-Cannibals-Interactive-Solution

This repository contains an interactive Python solution to the **Missionaries and Cannibals** problem, a classic puzzle that challenges users to transport missionaries and cannibals across a river without breaking key rules of the problem.

## Problem Statement

The puzzle involves three missionaries and three cannibals on the left side of a river. They all need to cross to the right side using a boat that can carry a maximum of two people at a time. However, if cannibals outnumber missionaries on either bank at any point, the missionaries will be eaten. The objective is to find a series of valid moves to get all the missionaries and cannibals safely across the river.

## Features

- **User-driven gameplay**: At each step, the user chooses how many missionaries and cannibals to move across the river.
- **Step-by-step state display**: The current state of the riverbanks and the boat's position is shown after each move.
- **Input validation**: Ensures that each move follows the rules of the game and prevents any invalid scenarios.
- **Clear feedback**: If an invalid move is attempted, the program informs the user and allows them to retry.
- **Victory condition**: The game ends when all missionaries and cannibals have safely crossed to the right side.

## How to Play

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/Missionaries-Cannibals-Interactive-Solution.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Missionaries-Cannibals-Interactive-Solution
    ```

3. Run the Python script:
    ```bash
    python missionaries_cannibals.py
    ```

4. Follow the on-screen instructions to move missionaries and cannibals across the river:
    - Enter the number of missionaries and cannibals you want to move.
    - The program will validate your move and display the updated state.

5. Keep playing until all missionaries and cannibals are on the right side of the river.

## Game Rules

1. The boat can carry one or two people at a time.
2. You can move a combination of missionaries and cannibals or just one type.
3. The number of cannibals should never outnumber the missionaries on either bank.
4. Your goal is to safely transport all missionaries and cannibals from the left bank to the right bank.

## Example Gameplay

- Starting with 3 missionaries and 3 cannibals on the left bank.
- The user moves one cannibal and one missionary to the right bank.
- The program checks if the move is valid, updates the state, and prompts the user for the next move.
- Repeat until all have crossed safely.

## Requirements

- Python 3.x

## Contributing

Feel free to fork this repository, submit issues, or create pull requests to improve the solution. Contributions and suggestions are welcome!
