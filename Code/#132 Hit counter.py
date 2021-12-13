"""
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""
import time

#No podemos suponer que lleguen ordenados (Rito question here, el lag es rey)
#Linked list con timemarks, ya se mejorará eficiencia luego
#Supongo que se usa la biblioteca time, cuya unidad son los segundos

class TimestampList():
	def __init__(self):
		self.head = null
		self.length = 0
		self.timemarks = []


if __name__ == '__main__':
	for i in range(5):
		print(time.time())
		time.sleep(1)
