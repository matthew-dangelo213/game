import sys

import pygame

pygame.init()

w = 320
h = 240
surface = pygame.display.set_mode((w, h))
color = (255, 0, 0)
clock = pygame.time.Clock()
background_colors = ["green", "purple", "blue", "yellow", "orange"]
background_index = 0
px = 30
py = 30

surface.fill(background_colors[background_index])

pygame.draw.rect(surface, color, pygame.Rect(px, py, 60, 60))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	background_index = (background_index + 1) % len(background_colors)
	px += 10
	px = min(px, w - 30 - 60)

	surface.fill(background_colors[background_index])
	pygame.draw.rect(surface, color, pygame.Rect(px, py, 60, 60))
	pygame.display.flip()
	clock.tick(5)