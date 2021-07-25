import pygame
import hangman

# Display
import words

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
FONT = pygame.font.SysFont('Arial', 35)

# Variables

game_status = 0
word = words.get_random_word()
guessed = []


def draw():
    window.fill((255, 255, 255))

    displayed_word = ""
    for letter in word:
        if letter in guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    text = FONT.render(displayed_word, 1, BLACK)
    window.blit(text, (400, 200))
    window.blit(images[game_status], (150, 90))
    pygame.display.update()


def main():
    global game_status
    FPS = 60
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

        draw()



while True:
    main()
