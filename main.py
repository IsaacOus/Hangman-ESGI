import pygame

# Display
import hangman

pygame.init()
WIDTH, HEIGHT = 800, 500
BLACK = (0, 0, 0)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman-ESGI!")

# Images
images = []
for i in range(7):
    images.append(pygame.image.load("images/Hangman-" + str(i) + ".png"))

# Font


FPS = 60
run = True
clock = pygame.time.Clock()


game = hangman.Hangman()
game.start_game()


# Draw word
display_word = [letter if letter in game.used_letter else '-' for letter in game.pickedWord]

# TODO Draw function

while run:
    clock.tick(FPS)
    window.fill((255, 255, 255))
    window.blit(images[game.get_hangman_status()], (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
