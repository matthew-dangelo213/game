import sys

import pygame

pygame.init()

w = 320
h = 240
surface = pygame.display.set_mode((w, h))
p_color = (255, 0, 0)
ground_colors = [(0, 100, 0), (111, 78, 55), (255, 165, 0), (255, 140, 0)]
gc_index = 0
# grass_color = (0, 100, 0)
# dirt_color = (111, 78, 55)
# planted_color = (255, 165, 0)
# grown_color = (255, 140, 0)
clock = pygame.time.Clock()
tx = 50
ty = 50
px = 30
py = 30
p_size = 30
movement_speed = 5
surface.fill("green")
pygame.draw.rect(surface, ground_colors[gc_index], pygame.Rect(tx, ty, w - (tx * 2), h - (ty * 2)))
pygame.draw.rect(surface, p_color, pygame.Rect(px, py, p_size, p_size))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				py -= movement_speed
			elif event.key == pygame.K_a:
				px -= movement_speed
			elif event.key == pygame.K_s:
				py += movement_speed
			elif event.key == pygame.K_d:
				px += movement_speed				
			elif event.key == pygame.K_SPACE:	
				if px > tx and px < w - tx - p_size and py > ty and py < h - ty - p_size:
					gc_index += 1
	
	if px > tx and px < w - tx - p_size and py > ty and py < h - ty - p_size:
		p_color = (255, 255, 255)
	else:
		p_color = (255, 0, 0)	

	surface.fill("green")
	pygame.draw.rect(surface, ground_colors[gc_index], pygame.Rect(tx, ty, w - (tx * 2), h - (ty * 2)))
	pygame.draw.rect(surface, p_color, pygame.Rect(px, py, p_size, p_size))
	pygame.display.flip()
	clock.tick(60)