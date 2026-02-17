import pandas as pd
from sklearn.metrics import precision_score, accuracy_score, recall_score ,classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = pd.read_csv("IRIS.csv")

X = iris.drop("species" , axis = 1)
y = iris["species"]
y = y.map({"Iris-setosa":1 , "Iris-versicolor":2,"Iris-virginica":3})


X_train, X_test , y_train , y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

guss_model = GaussianNB()
guss_model.fit(X_train , y_train)

y_pred = guss_model.predict(X_test)

print("recall score: ", classification_report(y_test, y_pred))
print("accuracy score: ", accuracy_score(y_test, y_pred))
# print("precision score: ", precision_score(y_test, y_pred))

