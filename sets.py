import settings
import bar
import random
import math
import functions as f

st = settings.Settings()

class Set():
	def __init__(self, number = st.number, dist = st.dist, window = None):
		self.number = number
		self.window = window
		self.set = []
		if window != None:
			if dist == "triangle":
				for i in range(self.number):
					x = f.get_x(i, st.bar_w)
					y = f.get_y(i, st.step_h)
					self.set.append(bar.Bar(x, y, window_obj = window.create_rectangle(int(x), 
						int(st.window_h), int(x + st.bar_w), int(st.window_h - y), fill = st.idle_c)))

	def find_max(self, maxindex, index = True):
		temp = self.set[0].y
		temp_i = 0
		for i in range(maxindex + 1):
			if self.set[i].y >= temp:
				temp = self.set[i].y
				temp_i = i
		if index:
			return temp_i
		else:
			return temp

	def compare(self, m, n, inc = True):
		if self.set[m].y > self.set[n].y:
			return True
		else:
			return False

	def swap(self, n, m):
		self.window.move(self.set[n].window_obj, f.delta_x(m, n, st.bar_w), 0)
		self.window.move(self.set[m].window_obj, f.delta_x(n, m, st.bar_w), 0)
		self.set[n], self.set[m] = self.set[m], self.set[n]
		#self.set[n].window_obj, self.set[m].window_obj = self.set[m].window_obj, self.set[n].window_obj

	def insert(self, n, b):
		for i in range(n, b):
			self.swap(i, b)

	def color(self, n, color):
		self.window.itemconfig(self.set[n].window_obj, fill = color)

	def scramble(self):
		for i in range(self.number):
			n = random.randint(i, self.number - 1)
			self.swap(n, i)
			self.color(i, st.idle_c)
			self.window.update()

	def bubble_sort(self):
		for i in range(self.number - 1, -1, -1):
			for j in range(i):
				if self.compare(j, j + 1):
					self.swap(j, j + 1)
					self.window.update()
			#self.color(i, st.sorted_c)

	def selection_sort(self):
		for i in range(self.number - 1, -1, -1):
			self.swap(self.find_max(maxindex = i), i)
			#self.color(i, st.sorted_c)
			self.window.update()

	def insertion_sort(self):
		for i in range(1, self.number):
			j = 0
			while j < i:
				if self.compare(j, i):
					self.insert(j, i)
					self.window.update()
					j = i
				j += 1

	def shell_sort(self):
		i = st.shell_i
		while i >= 1:
			for j in range(i, self.number):
				for k in range(j, i - 1, -i):
					if self.compare(k - i, k):
						self.swap(k, k - i)
						self.window.update()
			i = i // 2






