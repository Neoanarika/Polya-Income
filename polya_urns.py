import numpy as np 
import matplotlib.pyplot as plt
from tqdm import tqdm
from gini import *
net_worths = []
chart = []
for i in tqdm(range(1000)):
	chart = []
	x = 10
	urn = list(np.random.randint(2,size = x))
	net_worth = 1000
	for _ in range(20000):
		choose = np.random.randint(x)
		urn.append(urn[choose])
		if urn[choose] == 1: net_worth += 1
		else: net_worth -= 1
		chart.append(net_worth)
		x+=1
	net_worths.append(net_worth)
#plt.plot(charts[0])
#plt.show()
print(net_worths)
n, bins, patches = plt.hist(net_worths, 50)

plt.grid(True)
plt.show()
print(gini(np.array(net_worths).astype(np.float32)))
