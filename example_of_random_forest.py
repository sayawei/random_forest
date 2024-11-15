import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
data_size = 1000

data = pd.DataFrame({
    'age': np.random.randint(18, 70, data_size),
    'income': np.round(np.random.normal(50000, 15000, data_size), 2),
    'credit_score': np.random.randint(300, 850, data_size),
    'marital_status': np.random.choice(['Single', 'Married', 'Divorced'], data_size),
    'owns_house': np.random.choice(['Yes', 'No'], data_size),
    'job_type': np.random.choice(['Salaried', 'Self-employed', 'Unemployed'], data_size),
    'use_product': np.random.choice([0, 1], data_size)
})

print(data.head())

encoder = LabelEncoder()
data['marital_status'] = encoder.fit_transform(data['marital_status'])
data['owns_house'] = encoder.fit_transform(data['owns_house'])
data['job_type'] = encoder.fit_transform(data['job_type'])

X = data.drop(columns='use_product')
y = data['use_product']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
