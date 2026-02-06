import pygame

print("Made by Nick")          # Still prints to terminal too (optional)
print("github:hellooooooo208")

pygame.init()

# Create fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load a font (Arial or default system font, size 48 pixels)
font = pygame.font.SysFont("arial", 48)          # You can change "arial" to "comicsansms", None (default), etc.

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear screen white
    screen.fill((255, 255, 255))

    # Get screen size for centering everything
    screen_width, screen_height = screen.get_size()

    # --- Draw the square (centered, black) ---
    square_size = min(screen_width, screen_height) // 5
    square_x = (screen_width - square_size) // 2
    square_y = (screen_height - square_size) // 2
    pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size))

    # --- Draw your name/text on screen ---
    # Create text surface (white text with black outline for visibility, or change colors)
    text = font.render("Made by Nick", True, (0, 0, 0))          # black text
    text_rect = text.get_rect(center=(screen_width // 2, 100))   # centered horizontally, 100 pixels from top
    screen.blit(text, text_rect)                                 # "paste" the text onto the screen

    # Optional: Add your GitHub below it
    github_text = font.render("github:hellooooooo208", True, (50, 50, 50))  # darker gray
    github_rect = github_text.get_rect(center=(screen_width // 2, 170))     # a bit lower
    screen.blit(github_text, github_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()