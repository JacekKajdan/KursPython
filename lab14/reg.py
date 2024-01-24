import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv("Salary_dataset.csv")

x = df['YearsExperience'].to_numpy().reshape(-1, 1)
y = df['Salary'].to_numpy()

#Wykres 1
plt.scatter(x, y)
plt.xlabel('Lata doświadczenia')
plt.ylabel('Pensja')
plt.title('Doświadczenie, a pensja dane')
plt.legend()
plt.show()


model = LinearRegression()
model.fit(x, y)

print(f'Współczynnik nachylenia (a): {model.coef_[0]}')
print(f'Wyraz wolny (b): {model.intercept_}')

X_pred = np.linspace(min(x), max(x), 30).reshape(-1, 1)
y_pred = model.predict(X_pred)

#Wykres 2
plt.scatter(x, y)
plt.plot(X_pred, y_pred, color='red')
plt.xlabel('Lata doświadczenia')
plt.ylabel('Doświadczenie, a pensja dane')
plt.title('Regresja liniowa z wygenerowanymi danymi')
plt.legend()
plt.show()