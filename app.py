# app.py

import streamlit as st

st.set_page_config(page_title="Koffee Chat", page_icon="☕")

st.title("☕ Koffee Chat - 사내 커리어 매칭")
st.write("고민을 입력하면, 당신에게 어울리는 사람을 추천해드립니다.")

# 사용자 입력
user_input = st.text_input("당신의 고민을 입력해주세요:")

if st.button("추천 받기"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요 🙏")
    else:
        st.success("추천 결과를 확인해보세요!")

        # 더미 카드 UI
        st.markdown("""
        <div style='background-color: #002244; padding: 20px; border-radius: 16px; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.2);'>
            <h3>👨‍💻 김개발 (백엔드 3년차)</h3>
            <p>#커리어전환 #디자인이해</p>
            <p style='opacity: 0.8;'>가능 시간: 월/수/금 14:00~17:00</p>
        </div>
        """, unsafe_allow_html=True)