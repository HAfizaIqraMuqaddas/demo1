import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Connect to database
conn = sqlite3.connect('customers.db')

cur = conn.cursor()
cur.execute("SELECT * FROM customers LIMIT 5;")
print(cur.fetchall())




# Step 2: Load data into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM customers", conn)
print(df.head())

# Step 3: Select features for clustering
X = df[['Annual_Income', 'Spending_Score']]

# Step 4: Apply Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Step 5: Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
