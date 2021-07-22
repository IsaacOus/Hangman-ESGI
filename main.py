import pygame

# Display
import hangman

pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman-ESGI!")

# Images
images = []
for i in range(7):
    images.append(pygame.image.load("images/Hangman-" + str(i) + ".png"))

FPS = 60
run = True
clock = pygame.time.Clock()

<<<<<<< Updated upstream
while run:
    game = hangman.Hangman()
=======

game = hangman.Hangman()



# Draw word
display_word = [letter if letter in game.used_letter else '-' for letter in game.pickedWord]

# TODO Draw function

while run:
    pygame.event.get()
>>>>>>> Stashed changes
    clock.tick(FPS)
    window.fill((255, 255, 255))
    window.blit(images[game.get_hangman_status()], (0, 0))
    pygame.display.update()

    game.start_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.start_game()

pygame.quit()
