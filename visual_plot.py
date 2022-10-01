from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
pyplot.figure(figsize=(6, 4.5))
plt.style.use( 'seaborn-whitegrid') 
palette = pyplot.get_cmap('Set1')
#plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12}) 
 
x = [10, 20, 50, 100]
y_Supervised = [0.706, 0.779, 0.842, 0.885]
y_Self = [0.768, 0.846, 0.884, 0.9]
y_Semi = [0.762, 0.848, 0.875, 0.903]
y_ours = [0.791, 0.869, 0.895, 0.913]
 
plt.xlim(10, 100)  # 限定横轴的范围
plt.ylim(0.7, 0.92)  # 限定纵轴的范围
 
 
#plt.plot(x, y_Supervised, marker='o', mec='r',label='Supervised')
plt.plot(x, y_Supervised, color=palette(3), marker='*', label='Supervised')
plt.plot(x, y_Self, color=palette(1), marker='^', label='Self-supervised')
plt.plot(x, y_Semi, color=palette(2), marker='s', label='Semi-supervised')
plt.plot(x, y_ours, color=palette(0), marker='o', label='Ours')
 
plt.legend()  # 让图例生效
#plt.xticks(x, names, rotation=1)
 
plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.xlabel('Labeled Data Percentage') #X轴标签
plt.ylabel("AUC") #Y轴标签
pyplot.yticks([0.70, 0.75,0.80,0.85,0.90,0.92])
pyplot.xticks([10, 20, 50, 100])
#plt.title("A simple plot") #标题
plt.savefig('Fig.png',dpi = 300)
