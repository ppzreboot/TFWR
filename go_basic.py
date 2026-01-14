import utils_global
import utils_cocktail

def worker_hay(row):
	def _work():
		utils_global.move_to((0, row))
		while True:
			harvest()
			move(East)
	return _work

def worker_wood(y1):
	def all_tree():
		for _ in range(get_world_size()):
			while not can_harvest():
				print("waiting!!!")
			harvest()
			plant(Entities.Tree)
			move(East)
	def all_weird():
		for _ in range(get_world_size()):
			while not can_harvest():
				print("waiting!!!")
			harvest()
			plant(Entities.Tree)
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
				use_item(Items.Weird_Substance)
			move(East)

	def plain_wood():
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 1:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)

	def one_round():
		all_tree() # 第一行树
		move(North)
		move(North)
		all_tree() # 第三行输
		move(South)
		all_weird() # 第二行 Weird_Substance

		move(North)
		move(North)
		move(North)

		for _ in range(20):
			utils_cocktail.one_round(y1 + 4, y1 + 8, plain_wood)


	def _work():
		while True:
			round_start = get_time()
			utils_global.move_to((0, y1))
			one_round()
			quick_print('tree round', get_time() - round_start)
	return _work

def worker_carrot(y1, y2):
	def till_and_plant():
		till()
		plant(Entities.Carrot)
	def harvest_and_plant():
		harvest()
		plant(Entities.Carrot)
	def _work():
		utils_global.move_to((0, y1))
		utils_cocktail.one_round(y1, y2, till_and_plant)
		while True:
			utils_cocktail.one_round(y1, y2, harvest_and_plant)
	return _work

def worker_sunflower(y1, y2):
	def till_and_plant():
		till()
		plant(Entities.Sunflower)
	def harvest_and_plant():
		harvest()
		plant(Entities.Sunflower)
	def _work():
		utils_global.move_to((0, y1))
		utils_cocktail.one_round(y1, y2, till_and_plant)
		while True:
			utils_cocktail.one_round(y1, y2, harvest_and_plant)
	return _work

def go():
	clear()

	spawn_drone(worker_hay(0))
	spawn_drone(worker_hay(1))

	spawn_drone(worker_wood(3))

	spawn_drone(worker_carrot(20, 23))
	spawn_drone(worker_carrot(24, 27))
	spawn_drone(worker_carrot(28, 31))

	spawn_drone(worker_sunflower(12, 14))
	worker_sunflower(15, 17)()

def hay():
	def worker(y):
		def _():
			while get_pos_y() != y:
				move(North)
			while True:
				harvest()
				move(East)
		return _

	# 作准备
	clear()
	MD = max_drones()
	for y in range(MD - 1):
		spawn_drone(worker(y))
	spawn_drone(worker(MD))

def wood():
	def worker(y):
		def _():
			while get_pos_y() != y:
				move(North)
			
			while True:
				harvest()
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				while get_water() < .7:
					use_item(Items.Water)
				move(East)
		return _

	# 作准备
	clear()
	MD = max_drones()
	for y in range(MD - 1):
		spawn_drone(worker(y))
	worker(MD - 1)()
