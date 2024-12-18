import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Definición de las funciones
def f1(x):
    return 3 * x + 2

def f2(x):
    return x**3

def f3(x):
    return np.exp(2 * x)

def f4(x):
    return np.log(x)

def f5(x):
    return x**4 - 2 * x**2 + 1

# Diccionario de ejercicios
exercises = {
    "Ejercicio 1: f(x) = 3x + 2": (f1, -1, 3, 0, 2),
    "Ejercicio 2: f(x) = x^3": (f2, -1, 3, 0, 2),
    "Ejercicio 3: f(x) = e^(2x)": (f3, 0, 2, 0, 1),
    "Ejercicio 4: f(x) = ln(x)": (f4, 0.1, 3, 1, 2),
    "Ejercicio 5: f(x) = x^4 - 2x^2 + 1": (f5, -2, 2, 0, 1),
}

# Resolver el ejercicio
def solve_exercise(func, x1, x2, λ=0.5):
    x_mid = λ * x1 + (1 - λ) * x2
    y_mid = func(x_mid)
    y_comb = λ * func(x1) + (1 - λ) * func(x2)
    is_convex = y_mid <= y_comb
    return x_mid, y_mid, y_comb, is_convex

# Generar la gráfica
def plot_function(func, xmin, xmax, x1, x2, x_mid, y_mid, y_comb):
    x = np.linspace(xmin, xmax, 500)
    y = func(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x)", color="blue")
    plt.plot([x1, x2], [func(x1), func(x2)], 'r--', label="Línea convexa")
    plt.scatter([x1, x2, x_mid], [func(x1), func(x2), y_mid], color="red", zorder=5)
    plt.scatter([x_mid], [y_comb], color="green", label="Punto combinado", zorder=5)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title("Visualización de la función y combinación convexa", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    st.pyplot(plt)

# Configuración de la aplicación
st.set_page_config(page_title="Funciones y Convexidad", layout="wide")
st.title("Visualización y Resolución de Ejercicios de Convexidad")
st.sidebar.title("Selecciona un Ejercicio")

# Selección de ejercicio
exercise_name = st.sidebar.selectbox("Ejercicio", list(exercises.keys()))
func, xmin, xmax, x1, x2 = exercises[exercise_name]

# Parámetro λ
λ = st.sidebar.slider("Valor de λ", min_value=0.0, max_value=1.0, value=0.5)

# Resolver y mostrar resultados
x_mid, y_mid, y_comb, is_convex = solve_exercise(func, x1, x2, λ)

st.subheader(exercise_name)
st.markdown(
    f"""
    **Puntos seleccionados:**  
    - x₁ = {x1}, f(x₁) = {func(x1):.2f}  
    - x₂ = {x2}, f(x₂) = {func(x2):.2f}  

    **Combinación convexa:**  
    - x (medio) = {x_mid:.2f}  
    - f(x medio) = {y_mid:.2f}  
    - Combinación convexa de valores: {y_comb:.2f}  

    **¿Es la función convexa?**  
    - {'Sí' if is_convex else 'No'}
    """
)

# Mostrar gráfica
st.subheader("Gráfica")
plot_function(func, xmin, xmax, x1, x2, x_mid, y_mid, y_comb)

# Pie de página
st.sidebar.info("Creado por: Tu Nombre")
