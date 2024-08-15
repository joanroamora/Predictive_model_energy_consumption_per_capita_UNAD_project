# 🇺🇸 Analytical Tool for Per Capita Energy Consumption Projection

## Objective

The objective of this tool is to provide an interactive platform for projecting the per capita energy consumption of various countries until the year 2050. Using predictive linear regression models, users can load historical datasets, impute missing values, and obtain future energy consumption predictions.

## Problems Solved

- **Missing Data Imputation**: The tool offers functionality to impute missing values in the dataset, which is crucial for ensuring data integrity and consistency before performing predictive analysis.
- **Energy Consumption Projection**: Allows users to perform energy consumption projections using a linear regression model trained with historical data.
- **Interactive Interface**: Provides an interactive user interface that facilitates data loading, country and year selection, and prediction visualization.

## Implementation

### Project Structure

- **app.py**: Implements the Flask server that handles routes, data loading, missing value imputation, and provides a web interface for user interaction.
- **index.html**: Provides the structure for the web interface, allowing users to interact with the tool, select countries and years, and view generated predictions.
- **script.py**: Auxiliary script for executing functions related to data loading, missing value imputation, and energy consumption projection from the command line.

### Code Description

#### app.py
- **Flask Application**: The Flask application manages the main routes, including:
  - `/`: Loads the main page and displays the list of available countries.
  - `/prepare_data`: Loads the energy consumption dataset, performs missing value imputation, and saves the result in a global variable.
  - `/get_countries`: Returns a list of countries present in the imputed dataset.
  
- **Main Functions**:
  - `load_dataset(filepath)`: Loads a dataset from a CSV file.
  - `impute_missing_values(df)`: Imputes missing values in the dataset by replacing them with the row mean.

#### index.html
- **User Interface**:
  - Includes a form for selecting a country and a projection year.
  - Interactive buttons for loading the dataset and generating predictions.
  - Dynamically updates the available countries after loading the dataset.

#### script.py
- **Auxiliary Functions**:
  - `load_dataset(filepath)`: Similar to the version in `app.py`, loads a dataset from a CSV file.
  - `impute_missing_values(df)`: Imputes missing values using the corresponding row mean.
  - `predict_energy_consumption(df, year, row_index)`: Uses a linear regression model to project a country’s energy consumption until the specified year and generates a prediction graph.

### Project Execution

1. **Prerequisites**:
   - Install dependencies: `pip install flask pandas numpy scikit-learn matplotlib`
   - Ensure a CSV file with historical data is available at `./data/energy_data.csv`.

2. **Running the Server**:
   - Start the Flask application:
     ```bash
     python app.py
     ```
   - Access the tool in your browser at `http://127.0.0.1:3000/`.

3. **Command Line Usage**:
   - Run `script.py` to make a direct projection:
     ```bash
     python script.py
     ```

   This will load the dataset, impute missing values, and generate a prediction and graph saved as `energy_projection.png`.

## Contribution

Contributions are welcome. Please open an issue or submit a pull request if you would like to contribute to the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# 🇨🇴 Herramienta Analítica para la Proyección de Consumo Energético Per Cápita

## Objetivo

El objetivo de esta herramienta es proporcionar una plataforma interactiva que permita proyectar el consumo energético per cápita de diversos países hasta el año 2050. Utilizando modelos predictivos de regresión lineal, los usuarios pueden cargar datasets históricos, imputar valores faltantes, y obtener predicciones del consumo energético futuro.

## Problemas que Resuelve

- **Imputación de Datos Faltantes**: La herramienta ofrece una funcionalidad para imputar valores faltantes en el dataset, crucial para asegurar la integridad y consistencia de los datos antes de realizar análisis predictivos.
- **Proyección de Consumo Energético**: Permite realizar proyecciones del consumo energético per cápita utilizando un modelo de regresión lineal entrenado con datos históricos.
- **Interfaz Interactiva**: Proporciona una interfaz de usuario interactiva que facilita la carga de datos, selección de países y años, y visualización de predicciones.

## Implementación

### Estructura del Proyecto

- **app.py**: Contiene la implementación del servidor Flask que gestiona las rutas, carga de datos, imputación de valores faltantes, y ofrece una interfaz web para la interacción con los usuarios.
- **index.html**: Proporciona la estructura de la interfaz web, permitiendo a los usuarios interactuar con la herramienta, seleccionar países y años, y ver las proyecciones generadas.
- **script.py**: Script auxiliar para ejecutar las funciones de carga de datos, imputación de valores, y proyección de consumo energético desde la línea de comandos.

### Descripción del Código

#### app.py
- **Flask Application**: La aplicación Flask se encarga de manejar las rutas principales, incluyendo:
  - `/`: Carga la página principal y muestra la lista de países disponibles.
  - `/prepare_data`: Carga el dataset de consumo energético, realiza la imputación de valores faltantes y guarda el resultado en una variable global.
  - `/get_countries`: Devuelve una lista de países presentes en el dataset imputado.
  
- **Funciones Principales**:
  - `load_dataset(filepath)`: Carga un dataset desde un archivo CSV.
  - `impute_missing_values(df)`: Imputa valores faltantes en el dataset reemplazándolos por el promedio de los valores de la misma fila.

#### index.html
- **Interfaz de Usuario**:
  - Incluye un formulario para seleccionar un país y un año de proyección.
  - Botones interactivos para cargar el dataset y generar predicciones.
  - Se actualizan dinámicamente las opciones de países disponibles tras cargar el dataset.

#### script.py
- **Funciones Auxiliares**:
  - `load_dataset(filepath)`: Similar a la versión en `app.py`, carga un dataset desde un archivo CSV.
  - `impute_missing_values(df)`: Imputa valores faltantes usando el promedio de la fila correspondiente.
  - `predict_energy_consumption(df, year, row_index)`: Utiliza un modelo de regresión lineal para proyectar el consumo energético de un país hasta el año indicado y genera una gráfica de la predicción.

### Ejecución del Proyecto

1. **Requisitos Previos**: 
   - Instalar dependencias: `pip install flask pandas numpy scikit-learn matplotlib`
   - Asegurarse de tener un archivo CSV con datos históricos en `./data/energy_data.csv`.

2. **Ejecución del Servidor**:
   - Iniciar la aplicación Flask:
     ```bash
     python app.py
     ```
   - Acceder a la herramienta desde el navegador en `http://127.0.0.1:3000/`.

3. **Uso desde la Línea de Comandos**:
   - Ejecutar `script.py` para realizar una proyección directa:
     ```bash
     python script.py
     ```

   Esto cargará el dataset, imputará valores faltantes y generará una predicción y una gráfica que se guardará como `energy_projection.png`.

## Contribución

Las contribuciones son bienvenidas. Por favor, abra un *issue* o envíe un *pull request* si desea contribuir al proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.
