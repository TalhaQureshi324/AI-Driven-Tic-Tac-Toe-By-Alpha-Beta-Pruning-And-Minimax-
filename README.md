# AI Driven Tic Tac Toe By Alpha Beta Pruning & Minimax

**Implemented by Muhammad Talha Qureshi**

This repository contains three Artificial Intelligence tasks implemented
in Python using Pygame and Genetic Algorithms concepts.
Each task demonstrates a core AI decision-making technique: **Minimax**,
**Alpha-Beta Pruning**, and **Genetic Algorithms**.

------------------------------------------------------------------------

## 🎯 Project Overview

  ------------------------------------------------------------------------
  Task       Title          Technique             Description
  ---------- -------------- --------------------- ------------------------
  Task 1     Tic-Tac-Toe    Minimax Algorithm     AI plays optimally by
             (Minimax)                            exploring all possible
                                                  game states and choosing
                                                  the move that maximizes
                                                  its winning chances.

  Task 2     Tic-Tac-Toe    Minimax + Alpha-Beta  An optimized version of
             (Alpha-Beta)   Pruning               Task 1 that uses pruning
                                                  to reduce search space
                                                  and compares execution
                                                  performance.

  Task 3     String         Genetic Algorithm     AI evolves a random
             Matching                             population of strings to
                                                  match a target word
                                                  using selection,
                                                  crossover, and mutation.
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧩 How to Run the Project

### 🖥️ Prerequisites

Make sure Python (≥ 3.9) and Pygame are installed:

``` bash
pip install pygame
```

### ▶️ Run the Main Menu

This file allows you to choose between all three tasks:

``` bash
python bscs23122_AI_assm_2_.py
```

You will see a menu like this:

      AI Assignment 2 Menu
    1. Tic-Tac-Toe using Minimax (Task 1)
    2. Tic-Tac-Toe using Alpha-Beta Pruning (Task 2)
    3. Genetic Algorithm for String Matching (Task 3)
    4. Exit

Choose any option (1-3) to run that specific task.

------------------------------------------------------------------------

## 🧠 Task 1 - Tic-Tac-Toe using Minimax

### 🧩 Concept

The Minimax algorithm allows AI to simulate every possible game outcome
before deciding its move.\
It assumes: - The AI (O) plays optimally to maximize its score. - The
Player (X) plays optimally to minimize AI's score.

### ⚙️ Working

-   The board is represented as a 3×3 grid.
-   After each player move, the AI explores all possible moves
    recursively.
-   Each state is evaluated using the minimax score:
    -   **Win for AI (O): +10**
    -   **Win for Player (X): -10**
    -   **Draw: 0**
-   AI chooses the move with the highest minimax value (best guaranteed
    outcome).

### 🔄 Example Workflow

1.  Player places X.
2.  AI simulates all possible responses for O.
3.  For each possible O, AI also predicts how the player might respond
    next.
4.  This recursion continues until all possible game endings are
    evaluated.
5.  The best move (leading to the best final score) is selected.

------------------------------------------------------------------------

## ⚡ Task 2 - Tic-Tac-Toe using Alpha-Beta Pruning

### 🧩 Concept

This task extends Minimax with **Alpha-Beta Pruning**, a technique that
cuts off unnecessary branches of the game tree.
This makes the decision-making faster and more efficient while
guaranteeing the same result as plain Minimax.

### 🧮 Performance Metrics

At the end of the game, the program prints:

-   AI type used
-   Nodes explored
-   Maximum recursion depth
-   Execution time

**Example Output:**

    Performance Stats
    AI used: Alpha-Beta Pruning
    Nodes Explored: 3
    Max Depth: 1
    Execution Time: 0.000024 seconds

------------------------------------------------------------------------

## 🧬 Task 3 - Genetic Algorithm for String Matching

### 🧩 Concept

A **Genetic Algorithm (GA)** mimics natural selection to solve
optimization problems.
In this case, the goal is to evolve random strings until they match a
target word (e.g., `HELLOGA123`).

### ⚙️ Workflow

1.  **Initialization:** Create a random population of strings.
2.  **Fitness Calculation:** Compare each string with the target and
    count matching characters.
3.  **Selection:** Pick parent strings using tournament selection.
4.  **Crossover:** Mix genes (characters) between parents to create
    offspring.
5.  **Mutation:** Randomly alter some characters to maintain diversity.
6.  **Repeat:** Over generations, the population improves until a
    near-perfect or perfect match appears.

### 🧾 Sample Output

    Generation 1: Max Fitness = 2, Average Fitness = 0.28
    ...
    Generation 20: Max Fitness = 8, Average Fitness = 6.40

    Best match after 20 generations: HELLOLAW23
    Fitness: 8

------------------------------------------------------------------------

## 🕹️ Libraries Used

  Library   Purpose
  --------- ----------------------------------------------
  - pygame    GUI and graphics for Tic-Tac-Toe
  - random    Mutation, crossover, and selection in GA
  - string    Character set for chromosome generation
  - time      Execution time measurement for AI algorithms

------------------------------------------------------------------------

## 🔍 Complete Workflow Summary

### Main Menu (`bscs23122_AI_assm_2_.py`)

Displays a selection menu to run any of the three AI programs.

### Task 1 (Minimax)

-   Explores all possible game states recursively.
-   Evaluates each outcome and backpropagates scores.
-   Selects the move that maximizes AI's winning chance.

### Task 2 (Alpha-Beta)

-   Improves Minimax by skipping irrelevant branches.
-   Displays node count, recursion depth, and time for analysis.

### Task 3 (Genetic Algorithm)

-   Evolves random strings toward the target using crossover and
    mutation.
-   Prints fitness evolution across generations.

------------------------------------------------------------------------

## 📊 Key AI Concepts Demonstrated

  -----------------------------------------------------------------------
  Concept                        Description
  ------------------------------ ----------------------------------------
  - Minimax                        Decision-making by exploring all
                                 possible moves

  - Alpha-Beta Pruning             Optimization of Minimax by pruning
                                 branches

  - Genetic Algorithm              Evolutionary approach for optimization

  - Fitness Function               Measures how close a candidate solution
                                 is

  - Backtracking                   Used in Minimax to revert states after
                                 exploring a move
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🏁 Conclusion

This project demonstrates the power of search-based and evolutionary AI
algorithms using:

-   **Minimax and Alpha-Beta for deterministic game logic.**
-   **Genetic Algorithms for stochastic optimization.**

Together, these tasks showcase three distinct AI problem-solving
paradigms:-
**search, optimization, and evolution - implemented in Python.**

------------------------------------------------------------------------

## 📜 Author

**Muhammad Talha Qureshi**
BSCS23122 - Department of Computer Science\
Artificial Intelligence

⭐ *If you like this work, don't forget to star the repository!* ⭐
