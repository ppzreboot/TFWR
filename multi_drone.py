import ppz
import MOVE

# 每行派一个无人机（仅用于 WS == MD，无人机在 (0, 0) 的情况）
def one_line_one_drone(unit_job):
	WS = get_world_size()
	MD = max_drones()
	MD_HALF = MD / 2
	if MD != WS or ppz.pos() != (0, 0):
		ppz.throw()

	def one_line(y):
		def _():
			MOVE.to_y(y)
			for _ in range(WS):
				unit_job()
				move(East)
		return _
	worker_list = []

	worker_list.append(spawn_drone(one_line(MD_HALF)))
	for y in range(1, MD_HALF): # [1, MD_HALF - 1]
		worker_list.append(spawn_drone(one_line(MD_HALF - y)))
		worker_list.append(spawn_drone(one_line(MD_HALF + y)))
	one_line(0)()
	wait(worker_list)

def wait(list):
	for worker in list:
		wait_for(worker)

def drone_factory(job):
	worker_list = []
	def new():
		while True:
			worker = spawn_drone(job)
			if worker != None:
				worker_list.append(worker)
				return worker
	def wait_all():
		while len(worker_list):
			wait_for(worker_list.pop(0))

	return new, wait_all
