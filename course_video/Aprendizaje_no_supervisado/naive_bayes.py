from sklearn import datasets

dataset=datasets.load_breast_cancer()

x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

from sklearn.naive_bayes import GaussianNB
algoritmo=GaussianNB()

algoritmo.fit(x_train,y_train)

algoritmo.predict(x_test)

from sklearn.metrics import confusion_matrix

matriz=confusion_matrix(y_test,y_pred)
print(matriz)






