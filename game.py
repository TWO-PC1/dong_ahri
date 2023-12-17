import pygame 
import numpy as np
import random
import time
BOARD_SIZE = 10

board = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)
view = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)
for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j]='0'











           
def generate_mine():
    a=0
    while(a<=7):
        
        x=random.randint(0,BOARD_SIZE-1)
        y=random.randint(0,BOARD_SIZE-1)
        if board[x][y]=='0':
           board[x][y]='*'
           a+=1
        
            
            
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j]=='*':
                print('c')
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


def open(x,y):
   
    if(board[x][y]=='0'):
        
        if  x+1<=BOARD_SIZE-1 and not view[x+1][y]=='v':
            view[x+1][y]='v'
            open2(x+1,y)
            
        if  y+1<=BOARD_SIZE-1 and not view[x][y+1]=='v':
            view[x][y+1]='v'
            open3(x,y+1)
        if not view[x-1][y]=='v' and x-1>=0:
            view[x-1][y]='v'
            open4(x-1,y)
        if not view[x][y-1]=='v'and y-1>=0:
            view[x][y-1]='v'
            open5(x,y-1)

def open2(x,y):
    if(board[x][y]=='0'):
        
        if  x+1<=BOARD_SIZE-1 and not view[x+1][y]=='v':
            view[x+1][y]='v'
            open(x+1,y)
            
        if  y+1<=BOARD_SIZE-1 and not view[x][y+1]=='v':
            view[x][y+1]='v'
            open(x,y+1)
        if not view[x-1][y]=='v' and x-1>=0:
            view[x-1][y]='v'
            open(x-1,y)
        if not view[x][y-1]=='v'and y-1>=0:
            view[x][y-1]='v'
            open(x,y-1)

def open3(x,y):
    if(board[x][y]=='0'):
        
        if  x+1<=BOARD_SIZE-1 and not view[x+1][y]=='v':
            view[x+1][y]='v'
            open(x+1,y)
            
        if  y+1<=BOARD_SIZE-1 and not view[x][y+1]=='v':
            view[x][y+1]='v'
            open(x,y+1)
        if not view[x-1][y]=='v' and x-1>=0:
            view[x-1][y]='v'
            open(x-1,y)
        if not view[x][y-1]=='v'and y-1>=0:
            view[x][y-1]='v'
            open(x,y-1)

def open4(x,y):
    if(board[x][y]=='0'):
        
        if  x+1<=BOARD_SIZE-1 and not view[x+1][y]=='v':
            view[x+1][y]='v'
            open(x+1,y)
            
        if  y+1<=BOARD_SIZE-1 and not view[x][y+1]=='v':
            view[x][y+1]='v'
            open(x,y+1)
        if not view[x-1][y]=='v' and x-1>=0:
            view[x-1][y]='v'
            open(x-1,y)
        if not view[x][y-1]=='v'and y-1>=0:
            view[x][y-1]='v'
            open(x,y-1)
      
def open5(x,y):
    if(board[x][y]=='0'):
        
        if  x+1<=BOARD_SIZE-1 and not view[x+1][y]=='v':
            view[x+1][y]='v'
            open(x+1,y)
            
        if  y+1<=BOARD_SIZE-1 and not view[x][y+1]=='v':
            view[x][y+1]='v'
            open(x,y+1)
        if not view[x-1][y]=='v' and x-1>=0:
            view[x-1][y]='v'
            open(x-1,y)
        if not view[x][y-1]=='v'and y-1>=0:
            view[x][y-1]='v'
            open(x,y-1)


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
                if board[i][j] !='*' and view[i][j]=='v':
                    if int(board[i][j]) == num+1:
                        block_x = j * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[0]) / 2 + blank
                        block_y = i * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[1]) / 2 + blank 
                        button_text = font.render(str(num+1), True, BLACK)
                        screen.blit(button_text, (block_x, block_y))
                if board[i][j] =='*'and view[i][j]=='v':
                    block_x = j * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[0]) / 2 + blank
                    block_y = i * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[1]) / 2 + blank 
                    button_text = font.render('*', True, BLACK)
                    screen.blit(button_text, (block_x, block_y))
                if board[i][j] =='0'and view[i][j]=='v':
                    block_x = j * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[0]) / 2 + blank
                    block_y = i * BLOCK_SIZE + (BLOCK_SIZE - font.size('5')[1]) / 2 + blank 
                    button_text = font.render('0', True, BLACK)
                    screen.blit(button_text, (block_x, block_y))


                    



pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('게임')












font=pygame.font.Font(None,60)
Bfont=pygame.font.Font(None,300)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
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
           
        
            if game==True:
                x, y = event.pos
                pos1=(x -BLOCK_SIZE/2) / BLOCK_SIZE
                pos2=(y -BLOCK_SIZE/2) / BLOCK_SIZE
                j, i = int((x -BLOCK_SIZE/2) / BLOCK_SIZE), int((y -BLOCK_SIZE/2) / BLOCK_SIZE)  # blank를 빼서 좌표를 보정
                print(i,j)
                print(pos1,pos2)

                if not i>BLOCK_SIZE and not j>BLOCK_SIZE and pos1>0 and pos2>0:
                    if view[i][j]=='':
                        view[i][j] = "v"
                        open(i,j)
                        if board[i][j] == "*":
                            
                            board = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str)
                            for i in range(BOARD_SIZE):
                                for j in range(BOARD_SIZE):
                                    board[i][j]='0'

                            view = np.zeros([BOARD_SIZE, BOARD_SIZE], dtype=str) 
                            
                            
   

                            button_text=Bfont.render('pang!', True, GRAY)
                            text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2+button_control))
                            screen.blit(button_text, text_rect)
                            pygame.display.flip() 
                            time.sleep(2)
                            generate_mine()
                            
                            
                    v=0
                    for i in range(BOARD_SIZE):
                        for j in range(BOARD_SIZE):
                            if view[i][j]=='v':
                                v+=1
                                if v==BOARD_SIZE**2:
                                    button_text=Bfont.render('win!', True, GRAY)
                                    text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2+button_control))
                                    screen.blit(button_text, text_rect)
                                    pygame.display.flip() 
                                    time.sleep(2)




                            
             
            
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