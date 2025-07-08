import numpy as np
import matplotlib.pyplot as plt

print("hello world")

x = np.random.randn(50)
y = np.random.randn(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot')
plt.show()
