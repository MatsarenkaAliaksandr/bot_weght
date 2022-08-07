import pygame
import random

pygame.init()
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
gray = (192, 192, 192)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

game_over = False
x1 = 300
y1 = 400

x2 = round(random.randrange(0, 790) / 10.0) * 10.0
y2 = round(random.randrange(0, 490) / 10.0) * 10.0

snake_list = []
length_snake = 1

score = pygame.font.SysFont("SansSerif", 35)

x1_change = 0
y1_change = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 >= 800 or x1 < 0 or y1 >= 500 or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(gray)
    pygame.draw.rect(dis, red, (x2, y2, 10, 10))
    pygame.draw.rect(dis, blue, (x1, y1, 10, 10))
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    if len(snake_list) > length_snake:
        del snake_list[0]

    for x in snake_list:
        pygame.draw.rect(dis, blue, (x[0], x[1], 10, 10))
        value = score.render("Your Score: " + str(length_snake-1), True, white)
        dis.blit(value, [0, 0])

    pygame.display.update()

    if x1 == x2 and y1 == y2:
        x2 = round(random.randrange(0, 790) / 10.0) * 10.0
        y2 = round(random.randrange(0, 490) / 10.0) * 10.0
        length_snake += 1

    clock.tick(15)

pygame = quit()
quit()
