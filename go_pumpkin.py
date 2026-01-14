import utils_global
import utils_cocktail
import multi_drone
import ppz

def go():
	def one_drone(id):
		def check_dead():
			def unit():
				while get_status() == 0:
					pass
				s = get_status()
				if s == -1:
					plant(Entities.Pumpkin)
					dead_list.append((ppz.pos(), True))
			utils_cocktail.one_round(y1, y2, unit)
		def recheck():
			for i in range(len(dead_list)):
				target_pos, target_dead = dead_list[i]
				if (not target_dead): # 上几轮中被修复
					continue
				utils_global.move_to(target_pos)
				while get_status() == 0:
					pass
				s = get_status()
				if s == 1:
					dead_list[i] = (target_pos, False)
				else:
					while get_water() < 0.5:
						use_item(Items.water)
					plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
		def has_dead():
			for _, target_dead in dead_list:
				if target_dead:
					return True
			return False
		def job():
			utils_global.move_to((0, y1))
			check_dead()
			while has_dead():
				recheck()

		y1 = id * lines_per_drone
		y2 = y1 + lines_per_drone - 1
		dead_list = []
		return job

	def plant_pumpkin():
		plant(Entities.Pumpkin)

	clear()
	WS = get_world_size()
	MD = max_drones()
	lines_per_drone = WS / MD

	# 第一遍 till 和 plant
	multi_drone.one_round(MD, WS, ppz.till_and_plant(Entities.Pumpkin))
	quick_back()
	while True:
		performance_start = get_time()
		# 多无人机修复
		multi_drone.special_job(MD, one_drone)
		# 大丰收！
		harvest()
		quick_back()
		# 下一轮种植
		multi_drone.one_round(MD, WS, plant_pumpkin)
		quick_back()

		quick_print("一轮总用时", get_time() - performance_start)

def quick_back():
	move(East)
	move(North)

def get_status():
	ch = can_harvest()
	if ch:
		return 1 # 成熟的南瓜
	if get_entity_type() == Entities.Dead_Pumpkin:
		return -1 # 死亡的南瓜
	return 0 # 未成熟的南瓜
