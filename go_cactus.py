import utils_global
import ppz
import multi_drone

def go():
	clear()
	MD = max_drones()
	# set_world_size(8)
	WS = get_world_size()
	MAX_SIZE = WS - 1
	RIGHT_TOP = (MAX_SIZE, MAX_SIZE)

	while True:
		# 全局种上 Cactus
		multi_drone.one_round(MD, WS, ppz.till_and_plant(Entities.Cactus))
		# 移动遍历
		go = utils_global.right_top__2__origin(RIGHT_TOP)
		while(go()):
			sort_cactus(ppz.pos())
		harvest()

def sort_cactus(right_top):
	if right_top == (0, 0):
		return
	x, y = right_top
	if x == 0:
		bubble_sort_column((0, y), 0)
	elif y == 0:
		bubble_sort_row((0, x), 0)
	else:
		bubble_sort_square((0, 0), right_top)

def bubble_sort_row(x_range, y):
	x1, x2 = x_range
	utils_global.move_to((x1, y))
	for _ in range(x1, x2): # 正好不包含最后一个
		if measure() > measure(East):
			swap(East)
		move(East)
def bubble_sort_column(y_range, x):
	y1, y2 = y_range
	utils_global.move_to((x, y1))
	for _ in range(y1, y2):
		if measure() > measure(North):
			swap(North)
		move(North)

def bubble_sort_square(left_bottom, right_top):
	def sort_row_factory(y):
		def _():
			bubble_sort_row((x1, x2), y)
		return _

	x1, y1 = left_bottom
	x2, y2 = right_top

	# 按排冒泡（选出每排最大值）
	worker_list = []
	for y in range(y1, y2 + 1):
		while True:
			drone = spawn_drone(sort_row_factory(y))
			if drone == None:
				continue
			else:
				worker_list.append(drone)
				break
	for worker in worker_list:
		wait_for(worker)
	# 排最后一列（选出 square 里的最大值）
	bubble_sort_column((y1, y2), x2)
