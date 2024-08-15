import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_dataset(filepath):
    """
    Carga el dataset de consumo energético desde un archivo CSV.
    
    Parameters:
    filepath (str): Ruta al archivo CSV.
    
    Returns:
    DataFrame: Un DataFrame de pandas con los datos cargados.
    """
    try:
        # Cargar el dataset
        data = pd.read_csv(filepath)
        print("Dataset cargado correctamente.")
        return data
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")

def impute_missing_values(df):
    """
    Rellena los valores faltantes, representados por "-", en el DataFrame con el promedio
    de los valores numéricos de su misma fila, excluyendo la primera columna.
    
    Parameters:
    df (DataFrame): DataFrame de pandas con valores faltantes.
    
    Returns:
    DataFrame: DataFrame con valores faltantes rellenados.
    """
    # Reemplazar '-' por NaN para poder calcular la media
    df.replace('-', pd.NA, inplace=True)
    # Convertir a numérico, ignorando errores y excluyendo la primera columna
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    # Calcular la media de cada fila, ignorando valores NaN
    row_means = df.iloc[:, 1:].mean(axis=1)
    # Rellenar NaNs con el promedio de la fila correspondiente
    for i in range(len(df)):
        df.iloc[i, 1:] = df.iloc[i, 1:].fillna(row_means[i])
    print("Valores faltantes imputados correctamente.")
    return df

def predict_energy_consumption(df, year, row_index):
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

    # Gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(years_clean, values_clean, label='Datos Históricos')
    plt.plot(future_years, future_values, label='Proyección', linestyle='--')
    plt.title(f"Proyección del Consumo Energético Per Cápita hasta el Año {year}")
    plt.xlabel('Año')
    plt.ylabel('Consumo Energético Per Cápita (kWh)')
    plt.legend()
    plt.savefig("energy_projection.png")  # Guardar la gráfica como un archivo PNG
    plt.close()  # Cerrar la figura después de guardar para liberar memoria
    print(f"Gráfica guardada como 'energy_projection.png'")


# Uso de las funciones
if __name__ == "__main__":
    filepath = './data/energy_data.csv'
    df = load_dataset(filepath)
    df_imputed = impute_missing_values(df)
    # Añadir la línea para ejecutar la predicción
    predict_energy_consumption(df_imputed, 2040, 9)  # Ejemplo con el año 2030 y la fila 14
    print(df.head())  # Muestra las primeras filas del DataFrame
