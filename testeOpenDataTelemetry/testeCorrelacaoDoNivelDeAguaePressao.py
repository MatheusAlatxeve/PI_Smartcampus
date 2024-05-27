import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Dados de exemplo com nível do tanque de água e pressões do poço artesiano
dados = {
    'Timestamp': [1621396800000, 1621483200000, 1621569600000, 1621656000000, 1621742400000],
    'WaterTankLevel': [1000, 950, 900, 850, 800],  # Nível do tanque de água em litros
    'EntradaPressao': [30, 32, 29, 31, 33],  # Pressão de entrada em psi
    'SaidaPressao': [25, 26, 24, 27, 28]    # Pressão de saída em psi
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Converter 'Timestamp' para datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')

# Exibir o DataFrame
print(df)

# Gráfico de dispersão para visualizar a relação entre nível do tanque e pressão de entrada
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['WaterTankLevel'], y=df['EntradaPressao'])
plt.xlabel('Nível do Tanque de Água (litros)')
plt.ylabel('Pressão de Entrada (psi)')
plt.title('Relação entre Nível do Tanque de Água e Pressão de Entrada')
plt.grid(True)
plt.show()

# Gráfico de dispersão para visualizar a relação entre nível do tanque e pressão de saída
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['WaterTankLevel'], y=df['SaidaPressao'])
plt.xlabel('Nível do Tanque de Água (litros)')
plt.ylabel('Pressão de Saída (psi)')
plt.title('Relação entre Nível do Tanque de Água e Pressão de Saída')
plt.grid(True)
plt.show()

# Calcular o coeficiente de correlação de Pearson entre nível do tanque e pressão de entrada
corr_entrada, _ = pearsonr(df['WaterTankLevel'], df['EntradaPressao'])
print(f'Coeficiente de Correlação de Pearson entre Nível do Tanque e Pressão de Entrada: {corr_entrada:.2f}')

# Calcular o coeficiente de correlação de Pearson entre nível do tanque e pressão de saída
corr_saida, _ = pearsonr(df['WaterTankLevel'], df['SaidaPressao'])
print(f'Coeficiente de Correlação de Pearson entre Nível do Tanque e Pressão de Saída: {corr_saida:.2f}')
