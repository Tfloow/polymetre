#%%
import numpy as np
from matplotlib import pyplot as plt
pi = np.pi

x,y = np.meshgrid(np.linspace(-3,3,1000),np.linspace(-3,3,1000))
z = x + 1j*y

# La méthode de Heun
gain = np.abs(1+ z + z*z/2)

ax = plt.gca()
ax.axis('equal')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.title("Zone de stabilité de la méthode de Heun")
plt.xlim((-2.5,2.5))
plt.ylim((-2.5,2.5))
plt.xlabel(r"Re($h \lambda$)")
plt.ylabel(r"Im($h \lambda$)")
plt.contour(x,y,gain,np.linspace(0, 1, 11) ,colors='black', linewidths=0.5)
plt.contourf(x,y,gain,np.linspace(0, 1, 11) ,cmap='jet_r')
plt.colorbar()
plt.show()





# La méthode d'Adam-Basforth-Moulton d'ordre 2
b = 1+z+3/4*z**2
c = z**2 / 4
s1 = 1/2*(b-np.sqrt(b**2 - 4*c))
s2 = 1/2*(b+np.sqrt(b**2 - 4*c))
gain = np.maximum(np.abs(s1), np.abs(s2))

ax = plt.gca()
ax.axis('equal')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.title("Zone de stabilité de la méthode\n d'Adam-Basforth-Mouton d'ordre 2")
plt.xlim((-2.5,2.5))
plt.ylim((-2.5,2.5))
plt.xlabel(r"Re($h \lambda$)")
plt.ylabel(r"Im($h \lambda$)")
plt.contour(x,y,gain,np.linspace(0, 1, 11) ,colors='black', linewidths=0.5)
plt.contourf(x,y,gain,np.linspace(0, 1, 11) ,cmap='jet_r')
plt.colorbar()
plt.show()





# la méthode de Cranck-Nicolson
gain = np.abs((1+z/2)/(1-z/2))

ax = plt.gca()
ax.axis('equal')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.title("Zone de stabilité de la méthode de Cranck-Nicolson")
plt.xlim((-2.5,2.5))
plt.ylim((-2.5,2.5))
plt.xlabel(r"Re($h \lambda$)")
plt.ylabel(r"Im($h \lambda$)")
plt.contour(x,y,gain,np.linspace(0, 1, 11) ,colors='black', linewidths=0.5)
plt.contourf(x,y,gain,np.linspace(0, 1, 11) ,cmap='jet_r')
plt.colorbar()
plt.show()
