import streamlit as st
import pandas as pd
import joblib

# 加载模型
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('extra_trees_model.pkl')

# 应用标题
st.title("Prediction of Fluoride Ion Removal Rate using Amorphous Magnesium Oxide Hollow Spheres")

# 添加使用说明
st.markdown("""
### Instructions
This application is used to predict the removal rate of fluoride ions using amorphous magnesium oxide hollow spheres.  
Please enter the relevant parameters in the input box on the left, and then click the "Prediction" button to obtain the predicted removal rate results.
""")

# 调整左侧边距
st.markdown(
    """
    <style>
    .streamlit-container {
        margin-left: 10px; /* 调整左侧边距 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 输入参数
st.sidebar.header('Input Parameters')

def user_input_features():
    ph = st.sidebar.number_input('pH', min_value=2.0, max_value=13.0, value=2.0)
    time = st.sidebar.number_input('Time (min)', min_value=0.0, max_value=500.0, value=1.0)
    c_mgo = st.sidebar.number_input('C_MgO (g/L)', min_value=0.0, max_value=2.0, value=0.1)
    c_f = st.sidebar.number_input('C_F (mg/L)', min_value=0.0, max_value=100.0, value=10.0)
    no3 = st.sidebar.number_input('NO3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    br = st.sidebar.number_input('Br- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    cl = st.sidebar.number_input('Cl- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    so4 = st.sidebar.number_input('(SO4)2- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    hco3 = st.sidebar.number_input('HCO3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    co3 = st.sidebar.number_input('(CO3)2- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)
    po4 = st.sidebar.number_input('(PO4)3- (mg/L)', min_value=0.0, max_value=900.0, value=0.0)

    data = {
        'pH': ph,
        'time': time,
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

# 获取输入数据
df = user_input_features()

# 显示输入参数
st.subheader('Input Parameters')

# 使用列来显示输入参数
col1, col2 = st.columns(2)
with col1:
    st.write("**pH:**", df['pH'].values[0])
    st.write("**Time (min):**", df['time'].values[0])
    st.write("**C_MgO (g/L):**", df['C_MgO'].values[0])
    st.write("**C_F (mg/L):**", df['C_F'].values[0])
    st.write("**NO3- (mg/L):**", df['NO3-'].values[0])
with col2:
    st.write("**Br- (mg/L):**", df['Br-'].values[0])
    st.write("**Cl- (mg/L):**", df['Cl-'].values[0])
    st.write("**(SO4)2- (mg/L):**", df['(SO4)2-'].values[0])
    st.write("**HCO3- (mg/L):**", df['HCO3-'].values[0])
    st.write("**(CO3)2- (mg/L):**", df['(CO3)2-'].values[0])
    st.write("**(PO4)3- (mg/L):**", df['(PO4)3-'].values[0])

# 加载模型并进行预测
model = load_model()

# 使用模型进行预测
if st.sidebar.button("Prediction"):
    prediction = model.predict(df)[0]
    st.write(f"**Predicted Removal Rate**: {prediction:.2f}%")
    
    # 根据预测值设置进度条
    percentage = prediction / 100  # 将百分比转为小数
    st.markdown(f"**Removal Rate**:")
    
    # 渐变色进度条
    progress_color = f"linear-gradient(90deg, #ff4b4b {percentage*100}%, #d3d3d3 {percentage*100}%)"
    st.markdown(
        f"""
        <div style="width: 100%; height: 24px; background: {progress_color}; border-radius: 12px;"></div>
        """,
        unsafe_allow_html=True,
    )
