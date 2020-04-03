import settings
import random

st = settings.Settings()

class Bar():
	def __init__(self, x, y, window_obj = None):
		self.x = x
		self.y = y
		self.window_obj = window_obj