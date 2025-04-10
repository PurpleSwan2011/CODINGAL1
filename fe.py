import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Elements Display')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up font
font = pygame.font.SysFont(None, 55)

# Function to display text
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw shapes
    pygame.draw.rect(screen, red, (50, 50, 100, 50))  # Rectangle
    pygame.draw.circle(screen, green, (200, 200), 50)  # Circle
    pygame.draw.line(screen, blue, (300, 300), (400, 400), 5)  # Line

    # Display text
    display_text('Hello, Pygame!', black, 450, 100)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
