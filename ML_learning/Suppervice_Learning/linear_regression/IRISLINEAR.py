import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

iris = pd.read_csv("IRIS.csv")

X = iris.drop("species",axis =1)
y = iris["species"]

y = y.map({"Iris-setosa":1 , "Iris-versicolor":2,"Iris-virginica":3})

X_train , X_test ,y_train , y_test = train_test_split(
    X , y , test_size=0.2 , random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train,y_train)

y_pred = linear_model.predict(X_test)

# print("MSE",mean_squared_error(y_test,y_pred))
print("r2_score",r2_score(y_test,y_pred))