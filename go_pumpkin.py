import utils

def go():
	while True:
		clear()
		first_season()

def first_season():
	def till_and_plant():
		till()
		plant(Entities.Pumpkin)
	def first_check_dead():
		# 第一遍时，不可能没熟：只可能“正常熟”或“枯萎”
		if get_status() == -1:
			plant(Entities.Pumpkin)
			dead_list.append((get_pos_x(), get_pos_y()))

	def check_dead(pos):
		utils.slow_move(pos)
		while get_status() == 0:
			change_hat(Hats.Brown_Hat)
			quick_print("wait for recheck (200 tick)")
		if get_status() == 1:
			return pos
		else:
			plant(Entities.Pumpkin)

	dead_list = []
	# step 1: round(till and first plant)
	utils.one_round(till_and_plant)
	# step 2: round(first_check_dead and replant)
	utils.one_round(first_check_dead)
	quick_print("first round, dead_list length: ", len(dead_list))
	# step 3: loop(recheck_dead)
	while len(dead_list) > 0:
		good_list = []
		for d in dead_list:
			maybe_good = check_dead(d)
			if maybe_good != None:
				good_list.append(maybe_good)
		quick_print("good_list length", len(good_list))
		for good in good_list:
			dead_list.remove(good)
		quick_print("dead_list length", len(dead_list))
	# step 4: 大丰收
	harvest()

def one_season():
	pass

def get_status():
	ch = can_harvest()
	if ch:
		return 1 # 成熟的南瓜
	if get_entity_type() == Entities.Dead_Pumpkin:
		return -1 # 死亡的南瓜
	return 0 # 未成熟的南瓜
