import time

end_time = time.time()+0.2
t_now = time.time()
while t_now<end_time:
	t_now = time.time()
	print("%.6f" % t_now)
print("end")