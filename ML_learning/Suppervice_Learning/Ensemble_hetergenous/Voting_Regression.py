from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import VotingRegressor
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

vr = VotingRegressor(
    estimators = [
        ("lr", lin_reg),
        ("dtr", dtr),
        ("svr", svr)
    ]
)
vr.fit(X_train, y_train)
y_pred = vr.predict(X_test)



print("r^2 =", r2_score(y_test, y_pred))