import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100


x = np.linspace(0,1)

y1 = np.sin(x)
y2 = np.exp(-0.2*x)
y3 = np.arctan(x)
y4 = 2*x + 5
y5 = np.sqrt(x)
y6 = 6* np.ones_like(x)

y = np.vstack((y1,y2,y3,y4,y5,y6))
y.shape
fun_labels = ['sinus','exponentielle','arctangente','affine','racine','constant']

fig,axs = plt.subplots(nrows=2,ncols=3,sharex=True,sharey=False,figsize=(12,7))
for i in range(2):
    for j in range(3):
        axs[i,j].plot(x,y[i*3+j,:])
        axs[i,j].set_ylabel('y')
        axs[i,j].grid()
        axs[i,j].set_title(fun_labels[i*3+j])
        axs[i,j].set_xlabel('x')
fig.suptitle('Utilisation de subplots')
plt.savefig('subplots_demo.pdf')
plt.show()
