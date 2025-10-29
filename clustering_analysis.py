import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

# read an Excel file, the real path on PC is hidden
df = pd.read_excel('D:/.../6genes.xlsx', index_col=0)

# calculate Euclidean distance
distance_matrix = pdist(df.values, metric='euclidean')

# Construct a DataFrame of the distance matrix for easy viewing.
distance_df = pd.DataFrame(distance_matrix, index=df.index, columns=df.index)
# write the distance matrix to excel file
distance_df.to_excel('gene_euclidean_distance_matrix.xlsx')

# hierarchical clustering using average linkage
Z = linkage(distance_matrix, method='average')

# draw a clustering dendrogram
plt.figure(figsize=(12, 6))
dendrogram(
    Z,
    labels=df.index,           # gene probe as lable
    leaf_rotation=90,          # angle of lable rotation
    leaf_font_size=10,
)
plt.title('Hierarchical Clustering Dendrogram (Average Linkage, Euclidean Distance)')
plt.xlabel('Gene Probe ID')
plt.ylabel('Distance')
plt.tight_layout()
plt.show()