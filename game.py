import pygame 



WIDTH, HEIGHT=800,800


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




runnning=True
while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning=False
    screen.fill(WHITE)    
    pygame.draw.rect(screen, BLACK, (button_x, button_y +button_control, button_width, button_height)) 
    screen.blit(button_text, text_rect)
    pygame.display.flip() 