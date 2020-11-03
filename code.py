import numpy as np
import matplotlib.pylab as plt

G     = 6.673e-8
unitL = 3.09e21
unitV = 1.65e6
unitM = 1.989e43
unitT = unitL/unitV
G_int = G * (unitM * unitT**2 / unitL**3)

Mbh = 0.01
xbh = 0.5
ybh = 0.5

x  = 0.7
y  = 0.5
vx = -2. #0.
vy =  3. #np.sqrt(G_int * Mbh / 0.2) 


time     = 0.
time_max = 1.
dt       = 1.e-5

x    -= xbh
y    -= ybh
rad2  = x**2 + y**2
acc_x = - G_int * Mbh / rad2 * x / np.sqrt(rad2)
acc_y = - G_int * Mbh / rad2 * y / np.sqrt(rad2)

xx = x + vx * dt + 1./2 * dt**2 * acc_x
yy = y + vy * dt + 1./2 * dt**2 * acc_y

nsteps   = int(time_max/dt)
fac_red  = 100
xpath    = np.zeros(int(nsteps/fac_red)+1)
ypath    = np.zeros(int(nsteps/fac_red)+1)

for counter in np.arange(nsteps):
        
    if(counter % fac_red == 0):
            index = int(counter / fac_red)
            xpath[index] = xx
            ypath[index] = yy
    
    rad2  =   xx**2 + yy**2
    acc_x = - G_int * Mbh / rad2 * xx / np.sqrt(rad2)
    acc_y = - G_int * Mbh / rad2 * yy / np.sqrt(rad2)

    xtmp  = xx
    ytmp  = yy
    
    xx    = 2 * xx - x + dt**2 * acc_x
    yy    = 2 * yy - y + dt**2 * acc_y
    
    x     = xtmp
    y     = ytmp
    

plt.scatter(xpath,ypath)
plt.scatter([0],[0])
plt.show()
