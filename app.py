import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor

# 初始化并训练 CatBoost 模型
catboost_model = CatBoostRegressor(
    verbose=0,
    bagging_temperature=0.49515144330039407,
    depth=8,
    l2_leaf_reg=2.193560575993452,
    learning_rate=0.15327752053056587,
    subsample=0.841204717774464,
    iterations=1000,
    random_seed=42
)

# 假设你已经用 dropset 数据集训练了模型
# 这里可以添加代码读取数据集并训练模型
# df = pd.read_csv('dropset.csv')
# X = df.drop('Removal_rate', axis=1)
# y = df['Removal_rate']
# catboost_model.fit(X, y)

# Streamlit 用户界面
st.title("Removal Rate Prediction App")
st.write("使用 CatBoost 模型预测 Removal Rate")

# 用户输入特征
pH = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
time = st.number_input("Time (h)", min_value=0.0, value=1.0)
C_MgO = st.number_input("C_MgO (mg/L)", min_value=0.0, value=0.0)
C_F = st.number_input("C_F (mg/L)", min_value=0.0, value=0.0)
NO3_ = st.number_input("NO3- (mg/L)", min_value=0.0, value=0.0)
Br_ = st.number_input("Br- (mg/L)", min_value=0.0, value=0.0)
Cl_ = st.number_input("Cl- (mg/L)", min_value=0.0, value=0.0)
SO4_2 = st.number_input("SO4 (mg/L)", min_value=0.0, value=0.0)
HCO3_ = st.number_input("HCO3- (mg/L)", min_value=0.0, value=0.0)
CO3_2 = st.number_input("CO3 (mg/L)", min_value=0.0, value=0.0)
PO4_3 = st.number_input("PO4 (mg/L)", min_value=0.0, value=0.0)

# 按钮触发预测
if st.button("预测 Removal Rate"):
    # 将输入特征组织成 DataFrame
    input_data = pd.DataFrame({
        'pH': [pH],
        'time': [time],
        'C_MgO': [C_MgO],
        'C_F': [C_F],
        'NO3-': [NO3_],
        'Br-': [Br_],
        'Cl-': [Cl_],
        '(SO4)2-': [SO4_2],
        'HCO3-': [HCO3_],
        '(CO3)2-': [CO3_2],
        '(PO4)3-': [PO4_3],
    })

    # 进行预测
    prediction = catboost_model.predict(input_data)
    st.success(f"预测的 Removal Rate: {prediction[0]:.2f}")
