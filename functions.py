def get_x(n, width):
	return n * width

def get_y(n, step):
	return n * step

def delta_x(n, m, width):
	return (n - m) * width

def get_2n(number):
	deg = 0
	while 2**deg < number:
		deg += 1
	return 2**(deg - 1)
