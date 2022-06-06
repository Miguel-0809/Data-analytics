import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

boston=datasets.load_boston()

# Seleccionamos solo la columna 6 del dataset
x_bar = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
y_bar = boston.target

#* IMPLEMENTACIÓN DE BOSQUE DE DECISIÓN REGRESION
x_train, x_test, y_train, y_test = train_test_split(x_bar, y_bar, test_size=0.2)

#Defino el algoritmo a utilizar
bar=RandomForestRegressor(n_estimators=300,max_depth=8)

#Entreno el algoritmo
bar.fit(x_train,y_train)

#Realizo una predicción
y_pred=bar.predict(x_test)

#Graficamos los datos de prueba junto con la predicción
x_grid=np.arange(min(x_test),max(x_test),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(x_test,y_test)
plt.plot(x_grid,bar.predict(x_grid), color='red', linewidth=3)
plt.show()

#Precisión del modelo
print(bar.score(x_train,y_train))





