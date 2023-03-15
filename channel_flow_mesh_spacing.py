import numpy as np
import matplotlib.pyplot as plt

def get_y_coords(num_cells_y,stretching_type=1):
  npoints = num_cells_y+1
  y = np.zeros(npoints)

  if(stretching_type==0):
    # High-order predicition workshop 5
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
  elif(stretching_type==1):
    # Gullbrand, Grid-independent large-eddy simulation in turbulent channel flow using three-dimensional explicit filtering, 2003
    gam = 2.75
    # npts_wall_normal = np.int64(npoints/2)+1

    # for j in range(0,np.int64(npoints/2)):
    for j in range(0,npoints):
      y[j] = -np.tanh(gam*(1.0-2.0*np.float64(j)/np.float64(num_cells_y)))/np.tanh(gam)
      # y[npoints] = 
      # y[-(j+1)] = 1.0 - y[j]
    y[:] += 1.0
    y[:] *= 0.5
  else:
    print("ERROR: Invalid stretching_type. Aborting...")
    exit()

  print("Coordinates")
  print(y)
  print(" ")
  print("Element sizes:")
  print(np.diff(y))
  print(" ")
  return y

num_cells_y = 16
y0 = get_y_coords(num_cells_y,stretching_type=0)
y1 = get_y_coords(num_cells_y,stretching_type=1)
plt.plot(y0, np.ones(num_cells_y+1),'ro')
plt.plot(y1, 2.0*np.ones(num_cells_y+1),'bo')
plt.show()