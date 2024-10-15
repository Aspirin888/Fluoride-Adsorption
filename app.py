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
