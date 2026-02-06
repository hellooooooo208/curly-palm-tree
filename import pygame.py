import pygame

print("Made by Nick")          
print("github:hellooooooo208")

pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


font = pygame.font.SysFont("arial", 48)          

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

   
    screen.fill((255, 255, 255))

    
    screen_width, screen_height = screen.get_size()

    
    square_size = min(screen_width, screen_height) // 5
    square_x = (screen_width - square_size) // 2
    square_y = (screen_height - square_size) // 2
    pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size))

   
    text = font.render("Made by Nick", True, (0, 0, 0))         
    text_rect = text.get_rect(center=(screen_width // 2, 100))   
    screen.blit(text, text_rect)                                 

    # Optional: Add your GitHub below it
    github_text = font.render("github:hellooooooo208", True, (50, 50, 50))  
    github_rect = github_text.get_rect(center=(screen_width // 2, 170))     # a bit lowe
    screen.blit(github_text, github_rect)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
