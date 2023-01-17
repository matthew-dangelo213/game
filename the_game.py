import sys

import pygame

TILE_WIDTH = 320
TILE_HEIGHT = 240
N = 2
W = TILE_WIDTH * N
H = TILE_HEIGHT * N
BUFF = 1
DIRT_COLOR = (111, 78, 55)
DEAD_COLOR = (0, 0, 0)
PLAYER_COLOR = (128, 0, 128)
SEEDS = {
	"Tomato": {
		"color": (255, 20, 0),
		"price": 50,
		"exp": 1,
		"grow_time": 2500
	},
	"Blueberry": {
		"color": (50, 0, 255),
		"price": 300,
		"exp": 2,
		"grow_time": 4000
	},
	"Pumpkin": {
		"color": (255, 117, 24),
		"price": 1000,
		"exp": 5,
		"grow_time": 9000
	}
}


def lighten(color):
	return [min(255, x + 60) for x in color]


def is_ready(tile, current_time):
	return current_time - tile["time_planted"] >= SEEDS[tile["seed"]]["grow_time"]


def grass_color(tile, current_time):
	seed = tile["seed"]
	if not seed:
		return DIRT_COLOR
	if seed == "dead":
		return DEAD_COLOR
	if is_ready(tile, current_time):
		return SEEDS[tile["seed"]]["color"]
	else:
		return lighten(SEEDS[tile["seed"]]["color"])
	assert False


def create_tile(i, j):
	return {
		"rect": pygame.rect.Rect((i * TILE_WIDTH) + BUFF, (j * TILE_HEIGHT) + BUFF, TILE_WIDTH - (2 * BUFF), TILE_HEIGHT - (2 * BUFF)),
		"seed": None,
		"time_planted": None
	}


pygame.init()

surface = pygame.display.set_mode((W, H))
tiles = [create_tile(i, j) for i in range(N) for j in range(N)]

current_seed = "Tomato"
seed_options = ["Tomato", "Blueberry", "Pumpkin"]
seed_options_index = seed_options.index(current_seed)

current_time = 0
fruit_collected = 0
p_size = 30
px = 320 - (p_size / 2)
py = 240 - (p_size / 2)
movement_speed = 50
death_time = 100000
earned_total = 0
p_level = 0
exp_total = 0
surface.fill("green")
font = pygame.font.SysFont("Times New Roman", 38)
lvl_display = font.render("Lvl: " + str(p_level), 1, "black")
exp_display = font.render("Exp: " + str(exp_total), 1, "black")
cash_display = font.render("$" + str(earned_total), 1, "black")
fruit_display = font.render(current_seed, 1, "black")
clock = pygame.time.Clock()
current_time = pygame.time.get_ticks()
player_rect = pygame.Rect(px, py, p_size, p_size)
for tile in tiles:
	pygame.draw.rect(surface, grass_color(tile, current_time), tile["rect"])
pygame.draw.rect(surface, PLAYER_COLOR, player_rect)
surface.blit(lvl_display, (5, 1))
surface.blit(exp_display, (5, 20))
surface.blit(cash_display, (5, 50))
surface.blit(fruit_display, (5, 80))
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
			elif event.key == pygame.K_e:
				seed_options_index += 1
				seed_options_index %= len(seed_options)
				current_seed = seed_options[seed_options_index]
			elif event.key == pygame.K_q:
				seed_options_index -= 1
				seed_options_index %= len(seed_options)
				current_seed = seed_options[seed_options_index]

			elif event.key == pygame.K_SPACE:	
				for tile in tiles:
					if not tile["seed"] and (tile["rect"].contains(player_rect)):
						tile["seed"] = current_seed
						tile["time_planted"] = pygame.time.get_ticks()
					elif tile["seed"] and (tile["rect"].contains(player_rect)) and not is_ready(tile, current_time):
						tile["seed"] = None
						tile["time_planted"] = None
					elif tile["seed"] and (tile["rect"].contains(player_rect)) and is_ready(tile, current_time):
						fruit_collected += 1
						earned_total += SEEDS[tile["seed"]]["price"]
						exp_total += SEEDS[tile["seed"]]["exp"]
						tile["seed"] = None
						tile["time_planted"] = None

	current_time = pygame.time.get_ticks()

	for tile in tiles:
		if tile["seed"] and current_time - tile["time_planted"] > death_time + SEEDS[tile["seed"]]["grow_time"]:
			tile["seed"] = "dead"
	if exp_total >= 20:
		p_level = 2
	if exp_total >= 50:
		p_level = 3

	surface.fill("green")
	for tile in tiles:
		pygame.draw.rect(surface, grass_color(tile, current_time), tile["rect"])
	pygame.draw.rect(surface, PLAYER_COLOR, player_rect)
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
