def move_next(y1, y2):
	move(East)
	if get_pos_x() == 0:
		if get_pos_y() == y2:
			for _ in range(y2 - y1):
				move(South)
		else:
			move(North)

def one_round(y1, y2, job):
	count = get_world_size() * (y2 - y1 + 1)
	while count > 0:
		job()
		move_next(y1, y2)
		count -= 1
