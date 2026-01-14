# y 方向上移动 abs(count) 个单位
# 正数 -> North; 负数 -> South
def y(count):
	if count > 0:
		orientation = North
	else:
		orientation = South
		count = abs(count)
	m(orientation, count)

# x 方向上移动 abs(count) 个单位
# 正数 -> East; 负数 -> West
def x(count):
	if count > 0:
		orientation = East
	else:
		orientation = West
		count = abs(count)
	m(orientation, count)

# 移动到 destination
def to_y(destination):
	WS = get_world_size()
	WS_HALF = WS / 2

	count = destination - get_pos_y()
	distance = abs(count)
	worm_hole = distance > WS_HALF
	if count > 0: # 目的地在北方
		if worm_hole:
			m(South, WS - distance)
		else:
			m(North, distance)
	else: # 目的地在南方
		if worm_hole:
			m(North, WS - distance)
		else:
			m(South, distance)

def to_x(destination):
	WS = get_world_size()
	WS_HALF = WS / 2

	count = destination - get_pos_x()
	distance = abs(count)
	worm_hole = distance > WS_HALF
	if count > 0: # 目的地在东方
		if worm_hole:
			m(West, WS - distance)
		else:
			m(East, distance)
	else: # 目的地在西方
		if worm_hole:
			m(East, WS - distance)
		else:
			m(West, distance)

# 向 orientaion，移动 count 次
def m(orientation, count):
	for _ in range(count):
		move(orientation)

# 移动到 destination
def go(destination):
	to_x(destination[0])
	to_y(destination[1])
