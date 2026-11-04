#Задача 5.1
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,5), dpi=100)
x = [9815.56, 14234.38, 18957.98, 23482.76, 26767,6, 0]
y = [19064.71, 24964, 36141.81, 42906.98, 49257.36, 0]
plt.plot(x[:6],y[:6],'o',  label='u^2(T)', marker='.', markersize=10, markeredgecolor='blue')
plt.grid()
plt.legend()
plt.savefig('mygraph.png', dpi=300)
plt.show()
#Задача 5.2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
mean, std = 0, 1
sample_sizes = [100, 500000]
colors = ['red', 'pink']
fig, axes = plt.subplots(1, 2, figsize=(8, 5))
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, mean, std)

for idx, size in enumerate(sample_sizes):
    data = np.random.normal(mean, std, size)
    n, bins, patches = axes[idx].hist(data, bins=30, density=True, color=colors[idx], alpha=0.7, label=f'N = {size}')
    axes[idx].plot(x, pdf, 'k-', linewidth=2, label='Теоретическая кривая')
    
    axes[idx].set_title(f'Гистограмма (N = {size})')
    axes[idx].set_xlabel('Значение')
    axes[idx].set_ylabel('Плотность')
    axes[idx].legend()

plt.tight_layout()
plt.show()
