import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, classification_report, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

iris = pd.read_csv("IRIS.csv")

X = iris.drop("species",axis =1)
y = iris["species"]

y = y.map({"Iris-setosa":1 , "Iris-versicolor":2,"Iris-virginica":3})

X_train , X_test ,y_train , y_test = train_test_split(
    X , y , test_size=0.2 , random_state=42
)



scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train)
X_test_scaler = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaler,y_train)
y_pred = model.predict(X_test_scaler)

print("accuracy: " , accuracy_score(y_test,y_pred)*100 ,"%")
# print("precision: ", precision_score(y_test,y_pred)*100 ,"%")
print("classification:" , classification_report(y_test,y_pred))
# print("recall_score: ", recall_score(y_test,y_pred)*100 ,"%")