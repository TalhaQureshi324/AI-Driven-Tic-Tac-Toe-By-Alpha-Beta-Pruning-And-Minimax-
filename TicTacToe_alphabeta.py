#task 2
import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 650
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE - Minimax vs Alpha-Beta')
screen.fill(BG_COLOR)
font = pygame.font.SysFont(None, 40)

board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
game_over = False
player = 'X'

x_score = 0
o_score = 0

use_alpha_beta = False
node_count = 0
max_depth = 0
exec_time = 0

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

def draw_scores():
    score_text = font.render(f'Score - X: {x_score}  O: {o_score}', True, WHITE)
    pygame.draw.rect(screen, BG_COLOR, (0, HEIGHT - 50, WIDTH, 50))
    screen.blit(score_text, (20, HEIGHT - 40))

def check_winner(b):
    for row in b:
        if row.count(row[0]) == 3 and row[0] != '':
            return row[0]
    for col in range(BOARD_COLS):
        if b[0][col] == b[1][col] == b[2][col] and b[0][col] != '':
            return b[0][col]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != '':
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != '':
        return b[0][2]
    return None

def is_board_full(b):
    return all(cell != '' for row in b for cell in row)

def minimax(b, depth, is_maximizing):
    global node_count, max_depth
    node_count += 1
    max_depth = max(max_depth, depth)

    winner = check_winner(b)
    if winner == 'O':
        return 10 - depth
    elif winner == 'X':
        return depth - 10
    elif is_board_full(b):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if b[row][col] == '':
                    b[row][col] = 'O'
                    score = minimax(b, depth + 1, False)
                    b[row][col] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if b[row][col] == '':
                    b[row][col] = 'X'
                    score = minimax(b, depth + 1, True)
                    b[row][col] = ''
                    best_score = min(score, best_score)
        return best_score

def alpha_beta(b, depth, is_maximizing, alpha, beta):
    global node_count, max_depth
    node_count += 1
    max_depth = max(max_depth, depth)

    winner = check_winner(b)
    if winner == 'O':
        return 10 - depth
    elif winner == 'X':
        return depth - 10
    elif is_board_full(b):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if b[row][col] == '':
                    b[row][col] = 'O'
                    eval = alpha_beta(b, depth + 1, False, alpha, beta)
                    b[row][col] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if b[row][col] == '':
                    b[row][col] = 'X'
                    eval = alpha_beta(b, depth + 1, True, alpha, beta)
                    b[row][col] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def ai_move():
    global node_count, max_depth, exec_time
    node_count = 0
    max_depth = 0
    best_score = -float('inf')
    best_move = None
    start_time = time.time()

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                board[row][col] = 'O'
                if use_alpha_beta:
                    score = alpha_beta(board, 0, False, -float('inf'), float('inf'))
                else:
                    score = minimax(board, 0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    exec_time = time.time() - start_time
    if best_move:
        row, col = best_move
        board[row][col] = 'O'

def show_menu():
    global use_alpha_beta
    print("Choose AI Type:")
    print("1. Minimax (No Alpha-Beta)")
    print("2. Alpha-Beta Pruning")
    choice = input("Enter choice (1 or 2): ")
    use_alpha_beta = (choice == '2')

draw_lines()
show_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"\nPerformance Stats")
            print(f"AI used: {'Alpha-Beta Pruning' if use_alpha_beta else 'Minimax'}")
            print(f"Nodes Explored: {node_count}")
            print(f"Max Depth: {max_depth}")
            print(f"Execution Time: {exec_time:.6f} seconds")
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseY < HEIGHT - 50:
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = 'X'
                    draw_figures()

                    if check_winner(board) == 'X':
                        print("X Wins!")
                        game_over = True
                    elif is_board_full(board):
                        print("Draw!")
                        game_over = True
                    else:
                        ai_move()
                        draw_figures()

                        winner = check_winner(board)
                        if winner == 'O':
                            print("O Wins!")
                            game_over = True
                        elif is_board_full(board):
                            print("Draw!")
                            game_over = True

    draw_scores()
    pygame.display.update()
