import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("unit_converted_stars.csv") 

from sklearn.cluster import KMeans
import pandas as pd

X = df.iloc[:,[3,4]].values 

wcss= [ ] 
for i in range(1, 21): 
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42) 
  kmeans.fit(X) 

  wcss.append(kmeans.inertia_)

plt.plot(range(1,21),wcss)
plt.title("The Elbow Method")
plt.xlabel('Number of Clusters')
plt.show()

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
prediction = kmeans.fit_predict(X)

plt.figure(figsize = (10, 5))
sns.scatterplot(x = X[prediction == 0, 0], y = X[prediction == 0, 1], color = 'orange', label = 'Star Cluster 1')
sns.scatterplot(x = X[prediction == 1, 0], y = X[prediction == 1, 1], color = 'blue', label = 'Star Cluster 2')
sns.scatterplot(x = X[prediction == 2, 0], y = X[prediction == 2, 1], color = 'green', label = 'Star Cluster 3')
sns.scatterplot(x = kmeans.cluster_centers_[:, 0], y = kmeans.cluster_centers_[:, 1], color = 'red', label = 'Centroids', s = 100, marker = ',')

plt.title('Clusters of Stars')
plt.xlabel('Mass of Stars')
plt.ylabel('Radius of Stars')
plt.legend()
plt.title("STAR MASS AND RADIUS")
plt.show()
plt.figure()
