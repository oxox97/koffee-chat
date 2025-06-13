def generate_cards_html(profiles):
    colors = [
        ("#002244", "#004488"),  # navy
        ("#6A1B9A", "#AB47BC"),  # purple
        ("#00695C", "#26A69A"),  # teal
    ]
    card_html = "<div class='card-container'>"

    for i, profile in enumerate(profiles):
        grad1, grad2 = colors[i % len(colors)]
        similarity = profile.get("similarity", 0)
        card_html += f"""
        <div class="card">
            <div class="card-inner">
                <div class="card-header" style="background: linear-gradient(135deg, {grad1}, {grad2});">
                    <span class="icon">👤</span>
                </div>
                <div class="card-body">
                    <h3>{profile['name']}<br/>({profile['job_title']} {profile['years']}년차)</h3>
                    <p>{profile['description']}</p>
                    <div class="tag" style="background: linear-gradient(135deg, {grad1}, {grad2});">#{profile['interests'].split(",")[0]}</div>
                    <div class="similarity">유사도: {similarity:.2f}</div>
                </div>
            </div>
        </div>
        """

    card_html += "</div>"

    style = """
    <style>
    .card-container {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        gap: 30px;
        margin-top: 30px;
    }
    .card {
        background: white;
        border-radius: 24px;
        padding: 4px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        width: 300px;
        display: flex;
        flex-direction: column;
    }
    .card-inner {
        border-radius: 20px;
        overflow: hidden;
        background: white;
        font-family: sans-serif;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .card-header {
        height: 200px;
        position: relative;
        border-bottom-left-radius: 100% 20%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .icon {
        font-size: 36px;
        color: white;
    }
    .card-body {
        padding: 20px;
        text-align: center;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-body h3 {
        margin: 10px 0;
        font-size: 18px;
        color: #333;
    }
    .card-body p {
        font-size: 14px;
        color: #777;
        margin-bottom: 15px;
        flex-grow: 1;
    }
    .tag {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .similarity {
        font-size: 13px;
        color: #555;
        font-weight: bold;
    }
    </style>
    """

    return style + card_html
