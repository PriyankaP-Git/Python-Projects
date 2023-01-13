import matplotlib.pyplot as plt

import numpy as np

x= np.arange(0,10,1)
print(x)

y= np.arange(0,10,1)
print(y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("X vs Y")
plt.plot(x,y)
plt.show()



