from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

X, y = make_regression(
    n_samples=500,
    n_features=20,
    noise=20,
    random_state=42
)

X_train , X_test ,y_train , y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

dt_tree = DecisionTreeRegressor(
    max_depth=1
)

ada = AdaBoostRegressor(
    #estimator=dt_tree,
    n_estimators=200,
    random_state=42
)

ada.fit(X_train,y_train)

y_pred = ada.predict(X_test)

print("r2_score = ",r2_score(y_test,y_pred))