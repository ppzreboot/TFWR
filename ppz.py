def throw(err_msg):
	quick_print(err_msg)
	call_not_defined()

def till_and_plant__f(entity):
	def _tp():
		till()
		plant(entity)
	return _tp
def plant__f(entity):
	def _():
		plant(entity)
	return _

def pos():
	return (get_pos_x(), get_pos_y())
