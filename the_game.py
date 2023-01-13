import sys

import pygame

pygame.init()

w = 320 * 2
h = 240 * 2
surface = pygame.display.set_mode((w, h))
p_color = (128, 0, 128)
dirt_color = (111, 78, 55)
seeds = {"Tomato": {"color": (255, 20, 0), "price": 50, "exp": 1, "grow_time": 2500}, "Blueberry": {"color": (50, 0, 255), "price": 300, "exp": 2, "grow_time": 4000}, "Pumpkin": {"color": (255, 117, 24), "price": 1000, "exp": 5, "grow_time": 9000}}
current_seed = "Tomato"
seed_options = ["Tomato", "Blueberry", "Pumpkin"]
seed_options_index = seed_options.index(current_seed)
grown_color_tl = seeds[current_seed]["color"]
grown_color_tr = seeds[current_seed]["color"]
grown_color_bl = seeds[current_seed]["color"]
grown_color_br = seeds[current_seed]["color"]
growth_time_tl = seeds[current_seed]["grow_time"]
growth_time_tr = seeds[current_seed]["grow_time"]
growth_time_bl = seeds[current_seed]["grow_time"]
growth_time_br = seeds[current_seed]["grow_time"]
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
clock = pygame.time.Clock()
tx = 1
ty = 1
p_size = 30
px = 320 - (p_size / 2)
py = 240 - (p_size / 2)
movement_speed = 100
death_time = 100000
earned_total = 0
p_level = 0
exp_total = 0
seed_planted_tl = None
seed_planted_tr = None
seed_planted_bl = None
seed_planted_br = None
surface.fill("green")
font = pygame.font.SysFont("Times New Roman", 38)
lvl_display = font.render("Lvl: " + str(p_level), 1, "black")
exp_display = font.render("Exp: " + str(exp_total), 1, "black")
cash_display = font.render("$" + str(earned_total), 1, "black")
fruit_display = font.render(current_seed, 1, "black")
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
surface.blit(lvl_display, (5, 1))
surface.blit(exp_display, (5, 20))
surface.blit(cash_display, (5, 50))
surface.blit(fruit_display, (5, 80))
pygame.display.flip()

