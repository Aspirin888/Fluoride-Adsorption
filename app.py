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
    ph = st.sidebar.number_input('pH')
    time = st.sidebar.number_input('Time (min)')
    c_mgo = st.sidebar.number_input('C_MgO (g/L)')
    c_f = st.sidebar.number_input('C_F (mg/L)')
    no3 = st.sidebar.number_input('NO3- (mg/L)')
    br = st.sidebar.number_input('Br- (mg/L)')
    cl = st.sidebar.number_input('Cl- (mg/L)')
    so4 = st.sidebar.number_input('(SO4)2- (mg/L)')
    hco3 = st.sidebar.number_input('HCO3- (mg/L)')
    co3 = st.sidebar.number_input('(CO3)2- (mg/L)')
    po4 = st.sidebar.number_input('(PO4)3- (mg/L)')
   
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
