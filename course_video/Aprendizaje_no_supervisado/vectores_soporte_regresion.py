from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

boston = datasets.load_boston()

# Seleccionamos solo la columna 6 del dataset
x_svr = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
y_svr = boston.target


x_train, x_test, y_train, y_test = train_test_split(
    x_svr, y_svr, test_size=0.2)


# Defino el algoritmo a utilizar
svr = SVR(kernel='linear', C=1.0, epsilon=0.2)

# Entreno el modelo
svr.fit(x_train, y_train)

# Realizo una predicción
y_pred = svr.predict(x_test)

# Graficamos los datos juntos con el modelo
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='red', linewidth=3)
plt.show()

print('PRECISIÓN DEL MODELO')
print(svr.score(x_train,y_train))