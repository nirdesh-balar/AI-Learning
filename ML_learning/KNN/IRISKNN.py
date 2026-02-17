import pandas as pd
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline



iris = pd.read_csv("IRIS.csv")

X = iris.drop("species" , axis =1)
y = iris["species"]

# X_train , X_test , y_train , y_test = train_test_split(
#     X,y , test_size=0.2 , random_state=42
# )

# scaler = StandardScaler()  
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# Knn = KNeighborsClassifier(n_neighbors=11) 
# Knn.fit(X_train_scaled , y_train) 

# y_pred = Knn.predict(X_test_scaled)

# print("accuracy score: ", accuracy_score(y_test, y_pred))
# print("Classification Report:", classification_report(y_test, y_pred))


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('knn', KNeighborsClassifier())
])

param_grid = {"knn__n_neighbors": [3, 5, 7, 9]}

classifierCV = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
)

classifierCV.fit(X_train, y_train)

y_pred = classifierCV.predict(X_test)

print("accuracy score: ", accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))

print(classifierCV.best_params_)