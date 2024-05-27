import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Dados fornecidos
dados = {
    'Timestamp': [1621396800000, 1621483200000, 1621569600000, 1621656000000, 1621742400000],
    'WaterTankLevel': [1000, 950, 900, 850, 'NaN']  # Adicionando um valor não numérico para simular um erro
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Substituir 'NaN' por valores ausentes reconhecíveis pelo pandas
df['WaterTankLevel'] = df['WaterTankLevel'].replace('NaN', pd.NA)

# Remover valores ausentes
df = df.dropna()

# Converter 'WaterTankLevel' para tipo numérico
df['WaterTankLevel'] = pd.to_numeric(df['WaterTankLevel'])

# Ajustar o modelo SARIMA
modelo = SARIMAX(df['WaterTankLevel'], order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
resultado = modelo.fit(disp=False)

# Fazer previsões para o futuro
horizonte_futuro = 5  # Horizonte de previsão de 5 unidades de tempo (por exemplo, dias)
previsao = resultado.get_forecast(steps=horizonte_futuro)

# Obter os valores previstos e seus intervalos de confiança
previsao_media = previsao.predicted_mean
intervalo_confianca = previsao.conf_int()

# Imprimir as previsões
print("Previsão do nível do tanque de água:")
print(previsao_media)
print("\nIntervalo de confiança para as previsões:")
print(intervalo_confianca)
