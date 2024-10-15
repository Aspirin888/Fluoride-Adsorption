import streamlit as st
import pickle
import numpy as np

# 加载模型
with open('weighted_average_predict.pkl', 'rb') as file:
    model = pickle.load(file)

# 设置页面标题
st.title("无定形氧化镁空心球对氟离子的去除率预测")

# 左侧输入栏
st.sidebar.header("输入参数")

# 获取用户输入
time = st.sidebar.number_input("Time (min)", min_value=0, max_value=500, value=60, step=1)
CMgO = st.sidebar.number_input("CMgO (g/L)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
CF = st.sidebar.number_input("CF (mg/L)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
pH = st.sidebar.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
PO4 = st.sidebar.number_input("PO43- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
SO4 = st.sidebar.number_input("SO42- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
CO3 = st.sidebar.number_input("CO32- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
HCO3 = st.sidebar.number_input("HCO3- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
NO3 = st.sidebar.number_input("NO3- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
Cl = st.sidebar.number_input("Cl- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
Br = st.sidebar.number_input("Br- (mg/L)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)

# 将输入数据转换为数组
input_data = np.array([[time, CMgO, CF, pH, PO4, SO4, CO3, HCO3, NO3, Cl, Br]])

# 使用模型进行预测
if st.sidebar.button("预测"):
    prediction = model.predict(input_data)[0]
    
    # 显示预测的去除率
    st.write(f"**预测的去除率**: {prediction:.2f}%")
    
    # 计算进度条的进度（假设百分比最大为100）
    progress_value = int(prediction)
    
    # 显示进度条
    progress = st.progress(progress_value)
    
    # 渐变进度条颜色（通过插入自定义CSS）
    st.markdown(f"""
    <style>
    .stProgress > div > div > div > div {{
        background: linear-gradient(to right, #ff0000, #00ff00);
    }}
    </style>
    """, unsafe_allow_html=True)
