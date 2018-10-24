import matplotlib.pyplot as plt
import corrections as crt
def activation_fn(x):
	if x<0:
		return 0
	elif x>2:
		return 2
	else:
		return x
# step1 - initialize parameteres and weights
r1 = 1
r2 = 2
c1 = 0.6
c2 = 0.4
signal = [0.0, 0.5, 0.8, 1.0, 0.8, 0.5, 0.0]
m = len(signal)
x = signal.copy() # step 2
t_max = 3

for t in range(0, t_max): #step 3 step 7 & 8
	x_old = x.copy() #step 6
	plt.plot(x_old)
	print ('t = {}'.format(t+1))
	for i in range(0, m):
		k, h, j, l = crt.corrections(i, r1, r2, m)
		sum1 = sum((x_old[k:j]))
		left = sum(x_old[h:k])
		right = sum((x_old[j:l]))
		sum2 = left + right
		x[i] = activation_fn(round((c1*sum1 - c2*sum2), 2)) # step 4 & 5
		print ('	x{} = {}'.format(i, x[i]))
plt.show()
