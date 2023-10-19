import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from joblib import dump


df = pd.read_csv('creditcard.csv')
df.head()  # Display the first 5 rows

df = df.drop("Time", axis=1)

# Separate the features from the target
X = df.iloc[:, :-1]  # all features
y = df['Class']  # target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize a scaler, then apply it to the features
scaler = StandardScaler() # initialize
X_train = scaler.fit_transform(X_train) # Fit to the training data and transform it
X_test = scaler.transform(X_test) # transform the testing data

model = LogisticRegression(random_state=42)

# Train the model
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Confusion Matrix:', confusion_matrix(y_test, y_pred))

# Save the model
dump(model, 'trained_model.joblib')