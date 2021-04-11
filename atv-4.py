import matplotlib.pyplot as plt
import numpy as np
import math

# -360 360
x = np.arange(math.radians(-360), math.radians(360),0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('x valores de -360º para 360º')
plt.ylabel('sin(x) e cos(x)')
plt.title('Gráfico de sin e cos de -360º to 360º')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()