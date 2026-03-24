from sklearn.ensemble import StackingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


meta_model = LogisticRegression()
lr = LogisticRegression()
svc = SVC()
dtc = DecisionTreeClassifier(max_depth=3)

X, y = make_classification(
    n_samples = 500,
    n_features = 20,
    n_informative = 5,
    n_redundant = 2,
    random_state = 42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

stacking_clf = StackingClassifier(
    estimators= [
        ("lr", lr),
        ("svc", svc),
        ("dtc", dtc)
    ],
    final_estimator=meta_model,
    cv=5
)

stacking_clf.fit(X_train, y_train)
y_pred = stacking_clf.predict(X_test)

print("accuracy, ", accuracy_score(y_test, y_pred))