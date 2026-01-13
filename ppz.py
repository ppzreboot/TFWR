def throw(err_msg):
	quick_print(err_msg)
	call_not_defined()

def till_and_plant(entity):
	def _tp():
		if get_ground_type() != Grounds.Soil:
			till()
		plant(entity)
	return _tp

def pos():
	return (get_pos_x(), get_pos_y())
