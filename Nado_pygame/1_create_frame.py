import pygame

pygame.init() # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JAEMU GAME")

# 이벤트 루프 창이 안닫히도록
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit