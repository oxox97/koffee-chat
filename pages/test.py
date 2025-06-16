import streamlit as st

st.markdown("""
<div class="card">
  <h3>👨‍💻 김개발 (백엔드 3년차)</h3>
  <p>#커리어전환 #디자인이해</p>
</div>

<style>
.card {
  background: linear-gradient(135deg, #000000, #000080);
  border-radius: 16px;
  padding: 20px;
  margin: 10px 0;
  box-shadow: 0 6px 15px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 123, 255, 0.4);
  background: linear-gradient(135deg, #bbdefb, #e3f2fd);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h3>👩‍💻 박프론 (프론트엔드)</h3>
      <p>#멘토링 #리액트</p>
    </div>
    <div class="flip-card-back">
      <h4>커피챗 가능: 화/목 13~15시</h4>
      <p>사내 메신저로 연락해보세요!</p>
    </div>
  </div>
</div>

<style>
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 180px;
  perspective: 1000px;
}
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 16px;
  padding: 20px;
}
.flip-card-front {
  background-color: #fff;
  box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}
.flip-card-back {
  background-color: #e1f5fe;
  color: #000;
  transform: rotateY(180deg);
  box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glow-card">
  <h3>✨ 최데브 (백엔드 5년차)</h3>
  <p>#사내이동 #마이크로서비스</p>
</div>

<style>
.glow-card {
  border: 2px solid transparent;
  padding: 20px;
  margin: 10px 0;
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 0 5px rgba(0,0,0,0.1);
  position: relative;
  transition: all 0.3s ease;
}
.glow-card:hover {
  border: 2px solid #40c4ff;
  box-shadow: 0 0 20px #40c4ff;
}
.glow-card h3 {
  animation: glow-text 1.5s ease-in-out infinite alternate;
}
@keyframes glow-text {
  from {
    text-shadow: 0 0 5px #90caf9, 0 0 10px #64b5f6;
  }
  to {
    text-shadow: 0 0 15px #40c4ff, 0 0 25px #29b6f6;
  }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
  <h3>👨‍💻 김개발 (백엔드 3년차)</h3>
  <p>#커리어전환 #디자인이해</p>
</div>

<style>
.card {
  background: linear-gradient(135deg, #000000, #000080);
  border-radius: 16px;
  padding: 20px;
  margin: 10px 0;
  color: white;
  box-shadow: 0 6px 15px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(120deg, rgba(255,255,255,0.2) 0%, transparent 60%);
  transform: rotate(25deg);
  transition: all 0.5s ease;
  pointer-events: none;
}

.card:hover::before {
  top: 0%;
  left: 0%;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 123, 255, 0.4);
}
</style>
""", unsafe_allow_html=True)

import streamlit as st
import streamlit.components.v1 as components

components.html("""
<div class="card">
  <h3>👨‍💻 김개발 (백엔드 3년차)</h3>
  <p>#커리어전환 #디자인이해</p>
</div>

<style>
.card {
  position: relative;
  background: linear-gradient(135deg, #000000, #000080);
  color: white;
  border-radius: 16px;
  padding: 20px;
  margin: 10px;
  box-shadow: 0 6px 15px rgba(0,0,0,0.2);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card::after {
  content: '';
  position: absolute;
  top: var(--mouse-y, 50%);
  left: var(--mouse-x, 50%);
  width: 200px;
  height: 200px;
  background: radial-gradient(circle at center, rgba(255,255,255,0.3) 0%, transparent 80%);
  transform: translate(-50%, -50%);
  border-radius: 50%;
  pointer-events: none;
  transition: top 0.1s ease, left 0.1s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 123, 255, 0.4);
}
</style>

<script>
const card = document.querySelector('.card');
card.addEventListener('mousemove', e => {
  const rect = card.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  card.style.setProperty('--mouse-x', `${x}px`);
  card.style.setProperty('--mouse-y', `${y}px`);
});
</script>
""", height=200)

import streamlit as st
import streamlit.components.v1 as components

components.html("""
<div class="card-container">
  <div class="card">
    <div class="card-header orange">
      <span class="icon">💻</span>
    </div>
    <div class="card-body">
      <h3>TITLE</h3>
      <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
      <div class="tag orange">CODE</div>
    </div>
  </div>
</div>

<style>
.card-container {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.card {
  width: 250px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
  background: white;
  font-family: sans-serif;
}

.card-header {
  height: 100px;
  position: relative;
  border-bottom-left-radius: 100% 60%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-header.orange {
  background: linear-gradient(135deg, #ff6a00, #ffb347);
}

.icon {
  font-size: 36px;
  color: white;
}

.card-body {
  padding: 20px;
  text-align: center;
}

.card-body h3 {
  margin: 10px 0;
  font-size: 20px;
  color: #333;
}

.card-body p {
  font-size: 14px;
  color: #777;
  margin-bottom: 15px;
}

.tag {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: bold;
  color: white;
}

.tag.orange {
  background: linear-gradient(135deg, #ff6a00, #ffb347);
}
</style>
""", height=400)

import streamlit as st
import streamlit.components.v1 as components

components.html("""
<div class="card-container">
  <div class="card">
    <div class="card-inner">
      <div class="card-header orange">
        <span class="icon">💻</span>
      </div>
      <div class="card-body">
        <h3>TITLE</h3>
        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
        <div class="tag orange">CODE</div>
      </div>
    </div>
  </div>
</div>

<style>
.card-container {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.card {
  background: white;  /* 겉 배경 흰색 */
  border-radius: 24px;
  padding: 4px; /* 테두리처럼 보이도록 padding */
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.card-inner {
  border-radius: 20px;
  overflow: hidden;
  background: white;
  width: 250px;
  font-family: sans-serif;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.card-header {
  height: 300px;
  position: relative;
  border-bottom-left-radius: 100% 30%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-header.orange {
  background: linear-gradient(135deg, #ff6a00, #ffb347);
}

.icon {
  font-size: 36px;
  color: white;
}

.card-body {
  padding: 20px;
  text-align: center;
}

.card-body h3 {
  margin: 10px 0;
  font-size: 20px;
  color: #333;
}

.card-body p {
  font-size: 14px;
  color: #777;
  margin-bottom: 15px;
}

.tag {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: bold;
  color: white;
}

.tag.orange {
  background: linear-gradient(135deg, #ff6a00, #ffb347);
}
</style>
""", height=1600)
