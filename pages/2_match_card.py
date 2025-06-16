import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from modules.matching import recommend_profiles
from modules.ui import generate_cards_html

st.title("🔍 카드 매칭")

with st.form("match_form"):
    user_input = st.text_input("당신의 고민을 입력해주세요:")
    submitted = st.form_submit_button("추천 받기")

if submitted:
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요 🙏")
    else:
        st.subheader("✨ 이런 분들과 이야기 나눠보세요:")

        df_profiles = pd.read_csv("data/profiles.csv")
        recommended = recommend_profiles(user_input, df_profiles, top_k=3)
        card_html = generate_cards_html(recommended)
        components.html(card_html, height=1800, scrolling=True)