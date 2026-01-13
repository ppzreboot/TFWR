import utils_cocktail
import utils_global

def one_round(drone_num, WS, unit_job):
	lines_per_drone = WS / drone_num
	def job(did):
		y1 = did * lines_per_drone
		y2 = y1 + lines_per_drone - 1
		utils_global.move_to((0, y1))
		def _():
			utils_cocktail.one_round(y1, y2, unit_job)
		return _

	special_job(drone_num, job)

def special_job(drone_num, job_factory):
	worker_list = []
	for id in range(drone_num - 1):
		d = spawn_drone(job_factory(id))
		worker_list.append(d)
	job_factory(drone_num - 1)()

	for d in worker_list:
		wait_for(d)
