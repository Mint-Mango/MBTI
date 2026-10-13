import streamlit as st

# ─────────────────────────────────────────────
# 기본 설정
# ─────────────────────────────────────────────
st.set_page_config(page_title="MBTI 단짝 포켓몬 찾기", page_icon="🔍", layout="centered")

# 포켓몬 공식 일러스트 이미지 주소 (PokeAPI 공개 이미지 저장소)
IMG_URL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png"

# ─────────────────────────────────────────────
# 데이터: 유형별 단짝 포켓몬
# ─────────────────────────────────────────────
POKEMON = {
    "ISTJ": {"ko": "꼬부기", "en": "Squirtle", "no": 7, "type": ["물"],
             "feature": "단단한 등껍질 속에 몸을 숨기고, 입에서 물대포를 쏘아요.",
             "reason": ["단단한 등껍질처럼 책임감이 강하고 믿음직해요.",
                        "정해진 규칙과 약속을 차근차근 잘 지켜요.",
                        "말보다 행동으로 꾸준히 보여 주는 성실파예요."]},
    "ISFJ": {"ko": "럭키", "en": "Chansey", "no": 113, "type": ["노말"],
             "feature": "영양 가득한 알을 품고 다니며 다친 친구에게 나눠 줘요.",
             "reason": ["다친 친구를 정성껏 돌보는 따뜻한 마음을 가졌어요.",
                        "조용히 뒤에서 모두를 챙기는 든든한 친구예요.",
                        "작은 것까지 기억해 주는 세심함이 있어요."]},
    "INFJ": {"ko": "루카리오", "en": "Lucario", "no": 448, "type": ["격투", "강철"],
             "feature": "‘파동’을 느껴 상대의 마음과 생각을 읽어 낼 수 있어요.",
             "reason": ["상대의 마음을 읽어 내는 깊은 통찰력이 있어요.",
                        "옳다고 믿는 일에는 끝까지 흔들리지 않아요.",
                        "조용하지만 마음속에 큰 꿈을 품고 있어요."]},
    "INTJ": {"ko": "뮤츠", "en": "Mewtwo", "no": 150, "type": ["에스퍼"],
             "feature": "아주 뛰어난 두뇌와 강한 초능력을 가진 전설의 포켓몬이에요.",
             "reason": ["뛰어난 두뇌로 멀리 앞을 내다보며 계획을 세워요.",
                        "혼자 생각하는 시간을 좋아하는 독립적인 성격이에요.",
                        "목표가 생기면 누구보다 집중해서 이루어 내요."]},
    "ISTP": {"ko": "개굴닌자", "en": "Greninja", "no": 658, "type": ["물", "악"],
             "feature": "닌자처럼 재빠르게 움직이며 물로 만든 표창을 던져요.",
             "reason": ["말없이 빠르고 정확하게 문제를 해결해요.",
                        "위기의 순간에도 침착함을 잃지 않아요.",
                        "자유롭게 혼자 움직이는 것을 좋아해요."]},
    "ISFP": {"ko": "이상해씨", "en": "Bulbasaur", "no": 1, "type": ["풀", "독"],
             "feature": "등에 있는 씨앗이 햇빛을 받으며 조금씩 자라나요.",
             "reason": ["자연처럼 순하고 다정한 마음을 가졌어요.",
                        "다툼보다 평화로운 분위기를 좋아해요.",
                        "조용하지만 자기만의 감성이 뚜렷해요."]},
    "INFP": {"ko": "이브이", "en": "Eevee", "no": 133, "type": ["노말"],
             "feature": "환경에 따라 여러 모습으로 진화할 수 있는 신기한 포켓몬이에요.",
             "reason": ["무엇으로든 진화할 수 있는 무한한 가능성을 품었어요.",
                        "상상력이 풍부하고 마음이 아주 섬세해요.",
                        "자기만의 소중한 가치를 지키며 살아가요."]},
    "INTP": {"ko": "후딘", "en": "Alakazam", "no": 65, "type": ["에스퍼"],
             "feature": "두 개의 숟가락으로 초능력을 모으고, 지능이 매우 높아요.",
             "reason": ["엄청난 지능으로 궁금한 건 끝까지 파고들어요.",
                        "새로운 생각과 이론을 떠올리는 걸 좋아해요.",
                        "혼자 깊이 생각할 때 가장 빛나요."]},
    "ESTP": {"ko": "괴력몬", "en": "Machamp", "no": 68, "type": ["격투"],
             "feature": "네 개의 팔로 엄청난 힘을 내는 힘센 포켓몬이에요.",
             "reason": ["생각보다 몸이 먼저 움직이는 행동파예요.",
                        "도전과 모험을 두려워하지 않는 에너지가 넘쳐요.",
                        "현장에서 바로바로 문제를 해결해요."]},
    "ESFP": {"ko": "푸린", "en": "Jigglypuff", "no": 39, "type": ["노말", "페어리"],
             "feature": "동그란 눈으로 바라보며 듣는 이를 잠들게 하는 노래를 불러요.",
             "reason": ["노래하고 무대에 서는 걸 정말 좋아해요.",
                        "어디서나 분위기를 밝게 만드는 인기 스타예요.",
                        "지금 이 순간을 즐겁게 사는 법을 알아요."]},
    "ENFP": {"ko": "피카츄", "en": "Pikachu", "no": 25, "type": ["전기"],
             "feature": "볼에 있는 전기 주머니에서 찌릿찌릿 전기를 만들어요.",
             "reason": ["번쩍이는 전기처럼 밝은 에너지가 가득해요.",
                        "누구와도 금방 친해지는 친화력 최고예요.",
                        "호기심이 많아 새로운 모험을 사랑해요."]},
    "ENTP": {"ko": "팬텀", "en": "Gengar", "no": 94, "type": ["고스트", "독"],
             "feature": "그림자 속에 숨어 장난치는 것을 좋아하는 유령 포켓몬이에요.",
             "reason": ["장난기 많고 기발한 아이디어가 끊이지 않아요.",
                        "남들이 생각 못 한 방법을 찾아내는 재주가 있어요.",
                        "토론과 말장난을 즐기는 재치꾼이에요."]},
    "ESTJ": {"ko": "거북왕", "en": "Blastoise", "no": 9, "type": ["물"],
             "feature": "등껍질의 대포에서 강력한 물줄기를 발사해요.",
             "reason": ["강한 리더십으로 모두를 이끄는 대장 스타일이에요.",
                        "계획을 세우고 체계적으로 일을 처리해요.",
                        "맡은 일은 확실하게 끝내는 실천가예요."]},
    "ESFJ": {"ko": "해피너스", "en": "Blissey", "no": 242, "type": ["노말"],
             "feature": "몸의 털로 상대의 기분을 느끼고, 슬픈 이를 달래 줘요.",
             "reason": ["주변 사람들을 행복하게 해 주는 걸 좋아해요.",
                        "모두가 함께 어울리도록 다정하게 챙겨요.",
                        "친절하고 배려심이 넘치는 분위기 메이커예요."]},
    "ENFJ": {"ko": "망나뇽", "en": "Dragonite", "no": 149, "type": ["드래곤", "비행"],
             "feature": "덩치는 크지만 마음씨가 착해 바다에서 길 잃은 이를 도와줘요.",
             "reason": ["크고 강하지만 마음씨가 아주 따뜻해요.",
                        "어려움에 빠진 친구를 먼저 도와주러 가요.",
                        "사람들을 격려하고 하나로 모으는 힘이 있어요."]},
    "ENTJ": {"ko": "리자몽", "en": "Charizard", "no": 6, "type": ["불꽃", "비행"],
             "feature": "하늘을 날며 뜨거운 불꽃을 내뿜는 강한 포켓몬이에요.",
             "reason": ["뜨거운 불꽃처럼 열정과 자신감이 넘쳐요.",
                        "목표를 정하면 거침없이 앞으로 나아가요.",
                        "타고난 리더로 팀을 승리로 이끌어요."]},
}

