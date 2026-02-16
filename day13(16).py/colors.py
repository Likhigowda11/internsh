import matplotlib.pyplot as plt
print(plt.colormaps())


plt.figure()
sns.heatmap(corr_matrix,annot=True,cmap="berlin_r")
plt.title("Correlation Heatmap")
plt.show()