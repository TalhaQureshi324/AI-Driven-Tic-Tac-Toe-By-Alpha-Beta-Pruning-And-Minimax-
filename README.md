# AI DRIVEN TIC TAC TOE BY ALPHA BETA PRUNING AND MINIMAX 
### *Implemented by Muhammad Talha Qureshi*  

This repository contains **three Artificial Intelligence tasks** implemented in **Python** using **Pygame** and **Genetic Algorithm** concepts.  
Each task demonstrates a fundamental **AI decision-making technique** — *Minimax*, *Alpha-Beta Pruning*, and *Genetic Algorithms*.

---

## 🎯 **Project Overview**

| **Task** | **Title** | **Technique Used** | **Description** |
|-----------|------------|-------------------|-----------------|
| **Task 1** | Tic-Tac-Toe (Minimax) | Minimax Algorithm | AI plays optimally by exploring all possible game states and choosing the move that maximizes its winning chances. |
| **Task 2** | Tic-Tac-Toe (Alpha-Beta) | Minimax + Alpha-Beta Pruning | Optimized Minimax that reduces search space while giving identical results. |
| **Task 3** | String Matching | Genetic Algorithm | AI evolves a random population of strings to match a target word using selection, crossover, and mutation. |

---

## 🧩 **How to Run the Project**

### 🖥️ **Prerequisites**
Make sure **Python (≥ 3.9)** and **Pygame** are installed:

```bash
pip install pygame
```

### ▶️ **Run the Main Menu**
Use the main menu file to choose between tasks:

```bash
python bscs23122_AI_assm_2_.py
```

You will see a menu like this:

```
AI Assignment 2 Menu
1. Tic-Tac-Toe using Minimax (Task 1)
2. Tic-Tac-Toe using Alpha-Beta Pruning (Task 2)
3. Genetic Algorithm for String Matching (Task 3)
4. Exit
```

---

## 🧠 **Task 1 — Tic-Tac-Toe using Minimax**

### 🧩 **Concept**
The **Minimax algorithm** simulates every possible move of both the player and AI before deciding the best possible move.  

It assumes:
- The **AI (O)** plays optimally to maximize its score.  
- The **Player (X)** plays optimally to minimize AI’s score.  

### ⚙️ **Working**
1. Board represented as a 3×3 grid.  
2. After each player move, AI recursively explores all possibilities.  
3. Each state is evaluated with scores:  

| Result | Score |
|---------|-------|
| AI Win (O) | +10 |
| Player Win (X) | -10 |
| Draw | 0 |

4. AI picks the move with the highest Minimax score.

### 🔄 **Example Flow**
1. Player places X.  
2. AI simulates all possible O moves.  
3. For each move, AI predicts the player's next possible response.  
4. It backtracks through all outcomes and picks the move with the best final score.

---

## ⚡ **Task 2 — Tic-Tac-Toe using Alpha-Beta Pruning**

### 🧩 **Concept**
Alpha-Beta Pruning enhances Minimax by cutting off branches that won’t affect the final decision.  
It **reduces computational cost** while ensuring the **same decision quality**.

### 🧮 **Performance Metrics**
At the end, the program prints:

| Metric | Description |
|---------|--------------|
| **AI Used** | Whether Minimax or Alpha-Beta |
| **Nodes Explored** | Total recursive states visited |
| **Max Depth** | Maximum recursion depth |
| **Execution Time** | Time taken to make a move |

**Example Output:**  
```
Performance Stats
AI used: Alpha-Beta Pruning
Nodes Explored: 3
Max Depth: 1
Execution Time: 0.000024 seconds
```

---

## 🧬 **Task 3 — Genetic Algorithm for String Matching**

### 🧩 **Concept**
A **Genetic Algorithm (GA)** mimics natural selection.  
The goal: evolve random strings until they match a **target string** (e.g., `HELLOGA123`).

### ⚙️ **Workflow**
1. **Initialization** → Generate random population of strings.  
2. **Fitness Calculation** → Count how many characters match the target.  
3. **Selection** → Pick parents using tournament selection.  
4. **Crossover** → Combine parents’ genes to create offspring.  
5. **Mutation** → Randomly change a few characters to maintain diversity.  
6. **Repeat** → Over generations, best solutions evolve.

### 🧾 **Sample Output**
```
Generation 1: Max Fitness = 2, Average Fitness = 0.28
...
Generation 20: Max Fitness = 8, Average Fitness = 6.40

Best match after 20 generations: HELLOLAW23
Fitness: 8
```

---

## 🕹️ **Libraries Used**

| Library | Purpose |
|----------|----------|
| **pygame** | GUI for Tic-Tac-Toe |
| **random** | Mutation, crossover, and selection in GA |
| **string** | Character set for chromosome generation |
| **time** | Measure algorithm execution time |

---

## 🔍 **Complete Workflow Summary**

| File | Description |
|------|--------------|
| **bscs23122_AI_assm_2_.py** | Displays main menu to choose between the 3 tasks |
| **TicTacToe_minimax.py** | Implements pure Minimax algorithm |
| **TicTacToe_alphabeta.py** | Implements Alpha-Beta optimized Minimax |
| **StringMatching_GA.py** | Implements Genetic Algorithm for string evolution |

---

## 📊 **Key AI Concepts Demonstrated**

| Concept | Description |
|----------|--------------|
| **Minimax** | Recursive decision-making that explores all possible game outcomes |
| **Alpha-Beta Pruning** | Optimization that skips irrelevant branches in Minimax |
| **Genetic Algorithm** | Evolutionary search for optimal solutions |
| **Fitness Function** | Measures closeness to target solution |
| **Backtracking** | Used to revert board states during Minimax recursion |

---

## 🏁 **Conclusion**

This project showcases the power of **AI search and optimization algorithms** using:

- 🧩 Minimax & Alpha-Beta → Deterministic game-solving logic  
- 🧬 Genetic Algorithm → Stochastic evolutionary optimization  

Together, these demonstrate three key **AI paradigms** — *Search*, *Optimization*, and *Evolution*.

---

## 👨‍💻 **Author**
**Muhammad Talha Qureshi**  
*BSCS23122 – Department of Computer Science*  
*Artificial Intelligence Assignment 2 (Fall 2025)*  

⭐ *If you found this project helpful, don’t forget to star the repository!* ⭐  
