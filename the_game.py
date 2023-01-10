import sys

import pygame

pygame.init()

w = 320 * 2
h = 240 * 2
surface = pygame.display.set_mode((w, h))
p_color = (128, 0, 128)
dirt_color = (111, 78, 55)
planted_color = (255, 160, 160)
grown_color = (255, 0, 0)
dead_color = (0, 0, 0)
grass_color_tl = dirt_color
grass_color_tr = dirt_color
grass_color_bl = dirt_color
grass_color_br = dirt_color
current_time = 0
time_planted_tl = 0
time_planted_tr = 0
time_planted_bl = 0
time_planted_br = 0
fruit_collected = 0
fruit_price = 50
clock = pygame.time.Clock()
tx = 30
ty = 30
p_size = 30
px = 320 - (p_size / 2)
py = 240 - (p_size / 2)
movement_speed = 100
growth_time = 2500
death_time = 5000
seed_planted_tl = False
seed_planted_tr = False
seed_planted_bl = False
seed_planted_br = False
surface.fill("green")
font = pygame.font.SysFont("Times New Roman", 38)
collected_display = font.render(str(fruit_collected), 1, "black")
cash_display = font.render("$" + str(fruit_collected * fruit_price), 1, "black")
topleft_rect = pygame.Rect(tx, ty, (w / 2) - (tx * 2), (h / 2) - (ty * 2))
topright_rect = pygame.Rect((tx * 3) + (w / 2) - (tx * 2), ty, (w / 2) - (tx * 2), (h / 2) - (ty * 2))
botleft_rect = pygame.Rect(tx, (ty * 3) + (h / 2) - (ty * 2), (w / 2) - (tx * 2), (h / 2) - (ty * 2))
botright_rect = pygame.Rect((tx * 3) + (w / 2) - (tx * 2), (ty * 3) + (h / 2) - (ty * 2), (w / 2) - (tx * 2), (h / 2) - (ty * 2))
pygame.draw.rect(surface, dirt_color, topleft_rect)
pygame.draw.rect(surface, dirt_color, topright_rect)
pygame.draw.rect(surface, dirt_color, botleft_rect)
pygame.draw.rect(surface, dirt_color, botright_rect)
player_rect = pygame.Rect(px, py, p_size, p_size)
pygame.draw.rect(surface, p_color, player_rect)
surface.blit(collected_display, (20, 20))
surface.blit(cash_display, (50, 50))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player_rect.move_ip(0, -movement_speed)
			elif event.key == pygame.K_a:
				player_rect.move_ip(-movement_speed, 0)
			elif event.key == pygame.K_s:
				player_rect.move_ip(0, movement_speed)
			elif event.key == pygame.K_d:
				player_rect.move_ip(movement_speed, 0)			
			elif event.key == pygame.K_SPACE:	
				if not seed_planted_tl and (topleft_rect.contains(player_rect)):
					seed_planted_tl = True
					grass_color_tl = planted_color
					time_planted_tl = pygame.time.get_ticks()
				elif seed_planted_tl and (topleft_rect.contains(player_rect)) and grass_color_tl != grown_color:
					grass_color_tl = dirt_color
					seed_planted_tl = False
					time_planted_tl = -1
				elif seed_planted_tl and (topleft_rect.contains(player_rect)) and grass_color_tl == grown_color:
					fruit_collected += 1
					grass_color_tl = dirt_color
					seed_planted_tl = False
					time_planted_tl = -1

				if not seed_planted_tr and (topright_rect.contains(player_rect)):
					seed_planted_tr = True
					grass_color_tr = planted_color
					time_planted_tr = pygame.time.get_ticks()
				elif seed_planted_tr and (topright_rect.contains(player_rect)) and grass_color_tr != grown_color:
					grass_color_tr = dirt_color
					seed_planted_tr = False
					time_planted_tr = -1
				elif seed_planted_tr and (topright_rect.contains(player_rect)) and grass_color_tr == grown_color:
					fruit_collected += 1
					grass_color_tr = dirt_color
					seed_planted_tr = False
					time_planted_tr = -1

				if not seed_planted_bl and (botleft_rect.contains(player_rect)):
					seed_planted_bl = True
					grass_color_bl = planted_color
					time_planted_bl = pygame.time.get_ticks()
				elif seed_planted_bl and (botleft_rect.contains(player_rect)) and grass_color_bl != grown_color:
					grass_color_bl = dirt_color
					seed_planted_bl = False
					time_planted_bl = -1
				elif seed_planted_bl and (botleft_rect.contains(player_rect)) and grass_color_bl == grown_color:
					fruit_collected += 1
					grass_color_bl = dirt_color
					seed_planted_bl = False
					time_planted_bl = -1											

				if not seed_planted_br and (botright_rect.contains(player_rect)):
					seed_planted_br = True
					grass_color_br = planted_color
					time_planted_br = pygame.time.get_ticks()
				elif seed_planted_br and (botright_rect.contains(player_rect)) and grass_color_br != grown_color:
					grass_color_br = dirt_color
					seed_planted_br = False
					time_planted_br = -1
				elif seed_planted_br and (botright_rect.contains(player_rect)) and grass_color_br == grown_color:
					fruit_collected += 1
					grass_color_br = dirt_color
					seed_planted_br = False
					time_planted_br = -1	

	current_time = pygame.time.get_ticks()

	# if topleft_rect.contains(player_rect) or topright_rect.contains(player_rect) or botleft_rect.contains(player_rect) or botright_rect.contains(player_rect):
	# 	p_color = (255, 255, 255)
	# else:
	# 	p_color = (255, 0, 0)	

	if seed_planted_tl and current_time - time_planted_tl > growth_time:
		grass_color_tl = grown_color
	if seed_planted_tl and current_time - time_planted_tl > death_time + growth_time:
		grass_color_tl = dead_color

	if seed_planted_tr and current_time - time_planted_tr > growth_time:
		grass_color_tr = grown_color
	if seed_planted_tr and current_time - time_planted_tr > death_time + growth_time:
		grass_color_tr = dead_color

	if seed_planted_bl and current_time - time_planted_bl > growth_time:
		grass_color_bl = grown_color
	if seed_planted_bl and current_time - time_planted_bl > death_time + growth_time:
		grass_color_bl = dead_color

	if seed_planted_br and current_time - time_planted_br > growth_time:
		grass_color_br = grown_color
	if seed_planted_br and current_time - time_planted_br > death_time + growth_time:
		grass_color_br = dead_color

	surface.fill("green")
	pygame.draw.rect(surface, grass_color_tl, topleft_rect)
	pygame.draw.rect(surface, grass_color_tr, topright_rect)
	pygame.draw.rect(surface, grass_color_bl, botleft_rect)
	pygame.draw.rect(surface, grass_color_br, botright_rect)
	pygame.draw.rect(surface, p_color, player_rect)
	collected_display = font.render(str(fruit_collected), 1, "black")
	cash_display = font.render(str(fruit_collected * fruit_price), 1, "black")
	surface.blit(collected_display, (5, 20))
	surface.blit(cash_display, (5, 50))
	pygame.display.flip()
	clock.tick(60)
