import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Koffee Chat", page_icon="☕")

st.title("☕ Koffee Chat - 사내 커리어 매칭")
st.write("고민을 입력하면, 당신에게 어울리는 사람을 추천해드립니다.")

# 사용자 입력
user_input = st.text_input("당신의 고민을 입력해주세요:")

# 추천자 데이터 로드
@st.cache_data
def load_profiles():
    df = pd.read_csv("data/profiles.csv")
    return df

df_profiles = load_profiles()

# 카드 HTML 템플릿 함수
def render_profile_card(row):
    return f"""
    <div style='background-color: #002244; padding: 20px; border-radius: 16px; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.2); margin-bottom: 20px;'>
        <h3>👤 {row['name']} ({row['job_title']} {row['years']}년차)</h3>
        <p>💬 {row['description']}</p>
        <p>🔖 #{row['interests'].replace(',', ' #')}</p>
        <p style='opacity: 0.8;'>🕒 가능 시간: {row['available_time']}</p>
    </div>
    """

# 추천 버튼 누르면 추천자 카드 출력
if st.button("추천 받기"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요 🙏")
    else:
        st.subheader("✨ 이런 분들과 이야기 나눠보세요:")

        # 랜덤 3명 추출 (SBERT 연결 전)
        sample_profiles = df_profiles.sample(3)

        for _, row in sample_profiles.iterrows():
            st.markdown(render_profile_card(row), unsafe_allow_html=True)