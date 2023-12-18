import numpy as np
import pygame
import random

board = np.zeros([20, 10], dtype=str)

BOARD_SIZE = [20, 10]

WIDTH, HEIGHT = 800, 800
BLOCK_SIZE = int(WIDTH / BOARD_SIZE[0] - (WIDTH / BOARD_SIZE[1]) / 10)
blank = (WIDTH - (BLOCK_SIZE * BOARD_SIZE[0])) / 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('게임')

font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

button_width, button_height = 200, 50
button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT - button_height) // 2
button_text = font.render('Start', True, WHITE)
button_control = 100
text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2 + button_control))

game_over_text = font.render('Game Over', True, BLACK)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

game = False

current_block = None
current_block_position = [0, 0]

def generate_new_block():
    block_types = [
        # I 모양 블록
        [['1', '1', '1', '1'],
         ['','','','']],
        # O 모양 블록
        [['1', '1','',''],
         ['1', '1','','']],
        # T 모양 블록
        [['', '1', '',''],
         ['1', '1', '1','']],
        # L 모양 블록
        [['1', '', '',''],
         ['1', '1', '1','']],
        # J 모양 블록
        [['', '', '1',''],
         ['1', '1', '1','']],
        # S 모양 블록
        [['', '1', '1',''],
         ['1', '1', '','']],
        # Z 모양 블록
        [['1', '1', '',''],
         ['', '1', '1','']]
    ]

    return random.choice(block_types)

def reset_game():
    global current_block, current_block_position, game, board
    current_block = generate_new_block()
    current_block_position = [0, BOARD_SIZE[1] // 2 - 1]
    game = False
    board = np.zeros([20, 10], dtype=str)

def move_block_down():
    global current_block_position, current_block, game
    new_position = [current_block_position[0] + 1, current_block_position[1]]
    if is_valid_move(new_position,current_block):
        current_block_position = new_position
    else:
        place_block_on_board()
        if is_game_over():
            reset_game()
        else:
            reset_block()

def move_block_left():
    global current_block_position, current_block
    new_position = [current_block_position[0], current_block_position[1] - 1]
    if is_valid_move(new_position,current_block):
        current_block_position = new_position

def move_block_right():
    global current_block_position, current_block
    new_position = [current_block_position[0], current_block_position[1] + 1]
    if is_valid_move(new_position,current_block):
        current_block_position = new_position
def rotate_block():
    global current_block, current_block_position

    original_position = current_block_position.copy()
    rotated_block = np.rot90(current_block)
    rotated_block_width = len(rotated_block[0])
    rotated_block_height = len(rotated_block)

    # Check if the rotation goes beyond the right edge of the board or overlaps with existing blocks
    while (
        current_block_position[1] + rotated_block_width > BOARD_SIZE[1] or
        current_block_position[0] + rotated_block_height > BOARD_SIZE[0] or
        not is_valid_move(current_block_position, rotated_block)
    ):
        # Try adjusting the X-coordinate
        current_block_position[1] += 1

        # Check if the adjustment is successful
        if (
            current_block_position[1] + rotated_block_width <= BOARD_SIZE[1] and
            is_valid_move(current_block_position, rotated_block)
        ):
            break

        # If adjustment is not successful, revert the rotation and try a different adjustment
        current_block_position = original_position.copy()
        rotated_block = np.rot90(rotated_block, -1)

    current_block = rotated_block.tolist()


def reset_block():
    global current_block, current_block_position
    current_block = generate_new_block()
    current_block_position = [0, BOARD_SIZE[1] // 2 - 1]

def draw_board():
    for i in range(BOARD_SIZE[0]):
        for j in range(BOARD_SIZE[1]):
            pygame.draw.rect(screen, BLACK, ((j * BLOCK_SIZE) + blank, (i * BLOCK_SIZE) + blank, BLOCK_SIZE, BLOCK_SIZE), 2)

def draw_block(x, y):
    pygame.draw.rect(screen, BLACK, ((x * BLOCK_SIZE) + blank, (y * BLOCK_SIZE) + blank, BLOCK_SIZE, BLOCK_SIZE))

def draw_current_block():
    for i in range(len(current_block)):
        for j in range(len(current_block[0])):
            if current_block[i][j] != '':
                draw_block(current_block_position[1] + j, current_block_position[0] + i)

def draw_game_over():
    screen.blit(game_over_text, game_over_rect)

def button_click_action():
    global game
    game = True
    print('start')

def check_full_line():
    for i in range(BOARD_SIZE[0]):
        if all(board[i]):
            board[i] = np.zeros(BOARD_SIZE[1], dtype=str)
            board[1:i+1] = board[:i]
            board[0] = np.zeros(BOARD_SIZE[1], dtype=str)

def update_board():
    for i in range(BOARD_SIZE[0]):
        for j in range(BOARD_SIZE[1]):
            if board[i, j] != '':
                draw_block(j, i)

def is_valid_move(new_position, block):
    for i in range(len(block)):
        for j in range(len(block[0])):
            if (
                block[i][j] != '' and
                (new_position[0] + i >= BOARD_SIZE[0] or new_position[1] + j < 0 or new_position[1] + j >= BOARD_SIZE[1] or
                 board[new_position[0] + i, new_position[1] + j] != '')
            ):
                return False
    return True
def place_block_on_board():
    for i in range(len(current_block)):
        for j in range(len(current_block[0])):
            if current_block[i][j] != '':
                board[current_block_position[0] + i, current_block_position[1] + j] = '1'

def is_game_over():
    return any(board[0])

# 초기 게임 설정
reset_game()

running = True
clock = pygame.time.Clock()

while running:
    move_block_down()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect((button_x, button_y + button_control, button_width, button_height)).collidepoint(mouse_pos):
                button_click_action()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_block_left()
            elif event.key == pygame.K_RIGHT:
                move_block_right()
            elif event.key == pygame.K_UP:
                rotate_block()

    if game:
        check_full_line()

        screen.fill(WHITE)
        draw_board()
        draw_current_block()
        update_board()
        if is_game_over():
            draw_game_over()
            reset_game()
        pygame.display.flip()
    else:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (button_x, button_y + button_control, button_width, button_height))
        screen.blit(button_text, text_rect)
        pygame.display.flip()

    clock.tick(5)  # Adjust the speed as needed

pygame.quit()