import matplotlib.pyplot as plt
import numpy as np

#table data lighter
data_Table_61_a = np.array([0.27, 0.412, 0.544, 0.712, 0.801, 0.942, 1.012])
data_Table_61_T = np.array([13.4, 20.7, 27.8, 34.6, 41.5, 48.0, 52.9])
#table data heavier
data_Table_62_a = np.array([0.002, 0.028, 0.125, 0.245, 0.321, 0.454, 0.545])
data_Table_62_T = np.array([13.7, 21.5, 29.1, 36.4, 43.7, 50.6, 55.6])

#Linear aproximation
b,a = np.polyfit(data_Table_61_a,data_Table_61_T, 1)
c,d = np.polyfit(data_Table_62_a,data_Table_62_T, 1)

plt.figure(figsize=(8, 5))

#graphics
plt.scatter(data_Table_61_a, data_Table_61_T, label = 'обычная тележка', )
plt.scatter(data_Table_62_a, data_Table_62_T, label = 'утяжеленная тележка')
plt.plot(data_Table_61_a, b * data_Table_61_a + a, label = f'линейная апроксимация: обычная тележка (M ≈ {b:.1f} г)')
plt.plot(data_Table_62_a, c * data_Table_62_a + d, label = f'линейная апроксимация: утяжеленная тележка (M ≈ {d:.1f} г)')


#titles
plt.title("Зависимость силы натяжения нити от ускорения тележки")
plt.xlabel("ускорение(а,м/c^2)")
plt.ylabel("сила натяжения (Т, мН)")
plt.legend()

plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.show()