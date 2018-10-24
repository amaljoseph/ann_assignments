from random import uniform
def activation_fn(x):
	if x>0:
		return x
	return 0

# step 1 - initialize weights and activations
activations = [0.3, 0.5, 0.7, 0.9]
m = len(activations)
#k = uniform(0, 1/m)
k = 0.2	

a_old = activations.copy()
a_new = []
count = 0
while True: #step 2
	temp = sum(a_old)
	for i in range(0, m): # step 3 - update activations of each node
		value = a_old[i] - k * temp + k * a_old[i]
		a_new.append(activation_fn(value))
	a_old = a_new.copy() # step 4 - save activations for use in each iterations
	if sum(a_new) == max(a_new): # step 5 - test for stopping condition
		break
	a_new = []
	count += 1
	print('EPOCH {} - activations = {}'.format(count, a_old))
print ('The final activations are {}'.format(a_new))
