from sklearn import datasets

dataset=datasets.load_breast_cancer()

x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

from sklearn.svm import SVC
algoritmo=SVC(kernel='linear')

#*Entreno el modelo
algoritmo.fit(x_train,y_train)

#*Realizo una predicción
y_pred=algoritmo.predict(x_test)

#? Metricas de evalucion
from sklearn.metrics import confusion_matrix

matriz=confusion_matrix(y_test,y_pred)
print(matriz)

#*Calculo la precisión del modelo
from sklearn.metrics import precision_score
precision=precision_score(y_test,y_pred)

#*Calculo la exactitud
from sklearn.metrics import accuracy_score
exactitud=accuracy_score(y_test,y_pred)

#*Calculo la sensibilidad
from sklearn.metrics import recall_score
sensibilidad=recall_score(y_test,y_pred)

#*Calculo el porcentaje F1 
from sklearn.metrics import f1_score
puntajef1=f1_score(y_test,y_pred)

#*Calculo la curva ROC - AUC 
from sklearn.metrics import roc_auc_score
roc_auc=roc_auc_score(y_test,y_pred)

