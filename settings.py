import functions as f

class Settings():
	def __init__(self):
		#General settings
		self.number = 300
		self.window_h = 650
		self.window_w = 1200
		#Visual settings
		self.idle_c = "yellow"
		self.sort_c = "red"
		self.sorted_c = "blue"
		self.background_c = "snow2"
		#Distribution settings
		self.bar_w = self.window_w / self.number
		self.step_h = self.window_h / self.number
		self.dist = "triangle"
		self.view = "linear"
		#Sorts settings
		self.shell_i = f.get_2n(self.number)