# 타입별 배지 색
TYPE_COLOR = {
    "노말": "#a8a77a", "불꽃": "#ee8130", "물": "#6390f0", "전기": "#e6b800",
    "풀": "#7ac74c", "얼음": "#96d9d6", "격투": "#c22e28", "독": "#a33ea1",
    "땅": "#e2bf65", "비행": "#a98ff3", "에스퍼": "#f95587", "벌레": "#a6b91a",
    "바위": "#b6a136", "고스트": "#735797", "드래곤": "#6f35fc", "악": "#705746",
    "강철": "#b7b7ce", "페어리": "#d685ad",
}

ORDER = ["ISTJ", "ISFJ", "INFJ", "INTJ",
         "ISTP", "ISFP", "INFP", "INTP",
         "ESTP", "ESFP", "ENFP", "ENTP",
         "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

# ─────────────────────────────────────────────
# 디자인 (크림·노란색 톤, 큰 글씨)
# ─────────────────────────────────────────────
st.markdown("""
<style>
.stApp { background: #fff8e7; }
html, body, [class*="css"], .stMarkdown, p, li {
    font-family: "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif;
    color: #5d4037;
}
.block-container { max-width: 760px; padding-top: 2rem; }

.title { text-align: center; font-size: 44px; font-weight: 800; color: #5d4037; margin-bottom: 0; }
.subtitle { text-align: center; font-size: 21px; color: #8d6e63; margin-bottom: 24px; }
.section-title { text-align: center; font-size: 26px; font-weight: 700; margin: 10px 0 14px; }

/* MBTI 버튼 */
div.stButton > button {
    width: 100%;
    background: #ffd54f;
    color: #5d4037;
    border: none;
    border-radius: 18px;
    padding: 14px 0;
    box-shadow: 0 5px 0 #f9b81b;
    transition: transform 0.1s;
}
div.stButton > button p { font-size: 24px !important; font-weight: 800; }
div.stButton > button:hover { background: #ffe082; color: #5d4037; border: none; }
div.stButton > button:active { transform: translateY(4px); box-shadow: 0 1px 0 #f9b81b; }
div.stButton > button:focus:not(:active) { color: #5d4037; border: 3px solid #5d4037; }

/* 결과 카드 */
.card {
    background: #ffffff;
    border: 5px solid #ffd54f;
    border-radius: 28px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 8px 0 #fdecc8;
    animation: pop 0.6s ease;
}
@keyframes pop {
    0%   { transform: scale(0.6); opacity: 0; }
    70%  { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(1); }
}
.congrats {
    font-size: 30px; font-weight: 800; color: #e65100;
    animation: shine 1.2s ease-in-out infinite alternate;
}
@keyframes shine { from { transform: scale(1); } to { transform: scale(1.08); } }
.mbti-badge {
    display: inline-block; background: #ffd54f; border-radius: 999px;
    padding: 4px 22px; font-size: 26px; font-weight: 800; letter-spacing: 2px; margin: 8px 0;
}
.poke-img { width: 260px; max-width: 80%; animation: float 2.5s ease-in-out infinite; }
@keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
.poke-name { font-size: 40px; font-weight: 800; margin: 6px 0 0; }
.poke-en { font-size: 24px; color: #8d6e63; }
.type-badge {
    display: inline-block; color: #fff; font-size: 20px; font-weight: 700;
    border-radius: 12px; padding: 4px 16px; margin: 8px 4px;
}
.box {
    background: #fff8e7; border-radius: 20px; padding: 16px 20px;
    text-align: left; font-size: 21px; margin-top: 14px; line-height: 1.7;
}
.box h4 { font-size: 23px; margin: 0 0 6px; color: #5d4037; }

/* 화면 위로 떨어지는 축하 이모지 */
.confetti { position: fixed; top: -60px; font-size: 34px; z-index: 9999;
            pointer-events: none; animation: fall linear forwards; }
@keyframes fall { to { transform: translateY(110vh) rotate(360deg); opacity: 0.2; } }

.footer { text-align: center; font-size: 16px; color: #8d6e63; margin-top: 28px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 상태 저장
# ─────────────────────────────────────────────
if "pick" not in st.session_state:
    st.session_state.pick = None
if "celebrate" not in st.session_state:
    st.session_state.celebrate = False


def choose(mbti):
    st.session_state.pick = mbti
    st.session_state.celebrate = True


def reset():
    st.session_state.pick = None
    st.session_state.celebrate = False


def confetti_html():
    """화면 위에서 떨어지는 축하 이모지를 만듭니다."""
    emojis = ["🎉", "⭐", "✨", "🎊", "💛", "🌟"]
    pieces = []
    for i in range(24):
        left = (i * 41) % 100
        delay = (i % 8) * 0.25
        dur = 2.6 + (i % 5) * 0.4
        pieces.append(
            f'<div class="confetti" style="left:{left}vw; animation-duration:{dur}s; '
            f'animation-delay:{delay}s;">{emojis[i % len(emojis)]}</div>'
        )
    return "".join(pieces)


# ─────────────────────────────────────────────
# 화면
# ─────────────────────────────────────────────
st.markdown('<p class="title">🔍 MBTI 단짝 포켓몬 찾기</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">나의 MBTI를 누르면 꼭 맞는 단짝 포켓몬을 찾아 줘요!</p>',
            unsafe_allow_html=True)

if st.session_state.pick is None:
    # 1단계: MBTI 고르기
    st.markdown('<p class="section-title">👇 나의 MBTI를 골라 주세요</p>', unsafe_allow_html=True)
    for row in range(4):
        cols = st.columns(4)
        for c in range(4):
            mbti = ORDER[row * 4 + c]
            cols[c].button(mbti, key=f"btn_{mbti}", on_click=choose, args=(mbti,),
                           use_container_width=True)
else:
    # 2단계: 결과 보기
    mbti = st.session_state.pick
    p = POKEMON[mbti]

    # 축하 효과 (처음 찾았을 때 한 번만)
    if st.session_state.celebrate:
        st.balloons()
        st.markdown(confetti_html(), unsafe_allow_html=True)
        st.session_state.celebrate = False

    types_html = "".join(
        f'<span class="type-badge" style="background:{TYPE_COLOR.get(t, "#999")}">{t}</span>'
        for t in p["type"]
    )
    reasons_html = "".join(f"<li>{r}</li>" for r in p["reason"])

    st.markdown(f"""
<div class="card">
  <div class="congrats">🎉 단짝 포켓몬을 찾았어요! 🎉</div>
  <div class="mbti-badge">{mbti}</div><br>
  <img class="poke-img" src="{IMG_URL.format(p['no'])}" alt="{p['ko']} 이미지">
  <div class="poke-name">{p['ko']}</div>
  <div class="poke-en">({p['en']})</div>
  <div>{types_html}</div>
  <div class="box">
    <h4>📖 특징</h4>
    {p['feature']}
  </div>
  <div class="box">
    <h4>💛 {mbti}와(과) 어울리는 이유</h4>
    <ul style="margin:0; padding-left:22px;">{reasons_html}</ul>
  </div>
</div>
""", unsafe_allow_html=True)

    st.write("")
    st.button("🔄 다시 고르기", on_click=reset, use_container_width=True)

st.markdown('<p class="footer">※ 재미로 보는 결과예요. 성격은 사람마다 다양하답니다! 😊<br>'
            '이미지 출처: PokeAPI (Pokémon © Nintendo / Creatures / GAME FREAK)</p>',
            unsafe_allow_html=True)
