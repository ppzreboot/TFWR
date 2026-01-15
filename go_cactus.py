import ppz
import multi_drone
import MOVE

WS = get_world_size()

def go():
	clear()
	# 全局种上 Cactus
	multi_drone.danger__one_line_one_drone(ppz.till_and_plant__f(Entities.Cactus))
	while True:
		sort()
		harvest()
		MOVE.go((0, 0))
		multi_drone.danger__one_line_one_drone(ppz.plant__f(Entities.Cactus))

def bubble_sort_row(y):
	MOVE.go((0, y)) # 归位
	for last in range(WS - 1):
		for _ in range(WS - last - 1):
			if measure() > measure(East):
				swap(East)
			move(East)
		MOVE.go((0, y)) # 归位
def bubble_sort_col(x):
	MOVE.go((x, 0)) # 归位
	for last in range(WS - 1):
		for _ in range(WS - last - 1):
			if measure() > measure(North):
				swap(North)
			move(North)
		MOVE.go((x, 0)) # 归位

def sort():
	MOVE.go((0, 0))

	sort_row = []
	handled = 0
	def ROW(y):
		def _():
			bubble_sort_row(y)
		return _
	while handled < WS:
		d = spawn_drone(ROW(handled))
		if d != None:
			sort_row.append(d)
		else:
			bubble_sort_row(handled)
		handled += 1
	multi_drone.wait(sort_row)

	MOVE.go((0, 0))
	sort_col = []
	handled = 0
	def COL(x):
		def _():
			bubble_sort_col(x)
		return _
	while handled < WS:
		d = spawn_drone(COL(handled))
		if d != None:
			sort_col.append(d)
		else:
			bubble_sort_col(handled)
		handled += 1
	multi_drone.wait(sort_col)
