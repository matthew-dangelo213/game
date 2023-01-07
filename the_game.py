import sys

import pygame

pygame.init()

w = 320
h = 240
surface = pygame.display.set_mode((w, h))
p_color = (255, 0, 0)
# ground_colors = [(0, 100, 0), (111, 78, 55), (255, 165, 0), (255, 140, 0)]
# gc_index = 0
dirt_color = (111, 78, 55)
grass_color = dirt_color
planted_color = (255, 213, 128)
grown_color = (255, 165, 0)
dead_color = (0, 0, 0)
current_time = 0
time_planted = 0
clock = pygame.time.Clock()
tx = 50
ty = 50
px = 60
py = 60
p_size = 30
movement_speed = 5
growth_time = 5000
death_time = 10000
seed_planted = False
surface.fill("green")
pygame.draw.rect(surface, dirt_color, pygame.Rect(tx, ty, w - (tx * 2), h - (ty * 2)))
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
				if not seed_planted and px > tx and px < w - tx - p_size and py > ty and py < h - ty - p_size:
					seed_planted = True
					grass_color = planted_color
					time_planted = pygame.time.get_ticks()
				elif seed_planted and px > tx and px < w - tx - p_size and py > ty and py < h - ty - p_size:
					grass_color = dirt_color
					seed_planted = False
					time_planted = -1
					
	
	current_time = pygame.time.get_ticks()

	if px > tx and px < w - tx - p_size and py > ty and py < h - ty - p_size:
		p_color = (255, 255, 255)
	else:
		p_color = (255, 0, 0)	

	if seed_planted and current_time - time_planted > growth_time:
		grass_color = grown_color


	if seed_planted and current_time - time_planted > death_time + growth_time:
		grass_color = dead_color

	surface.fill("green")
	pygame.draw.rect(surface, grass_color, pygame.Rect(tx, ty, w - (tx * 2), h - (ty * 2)))
	pygame.draw.rect(surface, p_color, pygame.Rect(px, py, p_size, p_size))
	print(f"current time: {current_time} button press time: {time_planted}")
	pygame.display.flip()
	clock.tick(60)