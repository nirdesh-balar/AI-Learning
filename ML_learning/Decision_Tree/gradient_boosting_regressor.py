from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor

# generate data

X, y = make_regression(
    n_samples=1000,
    n_features=10,
    noise=20,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

gbr = GradientBoostingRegressor(
    n_estimators=200,  # How many decision tree we want to use (week learner tree).
    learning_rate=0.05,
    max_depth=3,
    subsample=0.8,
    random_state=42
)

gbr.fit(X_train, y_train)

y_pred = gbr.predict(X_test)

print("r^2: ", r2_score(y_test, y_pred))