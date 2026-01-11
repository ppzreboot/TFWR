import utils

def carrot():
	clear()
	def till_and_plant():
		till()
		plant(Entities.Carrot)
	utils.one_round(till_and_plant)
	while True:
		harvest_and_plant(Entities.Carrot)

def basic2():
	clear()
	while True:
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		utils.slow_move_next()

def harvest_and_plant(product):
	harvest()
	plant(product)
	utils.slow_move_next()
