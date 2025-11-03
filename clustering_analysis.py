import pandas as pd
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

# read an Excel file, the real path on PC is hidden
df = pd.read_excel("D:/.../6genes.xlsx", index_col=0)
df_zscore = (df - df.mean()) / df.std()

# calculate Euclidean distance
dist_condensed = pdist(df.values, metric='euclidean')

# Construct a DataFrame of the distance matrix for easy viewing.
dist_square = squareform(dist_condensed)
distance_df = pd.DataFrame(dist_square, index=df.index, columns=df.index)

# write the distance matrix to an Excel file
distance_df.to_excel('gene_euclidean_distance_matrix.xlsx')

# hierarchical clustering using average linkage
cm = sns.clustermap(df_zscore.T, figsize=(10, 8),
               row_cluster=True, col_cluster=True, yticklabels=False)
cm.ax_heatmap.set_xticklabels(cm.ax_heatmap.get_xticklabels(), fontsize=8)

plt.show()
