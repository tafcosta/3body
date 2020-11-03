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
x   = 0.7
y   = 0.5
vx  = -2. #0.
vy  =  2.2 #np.sqrt(G_int * Mbh / 0.2) 


time     = 0.
time_max = 5
dt       = 1.e-5

x    -= xbh
y    -= ybh
rad2  = x**2 + y**2
acc_x = - G_int * Mbh / rad2 * x / np.sqrt(rad2)
acc_y = - G_int * Mbh / rad2 * y / np.sqrt(rad2)

nsteps   = int((time_max - time)/dt)
fac_red  = 100
xpath    = np.zeros(int(nsteps/fac_red)+1)
ypath    = np.zeros(int(nsteps/fac_red)+1)


xx = x + vx * dt + 0.5 * dt**2 * acc_x
yy = y + vy * dt + 0.5 * dt**2 * acc_y

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
    

plt.tick_params(axis='both', which='both', direction='in', top='on', right='on', width=1.3, labelsize=
16)
plt.minorticks_on()

plt.plot(xpath,ypath,color='orchid',linestyle='--')
plt.scatter([0],[0],marker='+', color ='black')
plt.axes().set_aspect('equal', 'datalim')
plt.xlim(-0.5,0.5)
plt.ylim(-0.5,0.5)
plt.show()
