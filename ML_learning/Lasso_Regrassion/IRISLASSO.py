from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV


iris  = pd.read_csv("IRIS.csv")

X = iris.drop("species" , axis = 1)
y = iris["species"]


y = y.map({"Iris-setosa":1 , "Iris-versicolor":2,"Iris-virginica":3})

X_train , X_test ,y_train , y_test = train_test_split(
    X , y , test_size=0.2 , random_state=42
)
# lass_model = Lasso()
# lass_model.fit(X_train,y_train)


a = [0.001,0.01,0.1,1,2,3,4,5,6,9]

lassCV = LassoCV(
    alphas=a,
    cv=5,
    max_iter=1000,
    random_state=42
)
lassCV.fit(X_train,y_train)
y_pred = lassCV.predict(X_test)

print("MSE",mean_squared_error(y_test,y_pred))
print("r2_score",r2_score(y_test,y_pred))