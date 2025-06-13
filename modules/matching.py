from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import asyncio

# 모델 로딩 (최초 1회만)
_model = None

def load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

# 이벤트 루프 강제로 설정 (Streamlit + PyTorch 충돌 방지용)
def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

# 프로필 추천 함수
def recommend_profiles(user_input, df_profiles, top_k=3):
    # 모델 및 이벤트 루프 준비
    model = load_model()
    ensure_event_loop()

    # 텍스트 구성: description + interests
    df_profiles["text"] = df_profiles["description"].fillna("") + " " + df_profiles["interests"].fillna("")
    texts = df_profiles["text"].tolist()

    # 임베딩 생성
    profile_embeddings = model.encode(texts, convert_to_tensor=True)
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    # 유사도 계산
    cos_scores = util.cos_sim(user_embedding, profile_embeddings)[0]
    top_results = torch.topk(cos_scores, k=top_k)

    # 결과 정리
    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        row = df_profiles.iloc[idx.item()]
        results.append({
            "name": row.get("name", ""),
            "job_title": row.get("job_title", ""),
            "years": row.get("years", ""),
            "description": row.get("description", ""),
            "interests": row.get("interests", ""),
            "available_time": row.get("available_time", ""),
            "similarity": round(score.item(), 3)
        })

    return results
