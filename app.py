import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('extra_trees_model.pkl')

# Application title
st.title("Prediction of Fluoride Ion Removal Rate using Magnesium Oxide ")

# Instructions
st.markdown("""
### Instructions
This application predicts the removal rate of fluoride ions using amorphous magnesium oxide hollow spheres.  
Please enter the relevant parameters in the input box on the left, then click the "Prediction" button to obtain the predicted results.
""")

# Sidebar styling
st.markdown(
    """
    <style>
    .streamlit-container {
        margin-left: 10px; /* Adjust left margin */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input parameters
st.sidebar.header('Input Parameters')

def user_input_features():
    # Magnesium Oxide Parameters
    st.sidebar.subheader('Magnesium Oxide Parameters')
    bet = st.sidebar.number_input('BET (m2/g)', min_value=0.0, max_value=300.0, value=50.0)
    daverage = st.sidebar.number_input('Daverage (nm)', min_value=0.0, max_value=500.0, value=50.0)
    pore_volume = st.sidebar.number_input('Pore Volume (cm3/g)', min_value=0.0, max_value=5.0, value=1.0)
    qm = st.sidebar.number_input('Qm (mg/g)', min_value=0.0, max_value=1000.0, value=100.0)

    # Reaction Conditions
    st.sidebar.subheader('Reaction Conditions')
    ph = st.sidebar.number_input('pH', min_value=2.0, max_value=13.0, value=7.0)
    time = st.sidebar.number_input('Time (min)', min_value=0.0, max_value=500.0, value=10.0)
    c_mgo = st.sidebar.number_input('C_MgO (g/L)', min_value=0.0, max_value=2.0, value=0.1)
    c_f = st.sidebar.number_input('C_F (mg/L)', min_value=0.0, max_value=100.0, value=10.0)

    # Coexisting Ions
    st.sidebar.subheader('Coexisting Ions')
    no3 = st.sidebar.number_input('NO3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    br = st.sidebar.number_input('Br- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    cl = st.sidebar.number_input('Cl- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    so4 = st.sidebar.number_input('(SO4)2- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    hco3 = st.sidebar.number_input('HCO3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    co3 = st.sidebar.number_input('(CO3)2- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    po4 = st.sidebar.number_input('(PO4)3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)

    data = {
        'BET': bet,
        'Daverage': daverage,
        'Pore Volume': pore_volume,
        'Qm': qm,
        'pH': ph,
        'time': time,  # Ensure the key matches the model's expected input
        'C_MgO': c_mgo,
        'C_F': c_f,
        'NO3-': no3,
        'Br-': br,
        'Cl-': cl,
        '(SO4)2-': so4,
        'HCO3-': hco3,
        '(CO3)2-': co3,
        '(PO4)3-': po4
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get input data
df = user_input_features()

# Display input parameters
st.subheader('Input Parameters')

# Using columns to display input parameters
col1, col2 = st.columns(2)
with col1:
    st.write("**BET (m2/g):**", df['BET'].values[0])
    st.write("**Daverage (nm):**", df['Daverage'].values[0])
    st.write("**Pore Volume (cm3/g):**", df['Pore Volume'].values[0])
    st.write("**Qm (mg/g):**", df['Qm'].values[0])
    st.write("**pH:**", df['pH'].values[0])
    st.write("**Time (min):**", df['time'].values[0])  # Ensure consistent key usage
    st.write("**C_MgO (g/L):**", df['C_MgO'].values[0])
    st.write("**C_F (mg/L):**", df['C_F'].values[0])
with col2:
    st.write("**NO3- (mg/L):**", df['NO3-'].values[0])
    st.write("**Br- (mg/L):**", df['Br-'].values[0])
    st.write("**Cl- (mg/L):**", df['Cl-'].values[0])
    st.write("**(SO4)2- (mg/L):**", df['(SO4)2-'].values[0])
    st.write("**HCO3- (mg/L):**", df['HCO3-'].values[0])
    st.write("**(CO3)2- (mg/L):**", df['(CO3)2-'].values[0])
    st.write("**(PO4)3- (mg/L):**", df['(PO4)3-'].values[0])

# Load model and make prediction
model = load_model()

# Prediction button
if st.sidebar.button("Prediction"):
    prediction = model.predict(df)[0]
    st.write(f"**Predicted Removal Rate**: {prediction:.2f}%")
    
    # Progress bar
    percentage = prediction / 100  # Convert percentage to decimal
    st.markdown(f"**Removal Rate**:")
    
    # Gradient color progress bar
    progress_color = f"linear-gradient(90deg, #ff4b4b {percentage*100}%, #d3d3d3 {percentage*100}%)"
    st.markdown(
        f"""
        <div style="width: 100%; height: 24px; background: {progress_color}; border-radius: 12px;"></div>
        """,
        unsafe_allow_html=True,
    )
