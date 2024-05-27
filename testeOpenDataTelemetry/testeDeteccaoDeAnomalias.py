import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo de consumo de água (leituras do hidrômetro)
dados_consumo = {
    'Timestamp': [1621396800000, 1621483200000, 1621569600000, 1621656000000, 1621742400000, 
                  1621828800000, 1621915200000, 1622001600000, 1622088000000, 1622174400000,
                  1622260800000, 1622347200000, 1622433600000, 1622520000000, 1622606400000],
    'Consumo': [100, 150, 130, 170, 160, 180, 190, 210, 200, 220, 300, 250, 240, 230, 1000]  # Incluindo um valor anômalo
}

# Criar DataFrame
df_consumo = pd.DataFrame(dados_consumo)

# Converter 'Timestamp' para datetime
df_consumo['Timestamp'] = pd.to_datetime(df_consumo['Timestamp'], unit='ms')

# Definir 'Timestamp' como índice
df_consumo.set_index('Timestamp', inplace=True)

# Exibir o DataFrame
print(df_consumo)

# Plotar os dados de consumo
plt.figure(figsize=(10, 6))
plt.plot(df_consumo, marker='o')
plt.xlabel('Data')
plt.ylabel('Consumo de Água (litros)')
plt.title('Consumo de Água ao Longo do Tempo')
plt.grid(True)
plt.show()
