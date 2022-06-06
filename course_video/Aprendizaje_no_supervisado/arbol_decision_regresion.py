from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

boston=datasets.load_boston()

# Seleccionamos solo la columna 6 del dataset
x_adr = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
y_adr = boston.target

#* IMPLEMENTACIÓN DE ARBOLES DE DECISIÓN REGRESION

x_train, x_test, y_train, y_test = train_test_split(x_adr, y_adr, test_size=0.2)

from sklearn.tree import DecisionTreeRegressor

#Defino el algoritmo a usar
adr=DecisionTreeRegressor(max_depth=5)

#Entrena el modelo
adr.fit(x_train,y_train)

#Realizo una predicción
Y_pred=adr.predict(x_test)

#Graficamos los datos de prueba junto con la predicción
x_grid=np.arange(min(x_test),max(x_test),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(x_test,y_test)
plt.plot(x_grid,adr.predict(x_grid), color='red', linewidth=3)
plt.show()