def lighten(color):
	r = color[0] + 70
	g = color[1] + 70
	b = color[2] + 70
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255
	return (r, g, b)

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
			elif event.key == pygame.K_e:
				seed_options_index += 1
				seed_options_index %= len(seed_options)
				current_seed = seed_options[seed_options_index]
			elif event.key == pygame.K_SPACE:	
				if not seed_planted_tl and (topleft_rect.contains(player_rect)):
					seed_planted_tl = current_seed
					grass_color_tl = lighten(seeds[current_seed]["color"])
					grown_color_tl = seeds[current_seed]["color"]
					growth_time_tl = seeds[current_seed]["grow_time"]
					time_planted_tl = pygame.time.get_ticks()
				elif seed_planted_tl and (topleft_rect.contains(player_rect)) and grass_color_tl != grown_color_tl:
					grass_color_tl = dirt_color
					seed_planted_tl = None
					time_planted_tl = -1
				elif seed_planted_tl and (topleft_rect.contains(player_rect)) and grass_color_tl == grown_color_tl:
					fruit_collected += 1
					earned_total += seeds[seed_planted_tl]["price"]
					exp_total += seeds[seed_planted_tl]["exp"]
					grass_color_tl = dirt_color
					seed_planted_tl = None
					time_planted_tl = -1

				if not seed_planted_tr and (topright_rect.contains(player_rect)):
					seed_planted_tr = current_seed
					grass_color_tr = lighten(seeds[current_seed]["color"])
					grown_color_tr = seeds[current_seed]["color"]
					growth_time_tr = seeds[current_seed]["grow_time"]
					time_planted_tr = pygame.time.get_ticks()
				elif seed_planted_tr and (topright_rect.contains(player_rect)) and grass_color_tr != grown_color_tr:
					grass_color_tr = dirt_color
					seed_planted_tr = None
					time_planted_tr = -1
				elif seed_planted_tr and (topright_rect.contains(player_rect)) and grass_color_tr == grown_color_tr:
					fruit_collected += 1
					earned_total += seeds[seed_planted_tr]["price"]
					exp_total += seeds[seed_planted_tr]["exp"]
					grass_color_tr = dirt_color
					seed_planted_tr = None
					time_planted_tr = -1

				if not seed_planted_bl and (botleft_rect.contains(player_rect)):
					seed_planted_bl = current_seed
					grass_color_bl = lighten(seeds[current_seed]["color"])
					grown_color_bl = seeds[current_seed]["color"]
					growth_time_bl = seeds[current_seed]["grow_time"]
					time_planted_bl = pygame.time.get_ticks()
				elif seed_planted_bl and (botleft_rect.contains(player_rect)) and grass_color_bl != grown_color_bl:
					grass_color_bl = dirt_color
					seed_planted_bl = None
					time_planted_bl = -1
				elif seed_planted_bl and (botleft_rect.contains(player_rect)) and grass_color_bl == grown_color_bl:
					fruit_collected += 1
					earned_total += seeds[seed_planted_bl]["price"]
					exp_total += seeds[seed_planted_bl]["exp"]
					grass_color_bl = dirt_color
					seed_planted_bl = None
					time_planted_bl = -1											

				if not seed_planted_br and (botright_rect.contains(player_rect)):
					seed_planted_br = current_seed
					grass_color_br = lighten(seeds[current_seed]["color"])
					grown_color_br = seeds[current_seed]["color"]
					growth_time_br = seeds[current_seed]["grow_time"]
					time_planted_br = pygame.time.get_ticks()
				elif seed_planted_br and (botright_rect.contains(player_rect)) and grass_color_br != grown_color_br:
					grass_color_br = dirt_color
					seed_planted_br = None
					time_planted_br = -1
				elif seed_planted_br and (botright_rect.contains(player_rect)) and grass_color_br == grown_color_br:
					fruit_collected += 1
					earned_total += seeds[seed_planted_br]["price"]
					exp_total += seeds[seed_planted_br]["exp"]
					grass_color_br = dirt_color
					seed_planted_br = None
					time_planted_br = -1	

	current_time = pygame.time.get_ticks()

	if seed_planted_tl and current_time - time_planted_tl > growth_time_tl:
		grass_color_tl = grown_color_tl
	if seed_planted_tl and current_time - time_planted_tl > death_time + growth_time_tl:
		grass_color_tl = dead_color

	if seed_planted_tr and current_time - time_planted_tr > growth_time_tr:
		grass_color_tr = grown_color_tr
	if seed_planted_tr and current_time - time_planted_tr > death_time + growth_time_tr:
		grass_color_tr = dead_color

	if seed_planted_bl and current_time - time_planted_bl > growth_time_bl:
		grass_color_bl = grown_color_bl
	if seed_planted_bl and current_time - time_planted_bl > death_time + growth_time_bl:
		grass_color_bl = dead_color

	if seed_planted_br and current_time - time_planted_br > growth_time_br:
		grass_color_br = grown_color_br
	if seed_planted_br and current_time - time_planted_br > death_time + growth_time_br:
		grass_color_br = dead_color

	if exp_total >= 20:
		p_level = 2

	if exp_total >= 50:
		p_level = 3

	surface.fill("green")
	pygame.draw.rect(surface, grass_color_tl, topleft_rect)
	pygame.draw.rect(surface, grass_color_tr, topright_rect)
	pygame.draw.rect(surface, grass_color_bl, botleft_rect)
	pygame.draw.rect(surface, grass_color_br, botright_rect)
	pygame.draw.rect(surface, p_color, player_rect)
	lvl_display = font.render("Lvl: " + str(p_level), 1, "black")
	exp_display = font.render("Exp: " + str(exp_total), 1, "black")
	cash_display = font.render("$" + str(earned_total), 1, "black")
	fruit_display = font.render(current_seed, 1, "black")
	surface.blit(lvl_display, (5, 1))
	surface.blit(exp_display, (5, 35))
	surface.blit(cash_display, (5, 67))
	surface.blit(fruit_display, (5, 100))
	pygame.display.flip()
	clock.tick(60)
