import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

x = np.linspace(-2,2,150)
y = np.linspace(-2,2,150)

X,Y = np.meshgrid(x,y)
x0, y0 = 1.0,-0.3
sigma = 0.4
Z = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-((X-x0)**2+(Y-y0)**2)/(2*sigma**2))

plt.figure(figsize=(6.2,5))
plt.contourf(X,Y,Z,cmap=plt.cm.jet)
plt.colorbar()
plt.contour(X,Y,Z,colors='gray')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('../images/colormap.pdf')
plt.show()