import math

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

word = words.get_random_word().upper()
guessed = []

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


def draw():
    window.fill((255, 255, 255))

    # draw title
    text = FONT.render("HANGMAN GAME", 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    displayed_word = ""
    for letter in word:
        if letter in guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    text = FONT.render(displayed_word, 1, BLACK)
    window.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    window.blit(images[game_status], (120, 70))
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
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                game_status += 1
        draw()


while True:
    main()
