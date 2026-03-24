import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score,confusion_matrix, classification_report, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

heart_df = pd.read_csv("heart.csv")

X = heart_df.drop("target", axis=1)
y = heart_df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

y_train[y_train == 1] # 133
y_train[y_train == 0] #109

model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("accuracy: ", accuracy_score(y_test, y_pred)*100, "%")
# print("precision: ", precision_score(y_test, y_pred)*100, "%")

# cm = confusion_matrix(y_test,y_pred)
# print(cm)
# print("accuracy: ", accuracy_score(y_test, y_pred)*100, "%")
# print("precision: ", precision_score(y_test, y_pred)*100, "%")
# print("recall score: ",recall_score(y_test,y_pred)*100,"%")
# print("f1 score: ",f1_score(y_test,y_pred)*100,"%")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("accuracy: " , accuracy_score(y_test,y_pred)*100 ,"%")
print("precision: ", precision_score(y_test,y_pred)*100 ,"%")
print(classification_report(y_test,y_pred))
print("recall: ", recall_score(y_test,y_pred)*100 ,"%")
print("f1: ", f1_score(y_test,y_pred)*100 ,"%")