def go():
	WS = get_world_size()
	weird_sub_num = WS * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	quick_print("消耗物质", weird_sub_num)

	while True:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, weird_sub_num)

		l = spawn_drone(GO("left"))
		r = spawn_drone(GO("right"))
		wait_for(l)
		wait_for(r)

def GO(type):
	LEFT = { East: North, North: West, West: South, South: East }
	RIGHT = { East: South, North: East, West: North, South: West }

	def _():	
		orientation = East
		if type == "left":
			first = LEFT
			third = RIGHT
		else:
			first = RIGHT
			third = LEFT
		while True:
			if measure() == None:
				break
			if get_entity_type() == Entities.Treasure:
				harvest()
				break
			if move(first[orientation]):
				orientation = first[orientation]
			elif move(orientation):
				pass
			else:
				move(third[orientation])
				orientation = third[orientation]
	return _