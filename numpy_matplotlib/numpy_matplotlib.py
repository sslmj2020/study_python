import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x),'r--o',x,np.sin(2*x),'g-*')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('sinx-o,sin2x-*')
#plt.scatter(x,np.sin(x))
#plt.scatter(x,np.sin(2*x))
plt.show()

