import os
import sys

def menu():
    print("\n  AI Assignment 2 Menu ")
    print("1. Tic-Tac-Toe using Minimax (Task 1)")
    print("2. Tic-Tac-Toe using Alpha-Beta Pruning (Task 2)")
    print("3. Genetic Algorithm for String Matching (Task 3)")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def run_task(task_number):
    python_exec = f'"{sys.executable}"' 
    if task_number == '1':
        os.system(f'{python_exec} TicTacToe_minimax.py')
    elif task_number == '2':
        os.system(f'{python_exec} TicTacToe_alphabeta.py')
    elif task_number == '3':
        os.system(f'{python_exec} genetic_stringmatch.py')
    elif task_number == '4':
        print("Exiting program.")
        sys.exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    while True:
        user_choice = menu()
        run_task(user_choice)
