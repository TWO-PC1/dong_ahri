import pygame 
import numpy as np
import random
BOARD_SIZE = 10

board = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)
for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j]='0'











           
def generate_mine():
    a=0
    while(a<=5):
        x=random.randint(0,BOARD_SIZE-1)
        y=random.randint(0,BOARD_SIZE-1)
        if board[x][y]=='0':
           board[x][y]='*'
           a+=1
        
            
            
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j]=='*':
                
                if i-1>=0 and j>=0:
                    if board[i-1][j]!='*':
                        num=int(board[i-1][j])
                        board[i-1][j]=str(num+1)
                if i>=0 and j-1>=0:
                    if board[i][j-1]!='*':
                        num=int(board[i][j-1])
                        board[i][j-1]=str(num+1)
                if i-1>=0 and j-1>=0:
                    if board[i-1][j-1]!='*':
                        num=int(board[i-1][j-1])
                        board[i-1][j-1]=str(num+1)
                if i-1>=0 and j+1>=0 and j+1<=BOARD_SIZE-1:
                    if board[i-1][j+1]!='*':
                        num=int(board[i-1][j+1])
                        board[i-1][j+1]=str(num+1)
                if i+1>=0 and j+1>=0 and j+1<=BOARD_SIZE-1 and i+1<=BOARD_SIZE-1:
                    if board[i+1][j+1]!='*':
                        num=int(board[i+1][j+1])
                        board[i+1][j+1]=str(num+1)
                if i>=0 and j+1>=0 and j+1<=BOARD_SIZE-1:
                    if board[i][j+1]!='*':
                        num=int(board[i][j+1])
                        board[i][j+1]=str(num+1)
                if i+1>=0 and j-1>=0 and i+1<=BOARD_SIZE-1:
                    if board[i+1][j-1]!='*':
                        num=int(board[i+1][j-1])
                        board[i+1][j-1]=str(num+1)
                if i+1>=0 and j>=0 and i+1<=BOARD_SIZE-1:
                    if board[i+1][j]!='*':
                        num=int(board[i+1][j])
                        board[i+1][j]=str(num+1)
                        
                    
                    
                    
                  
                        
                    
                
            
            
            
            
            
            
    print(board)
        
            
generate_mine()





WIDTH, HEIGHT=800,800

BLOCK_SIZE= int(WIDTH / BOARD_SIZE-(WIDTH / BOARD_SIZE)/10)
blank = (WIDTH - (BLOCK_SIZE * BOARD_SIZE)) / 2

print(blank)
def draw_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
              # 그리드 그리기
            pygame.draw.rect(screen, BLACK, ((j * BLOCK_SIZE) + blank, (i * BLOCK_SIZE)+blank, BLOCK_SIZE, BLOCK_SIZE), 2)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            for num in range(8):
                if board[i][j] !='*':
                    if int(board[i][j]) == num+1:
                        block_x = j * BLOCK_SIZE + (BLOCK_SIZE - font.size(num)[0]) / 2 + blank
                        block_y = i * BLOCK_SIZE + (BLOCK_SIZE - font.size(num)[1]) / 2 + blank 
                        button_text = font.render(num, True, BLACK)
                        screen.blit(button_text, (block_x, block_y))

                    



pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('게임')












font=pygame.font.Font(None,36)

WHITE=(255,255,255)
BLACK=(0,0,0)

button_width, button_height = 200, 50
button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT - button_height) // 2
button_text=font.render('test', True, WHITE)
button_control=100
text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2+button_control))

game = False
def button_click_action():
    global game
    game = True
    print('start')

runnning=True
while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
           
        
                    
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            
            if pygame.Rect((button_x, button_y +button_control, button_width, button_height)).collidepoint(mouse_pos):
                button_click_action()
                
                
               
    if game:
        screen.fill(WHITE) 
        draw_board()
        pygame.display.flip() 
        
        
        
        
    else:            
        screen.fill(WHITE)    
        pygame.draw.rect(screen, BLACK, (button_x, button_y +button_control, button_width, button_height)) 
        screen.blit(button_text, text_rect)
        pygame.display.flip() 