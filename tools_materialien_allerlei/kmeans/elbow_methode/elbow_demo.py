# You can learn about the Matplotlib module in our "Matplotlib Tutorial: https://www.w3schools.com/python/matplotlib_intro.asp
# scikit-learn is a popular library for machine learning.

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Create arrays that resemble two variables in a dataset. Note that while we
# only use two variables here, this method will work with any number of variables:
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Plot the data points
plt.scatter(x, y)
plt.show()

# Turn the data into a set of points:
data = list(zip(x, y))

# In order to find the best value for K, we need to run K-means across our data for
# a range of possible values. We only have 10 data points, so the maximum number
# of clusters is 10. So for each value K in range(1,11), we train a K-means model
# and plot the intertia at that number of clusters:
inertias = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow Methode')
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Trägheit')
plt.savefig('kmeans_elbow_demo.svg')
plt.show()

# We can see that the "elbow" on the graph above (where the interia becomes more linear)
# is at K=2. We can then fit our K-means algorithm one more time and # plot the different
# clusters assigned to the data:
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()