from sklearn.linear_model import LinearRegression

import numpy as np

  

# Datos de ventas (X) y tiempo (Y)

X = np.array([[1], [2], [3], [4], [5]])

Y = np.array([100, 150, 200, 250, 300])

  

# Crear y entrenar el modelo

model = LinearRegression()

model.fit(X, Y)

  

# Predecir ventas futuras

prediccion = model.predict([[6]])

print(prediccion)