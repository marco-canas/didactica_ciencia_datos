import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# obtener datos

x = 6 * np.random.rand(500) - 3
y = 1 + x + x**2 + x**3 + x **4 + 10 * np.random.randn(500)

# separar para testear

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# preparar datos para algoritmos
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline





mi_pipeline = Pipeline([
            ('poly', PolynomialFeatures(degree=20)),
            ('scaler', StandardScaler())
])

X_preparado = mi_pipeline.fit_transform(X_train.reshape((-1,1)))

# modelo(s)

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import SGDRegressor
sgd_reg = SGDRegressor()

# afinar hiperparámetros
param_grid = [
        {"penalty": ['l2', 'l1'], 'alpha': [1, 0.1, 0.001, 0.00001, 0.0000001]},
        {"penalty": ['elasticnet'], 'l1_ratio': [0.25, 0.5, 0.75], 'learning_rate': ['constant', 'optimal', 'invscaling']}
]

grid_search_poly = GridSearchCV(sgd_reg, param_grid, cv=5,
                    scoring="neg_mean_squared_error", return_train_score=True)

grid_search_poly.fit(X_preparado, y_train)


best_model = grid_search_poly.best_estimator_
grid_search_poly.best_params_
cvres = grid_search_poly.cv_results_

for mean_score, params in zip(cvres["mean_test_score"], cvres['params']):
    print(np.sqrt(-mean_score), params)
best_model.coef_
# validar modelo final sobre conjunto para testear
X_test_prepared = mi_pipeline.transform(X_test.reshape(-1,1))
final_predictions = best_model.predict(X_test_prepared)
final_rmse = np.sqrt(mean_squared_error(y_test, final_predictions))
final_rmse

# mostrar la solución
x_dominio = np.linspace(-3, 3)
x_dominio_preparado = mi_pipeline.transform(x_dominio.reshape(-1,1))
y_rango = best_model.predict(x_dominio_preparado)

plt.plot(X_test, y_test, 'o')
y_real = 1 + x_dominio + x_dominio**2 + x_dominio**3 + x_dominio **4
plt.plot(x_dominio, y_real, 'r--')
plt.plot(x_dominio, y_rango, 'g-')


