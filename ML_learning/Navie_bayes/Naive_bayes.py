import pandas as pd
from sklearn.metrics import precision_score, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

heart = pd.read_csv("heart.csv")

X = heart.drop("target" , axis = 1)
y = heart["target"]

X_train, X_test , y_train , y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

guss_model = GaussianNB()
guss_model.fit(X_train , y_train)

y_pred = guss_model.predict(X_test)

print("recall score: ", recall_score(y_test, y_pred))
print("accuracy score: ", accuracy_score(y_test, y_pred))
print("precision score: ", precision_score(y_test, y_pred))

