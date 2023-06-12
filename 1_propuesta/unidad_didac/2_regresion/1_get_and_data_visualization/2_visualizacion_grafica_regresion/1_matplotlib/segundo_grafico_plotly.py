import plotly.graph_objects as go

# Datos de ejemplo
x = ['A', 'B', 'C', 'D']
y = [10, 8, 6, 4]

# Crear el gráfico de barras
fig = go.Figure(data=go.Bar(x=x, y=y))

# Personalizar el gráfico
fig.update_layout(title='Gráfico de barras interactivo', xaxis_title='Categoría', yaxis_title='Valor')

# Mostrar el gráfico
fig.show()
