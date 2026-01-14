import ppz
import MOVE

# 每行派一个无人机（仅用于 WS == MD 的情况）
def one_line_one_drone(unit_job):
	WS = get_world_size()
	MD = max_drones()

	def one_line(y):
		def _():
			MOVE.to_y(y)
			for _ in range(WS):
				unit_job()
				move(East)
		return _
	if MD != WS:
		ppz.throw()
	worker_list = []
	for y in range(MD - 1):
		worker_list.append(spawn_drone(one_line(y)))
	one_line(MD - 1)()
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
