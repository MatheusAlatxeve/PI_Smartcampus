import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dados históricos de pressão do poço artesiano (exemplo)
timestamps = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Coluna de timestamps
pressao = np.array([10, 20, 30, 40, 50])  # Pressão correspondente

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(timestamps, pressao, test_size=0.2, random_state=42)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print("Erro quadrático médio:", mse)

# Fazer uma previsão futura
timestamp_futuro = np.array([[6]])  # Timestamp para previsão futura
pressao_futura = model.predict(timestamp_futuro)
print("Pressão prevista para o futuro:", pressao_futura[0])
