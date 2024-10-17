# model.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Charger le dataset Iris
iris =  pd.read_csv('data/iris.csv')
X = iris.drop('class', axis=1)  # Assurez-vous que le nom de la colonne cible est 'species'

y = iris['class']
# Diviser en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Évaluer la précision
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Sauvegarder le modèle
joblib.dump(model, 'iris_model.joblib')
