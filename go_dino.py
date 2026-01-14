import ppz
import MOVE

def go():
	prepare()
	while True:
		circle()

def prepare():
	set_world_size(6)
	slow_till()
	change_hat(Hats.Dinosaur_Hat)

def slow_till():
	count = get_world_size() ** 2
	for _ in range(count):
		till()
		MOVE.next()

def circle():
	WS = get_world_size()
	MOVE.y(WS - 1) # 左上角

	while get_pos_x() != WS - 2:
		move(East)
		MOVE.y(2 - WS)
		move(East)
		MOVE.y(WS - 2)

	move(East) # 右上角
	MOVE.y(1 - WS) # 右下角
	MOVE.x(1 - WS) # 回到原点

def danger_go(destination):
	px, py = ppz.pos()
	dx, dy = destination
	MOVE.x(dx - px)
	MOVE.y(dy - py)
