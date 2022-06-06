from sklearn import datasets

dataset=datasets.load_breast_cancer()

x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
algpritmo=RandomForestClassifier(n_estimators=10, criterion='entropy')

algpritmo.fit(x_train,y_train)

y_pred=algpritmo.predict(x_test)
