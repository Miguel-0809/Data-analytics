import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

boston= datasets.load_boston()
x=boston.data[:,np.newaxis,5]
y=boston.target



# IMPLEMENTACIÓN DE REGRESIÓN LINEAL SIMPLE

from sklearn.model_selection import train_test_split

#? Separo los dato de "train" en entrenamiento y prueba para probar los algoritmos
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#?Defino el algoritmo a utilizar
lr=linear_model.LinearRegression()

#?Entreno el modelo
lr.fit(x_train,y_train)

#?Realizo una predicción
y_pred=lr.predict(x_test)


plt.scatter(x,y)
plt.plot(x_test,y_pred, color="red", linewidth=3)
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor medio")
plt.show()

print('DATOS DEL MODELO DE REGRESION SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(lr.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(lr.intercept_)




