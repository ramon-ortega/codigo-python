#Importing Numpy, matplotlib and sklear libraries

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")

#Que tipo de machine learning usaremos

from sklearn.cluster import KMeans

#Preprocesamiento
x=[1,5,1.5,8,1.9]
y=[2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show()

#Like we did before, covertir nuestra data to a numpy array
#X=np.array([1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11])
#Initialize the k menas algorithm

#kmenas=KMeans(n_clusters=2)
#kmeans.fit(X)

#Getting the values of centroids and labels based on the fitment
#centroids=kmeans.cluster_centers_
#labels = kmeans.labels

#print(centroids,type(centroids))
#print(labels,type(labels))

#Plotting and visualization of output

#colors=["g.","r.","c.","y."]

#for i in range(len(X)):
#	print('coordinate:' X[i], 'label: ', labels[i])
#	plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

#plt.scatter(centroids[:,0], centroids[:,1], marker ="x", s=150, widths=5, zorder=10)

#plt.show()
