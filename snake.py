import pygame
import random
pygame.init()

SPEED = 10
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 800, 600

body = 0
kus_hada = 10
hadi_telo = []

SCORE_FONT = pygame.font.SysFont('opensans', 40)
GAME_OVER_FONT = pygame.font.SysFont('opensans', 150)
pygame.display.set_caption("hadicek")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def had(x_hada, y_hada, x_zmena, y_zmena, x_ovoce, y_ovoce, delka_hada,run):
    for x in hadi_telo:
        pygame.draw.rect(WIN, GREEN, [x[0], x[1], kus_hada, kus_hada])
    global hlava
    hlava = []
    hlava.append(x_hada)
    hlava.append(y_hada)
    hadi_telo.append(hlava)
    if len(hadi_telo) > delka_hada:
        del hadi_telo[0]



def ovoce(kus_hada, x_hada, y_hada, x_ovoce, y_ovoce, delka_hada):
    pygame.draw.rect(WIN, RED, [x_ovoce, y_ovoce, kus_hada, kus_hada])

def game_over():
    game_over = GAME_OVER_FONT.render("GAME OVER", 1, WHITE)
    WIN.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, HEIGHT // 2 - game_over.get_height() //2))
    pygame.display.update()
    pygame.time.delay(4000)

def score(delka_hada):
    body = delka_hada - 1
    score = SCORE_FONT.render(f"score: {body}", 1, WHITE)
    WIN.blit(score, (10, 10))
def menu():
    menu_run = True
    while menu_run:
        WIN.blit(BLACK, (0, 0))
        pass

def hra():
    x_hada = WIDTH // 2
    y_hada = HEIGHT//2
    x_zmena = 0
    y_zmena = 0
    delka_hada = 1
    x_ovoce = round(random.randrange(0, WIDTH - kus_hada * 2) / 10) * 10
    y_ovoce = round(random.randrange(0, HEIGHT - kus_hada * 2) / 10) * 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_zmena = 0
                    y_zmena = -SPEED
                if event.key == pygame.K_DOWN:
                    x_zmena = 0
                    y_zmena = SPEED
                if event.key == pygame.K_LEFT:
                    x_zmena = -SPEED
                    y_zmena = 0
                if event.key == pygame.K_RIGHT:
                    x_zmena = SPEED
                    y_zmena = 0
        WIN.fill(BLACK)
        x_hada += x_zmena
        y_hada += y_zmena

        if x_hada == x_ovoce and y_hada == y_ovoce:
            x_ovoce = round(random.randrange(0, WIDTH - kus_hada) / 10) * 10
            y_ovoce = round(random.randrange(0, HEIGHT - kus_hada) / 10) * 10
            delka_hada += 1


        had(x_hada, y_hada, x_zmena, y_zmena, x_ovoce, y_ovoce, delka_hada,run)
        ovoce(kus_hada, x_hada, y_hada, x_ovoce, y_ovoce, delka_hada)
        score(delka_hada)

        if x_hada >= WIDTH or x_hada <= 0 or y_hada >= HEIGHT or y_hada <= 0:
            run = False
            game_over()

        for x in hadi_telo[:-1]:
            if x == hlava:
                run = False
                game_over()
        pygame.display.update()  

    pygame.quit()

hra()