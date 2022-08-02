import numpy as np
import matplotlib.pyplot as plt
import math

a_0 = ((math.exp(2*math.pi)-1)/(math.pi))
a_n = []
b_n = []
resolution = 100000

for n in range(resolution):
    a_x = ((math.exp(2*math.pi))-1)/((math.pi*((n+1)**2))+math.pi)
    a_n.append(a_x)
    b_x = ((n+1)-((n+1)*math.exp(2*math.pi)))/((math.pi*((n+1)**2))+math.pi)
    b_n.append(b_x)

w_t = np.arange(0,(4*math.pi),(math.pi/10000));

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12,5))
ax.set_xlabel('wt')
ax.set_ylabel('f(wt)')
ax.set_title("Fourier Series of exp^(wt)")

n = 0
f_x = a_0/2
for n in range(resolution):
    f_x = f_x + a_n[n]*np.cos((n+1)*w_t)
    f_x = f_x + b_n[n]*np.sin((n+1)*w_t)
    if (n == 0 or n == 3 or n == 6 or n == 99999):
        ax.plot(w_t, f_x, label=(n+1))
        
ax.legend();
        