import pygame
from queue import Queue
from cell import Cell, Food
from snake import Snake

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("your_font.ttf", 25)

WIDTH, HEIGHT = 620, 620
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


def draw(window, grid, snake, food):
    window.fill((0, 0, 0))
    # for row in grid:
    #     for cell in row:
    #         cell.draw(window)
    snake.draw(window)
    food.draw(window)
    SCORE = myfont.render(f"SCORE: {snake.score}", False, (255, 255, 255))
    window.blit(SCORE, (WIDTH - 3 * (WIDTH // 20), 0))
    pygame.display.update()


def build_grid(Wwindow, cell_size):
    grid = []
    cells = WIDTH // cell_size
    for i in range(cells):
        row = []
        for j in range(cells):
            row.append(Cell((i, j), WIDTH, HEIGHT))
        grid.append(row)
    return grid


def game(grid, food, snake):
    run = True
    while run:
        draw(window, grid, snake, food)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        navigation_key = pygame.key.get_pressed()
        if navigation_key[pygame.K_UP] and snake.getDirection() != [0, 1]:
            snake.setDirection([0, -1])
        if navigation_key[pygame.K_DOWN] and snake.getDirection() != [0, -1]:
            snake.setDirection([0, 1])
        if navigation_key[pygame.K_RIGHT] and snake.getDirection() != [-1, 0]:
            snake.setDirection([1, 0])
        if navigation_key[pygame.K_LEFT] and snake.getDirection() != [1, 0]:
            snake.setDirection([-1, 0])

        if (
            snake.getIndex()[0] == food.index[0]
            and snake.getIndex()[1] == food.index[1]
        ):
            snake.score += 1
            snake.length += 1
            snake.body.append(
                [
                    snake.body[-1][0] - snake.path[-1][0],
                    snake.body[-1][1] - snake.path[-1][1],
                ]
            )
            snake.path.append(
                [
                    snake.path[-1][0],
                    snake.path[-1][1],
                ]
            )
            food.reset(WIDTH)
        snake.move(grid)
        if snake.dead():
            main()
        clock.tick(20)
    pygame.quit()


def main():
    run = True
    grid = build_grid(window, 20)
    food = Food(WIDTH, HEIGHT)
    snake = Snake(WIDTH, HEIGHT)
    game(grid, food, snake)


if __name__ == "__main__":
    main()