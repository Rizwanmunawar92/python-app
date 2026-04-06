import streamlit as st  

# 1. Page Config (MUST be at the very top and only once)
st.set_page_config(page_title="QS Automation Pro", page_icon="🏗️")

st.title("🏗️ Quantity Surveyor: Python Automation")
st.markdown("---")

# 2. Interactive Inputs
st.header("Quick Cost Estimator")
col1, col2 = st.columns(2)

with col1:
    material_name = st.text_input("Material/Element Name", value="Concrete Slab")
    quantity = st.number_input("Quantity (m2/m3)", value=1.0, step=1.0)

with col2:
    unit_rate = st.number_input("Unit Rate (£)", value=0.0, step=0.5)
    wastage_percent = st.slider("Wastage Allowance (%)", 0, 15, 5)

# 3. Python Logic (The "Engine")
wastage_multiplier = 1 + (wastage_percent / 100)
subtotal = quantity * unit_rate
total_with_wastage = subtotal * wastage_multiplier

# 4. Displaying Results
st.markdown("---")
if st.button("Calculate Final Cost"):
    st.subheader(f"Total for {material_name}")
    st.metric(label="Total Cost (inc. wastage)", value=f"£{total_with_wastage:,.2f}")
    
    st.write(f"*Breakdown:*")
    st.write(f"* Base Cost: £{subtotal:,.2f}")
    st.write(f"* Wastage Added: £{(total_with_wastage - subtotal):,.2f}")
    
    if total_with_wastage > 1000:
        st.warning("⚠️ High Value Item: Check procurement lead times.")
    else:
        st.success("✅ Item within standard budget threshold.")
    
    # Only show balloons after the calculation button is pressed!
    st.balloons()