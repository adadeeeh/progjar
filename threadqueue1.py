import Queue
import threading

q = Queue.Queue()

class ThreadInput(threading.Thread):
	start = input("start: ")
	end = input("end: ")
	for i in range(start, end+1):
		q.put(i)

class ThreadPrint(threading.Thread):
#	def run(self):
		while not q.empty():
			print q.get()

for i in range(2):
	t = ThreadInput()
	t.start()
