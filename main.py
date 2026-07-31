import pygame
import math
from heart import heart_points
from particle import Particle
from config import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Heart")

clock = pygame.time.Clock()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Load heart points
raw_points = heart_points()

points = []
for x, y in raw_points:
    points.append((CENTER_X + x, CENTER_Y + y))

particles = []

draw_index = 0

pulse = 0

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    # Draw the heart progressively
    if draw_index < len(points):

        for _ in range(4):      # drawing speed

            if draw_index < len(points):

                particles.append(
                    Particle(points[draw_index])
                )

                draw_index += 1

    # Heart pulse animation
    pulse += 0.05

    scale = 1 + math.sin(pulse) * 0.03

    # Glow
    for p in particles:

        tx = CENTER_X + (p.tx - CENTER_X) * scale
        ty = CENTER_Y + (p.ty - CENTER_Y) * scale

        p.tx = tx
        p.ty = ty

        p.update()

        p.draw(screen)

    # Floating sparkle particles
    for i in range(40):

        x = (i * 97 + pygame.time.get_ticks() * 0.05) % WIDTH

        y = (i * 53 + pygame.time.get_ticks() * 0.03) % HEIGHT

        pygame.draw.circle(
            screen,
            (255, 170, 220),
            (int(x), int(y)),
            1
        )

    pygame.display.flip()

pygame.quit()
