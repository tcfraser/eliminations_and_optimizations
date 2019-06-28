import numpy as np

def f(x,y):
    clamp = (1-x**2)*(1-y**2)
    ang   = np.pi/8
    xr,yr = np.cos(ang) * x - np.sin(ang) * y, np.sin(ang) * x + np.cos(ang) * y
    waves = np.sin(np.pi*xr)*np.sin(np.pi*yr)
    bump  = np.exp( - 0.2*( (xr-0.5)**2 + 2*(yr-0.5)**2 ) )
    return clamp*bump*waves

samples_length = 31
surface_data = np.zeros((samples_length, samples_length, 3))
optimal_data = np.zeros((samples_length,5))

delta = 2/(samples_length-1)
input_vals = np.arange(-1,+1+delta,delta)

for i in range(samples_length):
    for j in range(samples_length):
        surface_data[i,j,:] = [input_vals[i],input_vals[j],f(input_vals[i],input_vals[j])]

for i in range(samples_length):
    optimal_data[i,0] = input_vals[i]
    optimal_data[i,1] = np.max(surface_data[i,:,2])
    optimal_data[i,2] = np.min(surface_data[i,:,2])
    optimal_data[i,3] = np.max(surface_data[:,i,2])
    optimal_data[i,4] = np.min(surface_data[:,i,2])

np.savetxt("surf.csv", np.reshape(surface_data, (samples_length**2, 3)), delimiter=' ')
np.savetxt("opt.csv", optimal_data, delimiter=' ', header='x maxA minA maxB minB', comments='')


