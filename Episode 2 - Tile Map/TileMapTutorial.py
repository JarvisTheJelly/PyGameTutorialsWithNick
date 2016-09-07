import pygame
import TileHandler

def run():
    """Holds the main functionality of the program

    Initializes the screen, handles the main game loop.
    """

    pygame.init()

    # Creates a window based on the size of the screen we establish below.
    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("Introduction to PyGame. Hello, YouTube!")

    tile_handler = TileHandler.TileHandler()
    tile_handler.fill_array_random()

    # Main game loop
    done = False
    while not done:

        # Handles events from the player, checks to see if they are done playing.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        # Fill the screen with black
        screen.fill((0, 0, 0))

        tile_handler.render(screen)

        pygame.display.update()

    # Handle destruction / cleanup
    pygame.quit()

if __name__ == "__main__":
    run()

