def throw(err_msg):
	quick_print(err_msg)
	call_not_defined()

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
