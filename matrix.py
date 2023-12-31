import streamlit as st
import numpy as np

def parse_matrix(matrix_text):
    # Split the text area content into rows
    rows = matrix_text.strip().split('\n')
    
    # Split each row into individual elements
    matrix = [list(map(float, row.split())) for row in rows]
    
    return np.array(matrix)

def matrix_calculator():
# Streamlit app
    
    st.image("matrix.png",width=50)

    st.title("Matrix Calculator")


    col1, col2=st.columns(2)

# Get user input for the matrix
    with col1:

        matrix_text_A = st.text_area("Enter matrix A (each row on a new line, elements separated by space):")

        if st.button("Display Matrix",key="A"):
            try:
        # Parse the input matrix
                user_matrix_A = parse_matrix(matrix_text_A)
        
        # Display the parsed matrix
                st.write("Matrix A:")
                st.write(user_matrix_A)
        
        # You can perform further processing with the matrix here
        # For example, compute the determinant, inverse, etc.
            except ValueError:
                st.error("Invalid matrix input. Please check your input format.")

    with col2:

        matrix_text_B = st.text_area("Enter matrix B(each row on a new line, elements separated by space):")

        if st.button("Display Matrix",key="B"):
            try:
        # Parse the input matrix
                user_matrix_B = parse_matrix(matrix_text_B,)
        
        # Display the parsed matrix
                st.write("Matrix B:")
                st.write(user_matrix_B)
        
        # You can perform further processing with the matrix here
        # For example, compute the determinant, inverse, etc.
            except ValueError:
                st.error("Invalid matrix input. Please check your input format.")


    st.write("Choose your operation")

    col3,col4,col5,col6=st.columns(4)

    if col3.button("Addition"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)
            user_matrix_B = parse_matrix(matrix_text_B)

            result_matrix = (user_matrix_A + user_matrix_B).astype(int)

            st.text("")
            
            st.write("Result (Addition):")
            st.write(result_matrix)

        except ValueError:
            st.error("Matrix addition is not possible. Please check the matrix dimensions.")

    if col3.button("Subtraction"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)
            user_matrix_B = parse_matrix(matrix_text_B)

            result_matrix = (user_matrix_A - user_matrix_B).astype(int)

            st.text("")
            
            st.write("Result (Subtraction):")
            st.write(result_matrix)

        except ValueError:
            st.error("Matrix subtraction is not possible. Please check the matrix dimensions.")

    if col3.button("Multiplication"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)
            user_matrix_B = parse_matrix(matrix_text_B)

            result_matrix = np.matmul(user_matrix_A, user_matrix_B).astype(int)

            st.text("")
            
            st.write("Result (Multiplication):")
            st.write(result_matrix)

        except ValueError:
            st.error("Matrix multiplication is not possible. Please check the matrix dimensions.")

    if col4.button("Dot Product(A.B)"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)
            user_matrix_B = parse_matrix(matrix_text_B)

            result_matrix = np.dot(user_matrix_A.flatten(), user_matrix_B.flatten()).astype(int)

            st.text("")
            
            st.write("Result (Dot Product):")
            st.success(result_matrix)

        except ValueError:
            st.error("Dot Product is not possible. Please check the matrix dimensions.")

    if col4.button("Cross Product(A x B)"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)
            user_matrix_B = parse_matrix(matrix_text_B)

            result_matrix = np.cross(user_matrix_A, user_matrix_B).astype(int)

            st.text("")
            
            st.write("Result (Cross Product):")
            st.write(result_matrix)

        except ValueError:
            st.error("Cross Product is not possible. Please check the matrix dimensions.")

    if col4.button("Rank of A"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)

            result_matrix = np.linalg.matrix_rank(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Rank of A):")
            st.success(result_matrix)

        except ValueError:
            st.error("Rank of Matrix is not possible. Please check the matrix dimensions.")
    
    if col5.button("Transpose of A"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)

            result_matrix = np.transpose(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Transpose of A):")
            st.write(result_matrix)

        except ValueError:
            st.error("Transpose of Matrix is not possible. Please check the matrix dimensions.")
    
    if col5.button("Inverse of A"):
        
        user_matrix_A = parse_matrix(matrix_text_A)

        if (np.linalg.det(user_matrix_A).astype(int)!=0):

            result_matrix = np.linalg.inv(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Inverse of A):")
            st.write(result_matrix)

        else:
            st.error("Inverse of Matrix is not possible as determinant is zero. Please use singular matrix.")

    if col5.button("Determinant of A"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)

            result_matrix = np.linalg.det(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Determiant of A):")
            st.success(result_matrix)

        except ValueError:
            st.error("Wrong Input")
    
    if col6.button("Eigenvalues of A"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)

            result_matrix = np.linalg.eigvals(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Eigenvalues of A):")
            st.write(result_matrix)

        except ValueError:
            st.error("Eigenvalues of Matrix is not possible. Please check the matrix dimensions.")
    
    if col6.button("Euclidean normal of A"):
        try:
            user_matrix_A = parse_matrix(matrix_text_A)

            result_matrix = np.linalg.norm(user_matrix_A).astype(int)

            st.text("")
            
            st.write("Result (Eigenvalues of A):")
            st.success(result_matrix)

        except ValueError:
            st.error("Eigenvalues of Matrix is not possible. Please check the matrix dimensions.")



if __name__ == "__main__":
    matrix_calculator()
