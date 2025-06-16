import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("💬 커리어 고민을 자유롭게 이야기해주세요")

# OpenAI client 구성 (v1 방식)
client = OpenAI(api_key=api_key)  
# client = openai.OpenAI(api_key=openai.api_key)

# 초기 메시지
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 커리어 고민을 함께 정리해드릴게요 🙌"}
    ]

# 채팅 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 입력 받기
user_input = st.chat_input("고민을 입력해주세요")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("답변을 생성 중입니다..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "너는 친절한 커리어 상담사야. 사용자의 고민을 잘 듣고 핵심을 요약하거나 질문을 이어가줘."},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
