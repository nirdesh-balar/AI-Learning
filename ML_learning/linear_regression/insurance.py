import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Train Test split
from sklearn.model_selection import train_test_split

# Train Model
from sklearn.linear_model import LinearRegression

# Evaluate 
from sklearn.metrics import r2_score

insurence_data = pd.read_csv("insurance.csv")

sns.scatterplot(x=insurence_data["bmi"], y=insurence_data["charges"],hue= insurence_data["smoker"])

#plt.show()

X = insurence_data.drop(columns=["charges", "region"])
y = insurence_data["charges"]

X["sex"] = X["sex"].map({"female": 1, "male": 0})
X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})

# for train and split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# for train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# fot how model is accurate for random data
r2 = r2_score(y_test, y_pred)
print("r-squared:", r2)

n = X_test.shape[0]
p = X_test.shape[1]

adjusted_r2 = 1 - ((1-r2) * (n-1) / (n-p-1))
print("adjusted r^2:", adjusted_r2)

