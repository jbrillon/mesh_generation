import numpy as np
import matplotlib.pyplot as plt

num_cells_y = 16
gam = 2.75

npoints = num_cells_y+1
y = np.zeros(npoints)

# for j in range(0,npoints):
#     y[j] = -np.tanh(gam*(1.0-2.0*np.float64(j-1))/np.float64(num_cells_y-1))/np.tanh(gam)
N = 1.0 # p+1 -- set to 1 in the code i got
r = 1.2**(N/2.0)
h0 = 0.5*(1.0-r)/(1.0-r**(num_cells_y/2.0));
h=0.;
for i in range(0,np.int64((num_cells_y-2)/2)):
  h += h0*r**np.float64(i);
  y[i+1] = h;
  y[num_cells_y-i-2+1] = 1.0-h;


y[np.int64(num_cells_y/2)-1+1] = 0.5;
y[num_cells_y-1+1] = 1.;

print(y)
print(np.diff(y))

plt.plot(y, np.ones(npoints),'ro')
plt.show()