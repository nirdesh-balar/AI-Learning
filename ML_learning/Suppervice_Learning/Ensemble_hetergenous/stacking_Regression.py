from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import StackingRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

X, y = make_regression(
    n_samples = 500,
    n_features = 20,
    n_informative = 5,
    random_state = 42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

lin_reg = LinearRegression()
dtr = DecisionTreeRegressor(max_depth=3)
svr = SVR()

sr = StackingRegressor(
    estimators = [
        ("lr", lin_reg),
        ("dtr", dtr),
        ("svr", svr)
    ],
    cv=5
)

sr.fit(X_train, y_train)

y_pred = sr.predict(X_test)
y_pred_train = sr.predict(X_train)

print("r2 score test", r2_score(y_test, y_pred))
print("r2 score train", r2_score(y_train, y_pred_train))