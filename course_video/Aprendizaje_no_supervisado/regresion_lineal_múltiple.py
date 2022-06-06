from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

#Importamos los datos de la misma libreria de scikit-learn
boston=datasets.load_boston()

#*Seleccionamos las columnas 5,6 y 7 del dataset
x_multiple=boston.data[:,5:8]
#*Defino los datos correspondientes a las etiquetas
y_multiple=boston.target

#? Separo los dato de "train" en entrenamiento y prueba para probar los algoritmos
x_train,x_test,y_train,y_test= train_test_split(x_multiple,y_multiple,test_size=0.2)

#?Defino el algoritmo a utilizar
lr_multiple=linear_model.LinearRegression()

#?Entreno el modelo
lr_multiple.fit(x_train,y_train)

#?Realizo una predicción
y_pred_multiple=lr_multiple.predict(x_test)

print('DATOS DEL MODELO DE REGRESION MULTIPLE')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(lr_multiple.intercept_)
print("Precisión del modelo")
print(lr_multiple.score(x_train, y_train))

