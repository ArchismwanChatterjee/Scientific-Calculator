import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def perform_trigonometry(operation, angle_degrees):
    angle_radians = np.radians(angle_degrees)

    if operation == 'Sine':
        result = np.sin(angle_radians)
    elif operation == 'Cosine':
        result = np.cos(angle_radians)
    elif operation == 'Tangent':
        result = np.tan(angle_radians)
    elif operation == 'Secant':
        result = 1 / np.cos(angle_radians)
    elif operation == 'Cosecant':
        result = 1 / np.sin(angle_radians)
    elif operation == 'Cotangent':
        result = 1 / np.tan(angle_radians)
    else:
        result = None

    return result

def trigo_calculator():
    
    st.image("trigo.gif")
    
    st.title("Trigonometric Calculator")

    angle = st.number_input('Enter Angle (degrees)', value=0.0)
    operations = ['Sine', 'Cosine', 'Tangent', 'Secant', 'Cosecant', 'Cotangent']
    operation = st.selectbox('Select Trigonometric Operation', operations)

    result = perform_trigonometry(operation, angle)

    if result is not None:
        st.success(f'{operation}({angle} degrees) = {result:.4f}')
    
    st.text("")
    st.text("")
    
    x = np.linspace(0, 360, 1000)
    y = perform_trigonometry(operation, x)
    
    fig, ax = plt.subplots(figsize=(10, 4))  
    ax.plot(x, y)
    ax.set_xlabel('Angle (degrees)')
    ax.set_ylabel(f'{operation}(Angle)')
    st.pyplot(fig)

if __name__ == '__main__':
    trigo_calculator()

