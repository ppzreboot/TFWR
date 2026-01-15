import ppz
import MOVE

def go():
	prepare()
	while True:
		circle()

def prepare():
	clear()
	# set_world_size(6)
	slow_till()
	change_hat(Hats.Dinosaur_Hat)

def slow_till():
	count = get_world_size() ** 2
	for _ in range(count):
		till()
		MOVE.next()

def circle():
	def next(orientation):
		if move(orientation) == False:
			change_hat(Hats.Green_Hat) # 大丰收
			change_hat(Hats.Dinosaur_Hat) # 新一轮
			move(orientation)
	WS = get_world_size()
	while get_pos_y() != WS - 1: # 左上角
		next(North)

	while get_pos_x() != WS - 2:
		next(East)
		while get_pos_y() > 1:
			next(South)
		next(East)
		while get_pos_y() < WS - 1:
			next(North)

	next(East) # 右上角
	while get_pos_y() > 0: # 右下角
		next(South)
	while get_pos_x() > 0: # 回到原点
		next(West)

def danger_go(destination):
	px, py = ppz.pos()
	dx, dy = destination
	MOVE.x(dx - px)
	MOVE.y(dy - py)
