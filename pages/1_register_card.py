import streamlit as st
import pandas as pd
import os

st.title("📇 카드 등록")

# 파일 경로
DATA_PATH = "data/profiles.csv"

with st.form("register_form"):
    name = st.text_input("이름")
    job = st.text_input("직무")
    years = st.slider("연차", 1, 20, 3)
    description = st.text_area("하는 일 (간단히)")
    interests = st.text_input("관심사 (쉼표로 구분)")
    available_time = st.text_input("가능 시간 예: 월/수 14:00~17:00")
    submitted = st.form_submit_button("카드 등록하기")

if submitted:
    new_data = pd.DataFrame([{
        "name": name,
        "job_title": job,
        "years": years,
        "description": description,
        "interests": interests,
        "available_time": available_time
    }])
    
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data
    
    df.to_csv(DATA_PATH, index=False)
    st.success("카드가 성공적으로 등록되었습니다! 🙌")