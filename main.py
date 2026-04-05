import streamlit as st

st.title("🏗️ QS Automation Dashboard")

# Practice: Variables and User Input
st.header("Quick Cost Estimator")

rate = st.number_input("Enter Rate per m2 (£)", value=150.0)
area = st.number_input("Enter Total Area (m2)", value=10.0)

# Practice: Basic Math
total_cost = rate * area

if st.button("Calculate Total"):
    st.subheader(f"Total Estimated Cost: £{total_cost:,.2f}")
    st.info("This is a basic Python calculation running live!")