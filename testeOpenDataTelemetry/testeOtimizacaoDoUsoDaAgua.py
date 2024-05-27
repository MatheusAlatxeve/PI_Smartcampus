import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dados de exemplo de consumo de água (leituras do hidrômetro)
dados_consumo = {
    'Timestamp': [1621396800000, 1621483200000, 1621569600000, 1621656000000, 1621742400000,
                  1621828800000, 1621915200000, 1622001600000, 1622088000000, 1622174400000,
                  1622260800000, 1622347200000, 1622433600000, 1622520000000, 1622606400000],
    'Consumo': [100, 150, 130, 170, 160, 180, 190, 210, 200, 220, 300, 250, 240, 230, 1000]
}

# Criar DataFrame
df_consumo = pd.DataFrame(dados_consumo)

# Converter 'Timestamp' para datetime
df_consumo['Timestamp'] = pd.to_datetime(df_consumo['Timestamp'], unit='ms')

# Definir 'Timestamp' como índice
df_consumo.set_index('Timestamp', inplace=True)

# Exibir o DataFrame
print(df_consumo)

# Normalizar os dados de consumo
scaler = StandardScaler()
df_consumo['Consumo_normalizado'] = scaler.fit_transform(df_consumo[['Consumo']])

# Exibir os dados normalizados
print(df_consumo)

# Determinar o número ótimo de clusters usando o método do cotovelo
wcss = []  # Soma dos quadrados dentro do cluster

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(df_consumo[['Consumo_normalizado']])
    wcss.append(kmeans.inertia_)

# Plotar o gráfico do cotovelo
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Método do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# Aplicar K-means com o número ótimo de clusters (por exemplo, 3)
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=42)
df_consumo['Cluster'] = kmeans.fit_predict(df_consumo[['Consumo_normalizado']])

# Exibir os clusters
print(df_consumo)

# Plotar os clusters
plt.figure(figsize=(10, 6))
colors = ['r', 'g', 'b']
for i in range(3):  # Assumindo 3 clusters
    cluster_data = df_consumo[df_consumo['Cluster'] == i]
    plt.scatter(cluster_data.index, cluster_data['Consumo'], c=colors[i], label=f'Cluster {i}')

plt.xlabel('Data')
plt.ylabel('Consumo de Água (litros)')
plt.title('Segmentação de Consumo de Água por Clusters')
plt.legend()
plt.grid(True)
plt.show()
