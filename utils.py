def slow_move_next():
	move(East)
	if (get_pos_x() == 0):
		move(North)

def slow_move(pos_to):
	while get_pos_x() < pos_to[0]:
		move(East)
	while get_pos_x() > pos_to[0]:
		move(West)
	while get_pos_y() < pos_to[1]:
		move(North)
	while get_pos_y() > pos_to[1]:
		move(South)

def move_to_origin():
	slow_move((0, 0))

def one_round(job):
	i = 0
	sum = get_world_size() ** 2
	while i < sum:
		job()
		slow_move_next()
		i += 1

def one_round__map(job):
	list = []
	i = 0
	sum = get_world_size() ** 2
	while i < sum:
		list.append(job())
		slow_move_next()
		i += 1
	return list
