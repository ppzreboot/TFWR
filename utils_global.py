import ppz

def move_next():
	move(East)
	if (get_pos_x() == 0):
		move(North)	

# 有优化空间
def move_to(pos):
	while get_pos_x() < pos[0]:
		move(East)
	while get_pos_x() > pos[0]:
		move(West)
	while get_pos_y() < pos[1]:
		move(North)
	while get_pos_y() > pos[1]:
		move(South)

def one_round(job):
	for _ in (get_world_size() ** 2):
		job()
		move(East)
		if (get_pos_x() == 0):
			move(North)

def right_top__2__left_bottom(left_bottom, right_top):
	current = None
	def back():
		move(West)
		while (get_pos_y() < right_top[1]) and (get_pos_x() > left_bottom[0]):
			move(North)
			move(West)
	def _():
		global current
		if current == None:
			move_to(right_top)
			current = right_top
			return True
		if (current == left_bottom):
			return False
		if current[0] == right_top[0]:
			back()
		elif current[1] == left_bottom[1]:
			back()
		else:
			move(East)
			move(South)
		current = ppz.pos()
		return True

	return _

def right_top__2__origin(right_top):
	return right_top__2__left_bottom((0, 0), right_top)
