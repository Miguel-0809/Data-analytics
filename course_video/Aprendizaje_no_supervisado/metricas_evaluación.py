from string import punctuation
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

#?METRICAS

#*MATRIZ DE CONFUSIÓN, mide el desempeño de un modelo de clasificación
from sklearn.metrics import confusion_matrix
matriz=confusion_matrix(y_test, y_pred)

#*Relación de predicciones correctas entre el total de predicciones
from sklearn.metrics import accuracy_score
exactitud=accuracy_score(y_test, y_pred)

#* Mide la precision del clasificador a la hora de predecir CASOS POSITIVOS
from sklearn.metrics import precision_score
precision=precision_score(y_test,y_pred)

#*Mide cuan sensible es clasificador para detectar instancias positivas
from sklearn.metrics import recall_score
sensibilidad=recall_score(y_test,y_pred)

#*Medida armónica de la memoria y la precisión
from sklearn.metrics import f1_score
puntaje=f1_score(y_test,y_pred)




