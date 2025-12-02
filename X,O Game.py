
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("X/O GAME")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 150)

run = True
while run:
    screen.fill(WHITE)

    # Draw grid lines
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

    # Draw X and O on the board
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * 200 + 50, row * 200 + 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            if board[row][col] == "":
                board[row][col] = player
                player = "O" if player == "X" else "X"  # switch player

    pygame.display.update()

pygame.quit()