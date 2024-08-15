from flask import Flask, render_template, jsonify, request, session
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesaria para usar sesiones

# Variable global para almacenar el DataFrame
global_df = None

def load_dataset(filepath):
    try:
        data = pd.read_csv(filepath)
        return data, "Dataset cargado correctamente."
    except Exception as e:
        return None, f"Error al cargar el dataset: {e}"

def impute_missing_values(df):
    df.replace('-', pd.NA, inplace=True)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    row_means = df.iloc[:, 1:].mean(axis=1)
    for i in range(len(df)):
        df.iloc[i, 1:] = df.iloc[i, 1:].fillna(row_means[i])
    return df, "Valores faltantes imputados correctamente."

def predict_energy_consumption(df, year, row_index, country_name):
    """
    Realiza una proyección de consumo energético per cápita usando regresión lineal.
    
    Parameters:
    df (DataFrame): DataFrame que contiene los datos históricos.
    year (int): Año hasta el cual se desea proyectar, entre 2024 y 2050.
    row_index (int): Índice de la fila para la cual se desea hacer la proyección.
    
    Returns:
    None: Imprime en pantalla el valor proyectado y muestra una gráfica.
    """
    # Preparar los datos para la regresión
    years = np.arange(1965, 2024)  # Años de datos históricos
    values = df.iloc[row_index, 1:].values  # Excluir la primera columna con nombres de países
    values = pd.to_numeric(values, errors='coerce')  # Convertir a numérico, manejar no-numéricos

    # Limpiar valores faltantes
    mask = np.isfinite(values)
    years_clean = years[mask]
    values_clean = values[mask]

    # Entrenar el modelo de regresión
    model = LinearRegression()
    model.fit(years_clean.reshape(-1, 1), values_clean)

    # Predecir hasta el año deseado
    future_years = np.arange(2024, year + 1)  # Años a predecir
    all_years = np.concatenate([years_clean, future_years])  # Todos los años para la gráfica
    future_values = model.predict(future_years.reshape(-1, 1))

    # Mostrar resultados
    print(f"Predicción del consumo energético per cápita para el año {year}: {future_values[-1]} kWh")
    
    image_path = "static/images/energy_projection.png"
    if os.path.exists(image_path):
        os.remove(image_path)  # Elimina el archivo si existe

    # Gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(years_clean, values_clean, label='Datos Históricos')
    plt.plot(future_years, future_values, label='Proyección', linestyle='--')
    plt.title(f"Proyección del Consumo Energético Per Cápita hasta el Año {year}")
    plt.xlabel('Año')
    plt.ylabel('Consumo Energético Per Cápita (kWh)')
    plt.legend()
    plt.savefig(image_path)  # Guarda la nueva imagen
    plt.close()

    # Genera un timestamp para la URL de la imagen
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_url = f"{image_path}?t={timestamp}"
    return f"Predicción del consumo energético per cápita para el año {year} en el país {country_name} es: {future_values[-1]} kWh", image_url

@app.route('/')
def index():
    global global_df
    if global_df is not None:
        # Crear una lista de tuplas (índice, país)
        countries = [(i, country) for i, country in enumerate(global_df.iloc[:, 0], start=1)]
    else:
        countries = []
    return render_template('index.html', countries=countries)

@app.route('/prepare_data', methods=['POST'])
def prepare_data():
    global global_df
    df, message = load_dataset('./data/energy_data.csv')
    if df is None:
        return jsonify({'error': message}), 500
    df_imputed, message_impute = impute_missing_values(df)
    global_df = df_imputed  # Guardar el DataFrame imputado en la variable global
    return jsonify({'message': f"{message} {message_impute}"}), 200

@app.route('/get_countries')
def get_countries():
    global global_df
    if global_df is not None:
        countries = [(i, country) for i, country in enumerate(global_df.iloc[:, 0], start=1)]
        return jsonify(countries=countries)
    else:
        return jsonify(countries=[])

@app.route('/predict', methods=['POST'])
def predict():
    global global_df
    year = request.form.get('year', type=int)
    row_index = request.form.get('country', type=int) - 1  # Ajustar para índice de Python

    if year is None or row_index is None or row_index < 0 or global_df is None:
        return jsonify({'error': 'Debe seleccionar año y país'}), 400

    try:
        country_name = global_df.iloc[row_index, 0]  # Asumiendo que la primera columna es el nombre del país
        message, image_path = predict_energy_consumption(global_df, year, row_index, country_name)
        return jsonify({'message': message, 'image_path': image_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=3000)
