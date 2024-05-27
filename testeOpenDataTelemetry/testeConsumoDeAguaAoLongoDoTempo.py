import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo do hidrômetro acumulado
dados = {
    'Timestamp': [1621396800000, 1621483200000, 1621569600000, 1621656000000, 1621742400000],
    'WaterMeterReading': [1000, 1100, 1200, 1250, 1350]  # Leituras acumuladas do hidrômetro
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Converter 'Timestamp' para datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')

# Calcular a taxa de consumo de água (diferença entre leituras sucessivas)
df['WaterConsumption'] = df['WaterMeterReading'].diff()

# Exibir o DataFrame resultante
print(df)

# Visualizar a taxa de consumo de água ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['WaterConsumption'], marker='o', color='b', label='Consumo de Água')
plt.xlabel('Tempo')
plt.ylabel('Consumo de Água (unidades)')
plt.title('Consumo de Água ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()
