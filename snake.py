import pygame, random

boxsize = 16
size = (512, 512)
matrix = [[0 for y in range(int(size[1]/boxsize))] for x in range(int(size[0]/boxsize))]
snake = [[size[0]/(boxsize*2), size[1]/(boxsize*2)]]
movedir = (1, 0)
fruitpos = [random.randint(0, int(size[0]/boxsize))-1, random.randint(0, int(size[1]/boxsize))-1]
pygame.init()
surface = pygame.display.set_mode(size)
pygame.display.set_caption("snake test")
clock = pygame.time.Clock()
while True:
    clock.tick(2)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not movedir == (1, 0):
                movedir = (-1, 0)
            elif event.key == pygame.K_RIGHT and not movedir == (-1, 0):
                movedir = (1, 0)
            elif event.key == pygame.K_UP and not movedir == (0, 1):
                movedir = (0, -1)
            elif event.key == pygame.K_DOWN and not movedir == (0, -1):
                movedir = (0, 1)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    nextpos = [snake[0][0]+movedir[0], snake[0][1]+movedir[1]]
    if (-1 in nextpos) or (size[0]/boxsize in nextpos) or (nextpos in snake[:-1]):
        snake = [[size[0]/(boxsize*2), size[1]/(boxsize*2)]]
        fruitpos = [random.randint(0, int(size[0]/boxsize))-1, random.randint(0, int(size[1]/boxsize))-1]
    else:
        if nextpos == fruitpos:
            snake.append(snake[len(snake)-1])
            fruitpos = [random.randint(0, int(size[0]/boxsize))-1, random.randint(0, int(size[1]/boxsize))-1]
        for spi in range(1, len(snake)):
            snake[len(snake)-spi] = snake[len(snake)-spi-1]
        snake[0] = nextpos
    surface.fill((0, 0, 0))
    for snakepart in snake:
        pygame.draw.rect(surface, (0, 255, 0), (snakepart[0]*boxsize, snakepart[1]*boxsize, boxsize, boxsize))
    pygame.draw.rect(surface, (255, 255, 0), (fruitpos[0]*boxsize, fruitpos[1]*boxsize, boxsize, boxsize))
    pygame.display.flip()
