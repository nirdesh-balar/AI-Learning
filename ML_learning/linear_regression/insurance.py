import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Train Test split
from sklearn.model_selection import train_test_split

# Train Model
from sklearn.linear_model import LinearRegression

# Evaluate 
from sklearn.metrics import r2_score

insurance_data = pd.read_csv("insurance.csv")

sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"],hue= insurance_data["smoker"])

#plt.show()

# X = insurance_data.drop(columns=["charges", "region"])
# y = insurance_data["charges"]

# X["sex"] = X["sex"].map({"female": 1, "male": 0})
# X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})

# # for train and split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42)

# # for train model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predict values
# y_pred = model.predict(X_test)

# # fot how model is accurate for random data
# r2 = r2_score(y_test, y_pred)
# print("r-squared:", r2)

# n = X_test.shape[0]
# p = X_test.shape[1]

# adjusted_r2 = 1 - ((1-r2) * (n-1) / (n-p-1))
# print("adjusted r^2:", adjusted_r2)



#  Feture enginnering

#  one hot encoding (using in single column multiple data into multiple column data) (used for incress model accurecy)
#  during One Hot Encoding we have facing "Dummy variable trap" . for this problem's solution we have to "drop_first = False" to "drop_first = True" to doing this one column is drop for reduce  redundancy 
 
# X = insurance_data.drop(columns=["charges"])
# y = insurance_data["charges"]

# X = pd.get_dummies(X, columns=["region"] , drop_first= True , dtype=int)

# X["sex"] = X["sex"].map({"female": 1, "male": 0})
# X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})

# X_train,X_test,y_train,y_test = train_test_split(X , y, test_size=0.2 , random_state=42)

# model = LinearRegression()
# model.fit(X_train,y_train)

# y_pred = model.predict(X_test)

# r2 = r2_score(y_test , y_pred)
# print("r2 score = " , r2)


# Interaction Features
X = insurance_data.drop(columns=["charges"])
y = insurance_data["charges"]

X = pd.get_dummies(X, columns=["region"], drop_first=True, dtype=int)

X["sex"] = X["sex"].map({"female": 1, "male": 0})
X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})

X["age_smoker"] = X["age"] * X["smoker"]
X["bmi_smoker"] = X["bmi"] * X["smoker"]

X_train,X_test , y_train , y_test = train_test_split (X ,y ,train_size=0.2 , random_state=42)

model = LinearRegression()
model.fit(X_train , y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test,y_pred)
print(r2)


# underfit & overfit
# r2 training is low & r2 testing is also low - underfit
# r2 training >> r2 testing is also low - overfit

y_train_pred = model.predict(X_train)
r2_train = r2_score(y_train,y_train_pred)

print("training data r2:", r2_train)
# print("test data r2:", r2)


