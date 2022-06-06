import numpy as np
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt

boston=datasets.load_boston()

x_p= boston.data[:,np.newaxis, 5]
y_p=boston.target



from sklearn.model_selection import train_test_split

#? Separo los dato de "train" en entrenamiento y prueba para probar los algoritmos
x_train_p,x_test_p,y_train_p,y_test_p= train_test_split(x_p,y_p,test_size=0.2)

from sklearn.preprocessing import PolynomialFeatures

#Se define el grado de polinomio
poli_reg=PolynomialFeatures(degree=2)

#Se transforma las características existentes en características de mayor grado
x_train_poli=poli_reg.fit_transform(x_train_p)
x_test_poli=poli_reg.fit_transform(x_test_p)

#Defino el algoritmo a utilizar
pr=linear_model.LinearRegression()

#Entreno el modelo
pr.fit(x_train_poli,y_train_p)

#Realizo una predicción
y_pred_pr=pr.predict(x_test_poli)


plt.scatter(x_p,y_p)
plt.plot(x_test_p,y_pred_pr,color="red",linewidth=3)
plt.show()

print('DATOS DEL MODELO DE REGRESION POLINOMIAL')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(pr.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(pr.intercept_)
print("Precisión del modelo")
print(pr.score(x_train_poli, y_train_p))

