#task 1 
import pygame
import sys
import copy

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
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)
font = pygame.font.SysFont(None, 40)

board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
game_over = False
player = 'X'

x_score = 0
o_score = 0

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

def evaluate_move(row, col, current_player):
    temp_board = copy.deepcopy(board)
    temp_board[row][col] = current_player
    move_value = minimax(temp_board, 0, current_player == 'O')
    if current_player == 'X' and move_value < 0:
        return 1
    elif current_player == 'O' and move_value > 0:
        return 1
    elif current_player == 'X' and move_value > 0:
        return -1
    elif current_player == 'O' and move_value < 0:
        return -1
    return 0

def update_score(row, col, current_player, is_winning_move=False):
    global x_score, o_score
    move_value = evaluate_move(row, col, current_player)
    if is_winning_move:
        move_value += 3
    if current_player == 'X':
        x_score += move_value
    else:
        o_score += move_value

def board_is_empty():
    return all(cell == '' for row in board for cell in row)

def ai_move():
    best_score = -float('inf')
    best_move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        row, col = best_move
        board[row][col] = 'O'
        update_score(row, col, 'O')

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseY < HEIGHT - 50:
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if board[clicked_row][clicked_col] == '':
                    is_first_move = board_is_empty()

                    board[clicked_row][clicked_col] = 'X'
                    draw_figures()

                    if check_winner(board) == 'X':
                        update_score(clicked_row, clicked_col, 'X', is_winning_move=True)
                        print('X wins!')
                        game_over = True
                    elif is_board_full(board):
                        update_score(clicked_row, clicked_col, 'X')
                        print('Draw!')
                        game_over = True
                    else:
                        update_score(clicked_row, clicked_col, 'X')
        
                        ai_move()
                        draw_figures()
        
                        winner = check_winner(board)
                        if winner == 'O':
                            for r in range(BOARD_ROWS):
                                for c in range(BOARD_COLS):
                                    if board[r][c] == 'O':
                                        update_score(r, c, 'O', is_winning_move=(check_winner(board) == 'O'))
                                        break
                            print('O wins!')
                            game_over = True
                        elif is_board_full(board):
                            print('Draw!')
                            game_over = True
                        else:
                            if is_first_move:
                                for r in range(BOARD_ROWS):
                                    for c in range(BOARD_COLS):
                                        if board[r][c] == 'O':
                                            update_score(r, c, 'O')
                                            break


    draw_scores()
    pygame.display.update()