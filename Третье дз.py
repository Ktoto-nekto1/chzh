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
#Задача 5.3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
species_counts = df['Species'].value_counts()
ax1.pie(species_counts, labels = species_counts.index, autopct='%1.1f%%', startangle=90)
ax1.set_title('Распределение по видам ирисов')

petal_length = df['PetalLengthCm']

conditions = [
    petal_length<=1.2,
    (petal_length<=1.5) &(petal_length>1.2),
    petal_length>1.5
]

labels = ['<=1.2cm', '1.2cm-1.5cm', '>1.5cm']

petal_counts = pd.cut(petal_length, bins=[0, 1.2, 1.5, 100], labels=labels).value_counts()

ax2.pie(petal_counts, labels=petal_counts.index, autopct='%1.1f%%', startangle=90)

plt.tight_layout()
plt.show()
