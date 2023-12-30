
import streamlit as st
import math

def math_calculator():
    st.title("Mathematical Calculator")

    num = st.number_input("Enter the number(n): ")
    num2= st.number_input("Enter the number(r): ")
    num3=int(num)
    num4=int(num2)


    st.write("Choose your operation")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    # Button to perform Round-Off
    if col1.button("Rnd(n)"):
        st.text("")
        result = round(num)
        st.success(f"Result (Rnd(n)): {result}")

    # Button to perform Factorial
    if col3.button("n!"):
        if num.is_integer() and num >= 0:
            st.text("")
            result = math.factorial(int(num))
            st.success(f"Result (Factorial): {result}")
        else:
            st.error("Please enter a non-negative integer for Factorial.")

    # Buttons to perform Exponential
    if col2.button("2^n"):
        st.text("")
        result = 2 ** num
        st.success(f"Result (2^n): {result}")

    if col2.button("e^n"):
        st.text("")
        result = math.exp(num)
        st.success(f"Result (e^n): {result}")

    if col2.button("n^r"):
        st.text("")
        result = math.pow(num,num2)
        st.success(f"Result (n^r): {result}")

    # Button to perform Permutation
    if col1.button("nPr"):
        if num3>=num4:
            result=math.perm(num3,num4)
            st.success(f"Result (nPr): {result}")
        else:
            st.error("Please ensure that n>=r")

    # Button to perform Combination
    if col1.button("nCr"):
        if num3>=num4:
            result=math.comb(num3,num4)
            st.success(f"Result (nCr): {result}")
        else:
            st.error("Please ensure that n>=r")

    # Button to perform Logarithm
    if col4.button("log n"):
        if num!=0:
            result=math.log10(num)
            st.success(f"Result (log n): {result}")
        else:
            st.error("n cannot be 0")

    if col4.button("ln n"):
        if num!=0:
            result=math.log(num)
            st.success(f"Result (ln n): {result}")
        else:
            st.error("n cannot be 0")
    
    if col4.button("log of n to the base r"):
        if num!=0 and num2!=0:
            result=math.log(num,num2)
            st.success(f"Result (log of n to the base r): {result}")
        else:
            st.error("n and r cannot be 0")
    # Button to perform Gamma
    if col3.button("Gamma(n)"):
        result=math.gamma(num)
        st.success(f"Result (Gamma(n)): {result}")
        

    # Button to perform Hypotenuse
    if col3.button("Hypotenuse"):
        result=math.hypot(num,num2)
        st.success(f"Result (hypot(n,r)): {result}")

    
    # Button to perform Root
    if col5.button("Sqrt(n)"):
        result=math.sqrt(num)
        st.success(f"Result (Sqrt(n)): {result}")
    
    if col5.button("Cbrt(n)"):
        result=num**(1/3)
        st.success(f"Result (Cbrt(n)): {result}")

    if col5.button("rth root of n"):
        if num2!=0:
            result=num**(1/num2)
            st.success(f"Result (rth root of n): {result}")
        else:
            st.error("r cannot be 0")
    

if __name__ == "__main__":
    math_calculator()
