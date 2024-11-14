import pygame
import random

grid_width = 20
grid_height = 16
grid_square = 32
screen_width = 640
screen_height = 512

def draw_grid(screen):
    for i in range(0, screen_width, grid_square):
        pygame.draw.line(screen, (100, 0, 0), (i,0), (i, screen_width))
    for j in range(0, screen_height, grid_square):
        pygame.draw.line(screen, (100, 0, 0), (0,j), (screen_width, j))



def main():

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        x = 0
        y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (x <= event.pos[0] < (x + grid_square)) and (y <= event.pos[1] < (y + grid_square)):
                        x = random.randrange(0, grid_width) * grid_square
                        y = random.randrange(0, grid_height) * grid_square
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
