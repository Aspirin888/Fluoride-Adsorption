import streamlit as st
import pandas as pd
import joblib

# 加载模型
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('extra_trees_model.pkl')

# 应用标题
st.title("无定形氧化镁空心球对氟离子的去除率预测")

# 输入参数
st.sidebar.header('输入参数')

def user_input_features():
    time = st.sidebar.number_input('Time (min)', min_value=0.0, max_value=10.0, value=0.0)
    cmgo = st.sidebar.number_input('CMgO (g/L)',min_value=0.0, max_value=10.0, value=0.0)
    cf = st.sidebar.number_input('CF (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    ph = st.sidebar.number_input('pH', min_value=0.0, max_value=14.0, step=0.1)
    po4 = st.sidebar.number_input('PO43- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    so4 = st.sidebar.number_input('SO42- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    co3 = st.sidebar.number_input('CO32- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    hco3 = st.sidebar.number_input('HCO3- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    no3 = st.sidebar.number_input('NO3- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    cl = st.sidebar.number_input('Cl- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)
    br = st.sidebar.number_input('Br- (mg/L)', min_value=0.0, max_value=10.0, value=0.0)

    CZn = st.sidebar.number_input('Time (min))', min_value=0.0, max_value=10.0, value=0.0)
    Calkali = st.sidebar.number_input('Calkali (mol/l)', min_value=0.0, max_value=10.0, value=0.0)
    Molar_ratio = st.sidebar.number_input('Molar_ratio (摩尔比)', min_value=0.0, max_value=10.0, value=0.0)
    Temperature = st.sidebar.number_input('Temperature (K)', min_value=0, max_value=100, value=25)
    Time = st.sidebar.number_input('Time (min)', min_value=0, max_value=800, value=10)
    
    data = {
        'Time': time,
        'C_MgO': cmgo,
        'C_F': cf,
        'pH': ph,
        'PO4': po4,
        'SO4': so4,
        'CO3': co3,
        'HCO3': hco3,
        'NO3': no3,
        'Cl': cl,
        'Br': br
    }
    features = pd.DataFrame(data, index=[0])
    return features

# 获取输入数据
input_df = user_input_features()

# 显示输入的参数
st.subheader('输入的参数')
st.write(input_df)

# 加载模型并进行预测
model = load_model()
prediction = model.predict(input_df)

# 显示预测结果
st.subheader('预测结果')
st.write(prediction)
