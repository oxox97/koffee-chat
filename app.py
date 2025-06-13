import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from modules.matching import recommend_profiles
from modules.ui import generate_cards_html  # 카드 HTML 함수 import

import os
os.environ["STREAMLIT_RUN_ON_SAVE"] = "false"

st.set_page_config(page_title="Koffee Chat", page_icon="☕")
st.title("☕ Koffee Chat - 사내 커리어 매칭")
st.write("고민을 입력하면, 당신에게 어울리는 사람을 추천해드립니다.")


# 추천 버튼 클릭 시
with st.form("koffee_form"):
    user_input = st.text_input(
        "당신의 고민을 입력해주세요:",
        placeholder="예: 디자이너인데 백엔드 개발을 배우고 싶어요"
    )
    submitted = st.form_submit_button("추천 받기")  # ⬅️ Enter로도 동작
    st.write(submitted)

if submitted:
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요 🙏")
    else:
        st.subheader("✨ 이런 분들과 이야기 나눠보세요:")
        df_profiles = pd.read_csv("data/profiles.csv")
        recommended = recommend_profiles(user_input, df_profiles, top_k=3)
        card_html = generate_cards_html(recommended)
        components.html(card_html, height=1800, scrolling=True)