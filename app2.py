import streamlit as st
import random
import pandas as pd

# 제목
st.title("💊SafePrenatal💊 \n (임산부 약물 안전 도우미) ")
st.caption("성분 검색과 퀴즈를 통해 임부금기 의약품에 대해 쉽고 정확하게 학습하세요.")


# 엑셀 파일 불러오기
# 데이터 불러오기
df = pd.read_excel("임부금기 성분리스트_250401.xlsx", sheet_name="임부금기", skiprows=1)
df = df.rename(columns={
    df.columns[1]: "성분명",
    df.columns[2]: "임부금기등급",
    df.columns[3]: "비고",
    df.columns[4]: "허가사항"
})

st.title("✅ 임부금기 성분 체크 리스트")

# 1. 성분명 리스트에서 다중 선택
selected_ingredients = st.multiselect(
    "확인하고 싶은 성분을 선택하세요",
    options=df["성분명"].dropna().unique().tolist(),
    default=[]
)

# 2. 선택된 성분 출력
if selected_ingredients:
    results = df[df["성분명"].isin(selected_ingredients)]
    st.success(f"🔎 {len(results)}건 선택됨")
    st.dataframe(results[["성분명", "임부금기등급", "허가사항"]])
else:
    st.info("👆 위에서 성분을 하나 이상 선택해 주세요.")

# 게임 데이터 정의
sim_data_full = [
  { "q": "[임신 초기] 친구가 Abiraterone이 들어간 건강기능식을 선물했어요. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 중기] 의사가 감기 증상 완화를 위해 Abacavir를 권유했어요. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 말기] 수면장애로 Zolpidem을 복용하려 합니다. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 중기] 의사가 철분제 외에 Hydroxyurea를 함께 처방했어요. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 초기] 고용량 Vitamin A가 함유된 보조제를 선물 받았어요. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 말기] 친구가 준 와인 한잔 마셔도 괜찮을까요?", "a": "아니요" },
  { "q": "[임신 초기] 피부 트러블이 심해져 Isotretinoin(경구형 비타민 A 유도체)을 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 중기] 친정에서 준 한약에 효소가 들어 있다는데 복용해도 될까요?", "a": "네" },
  { "q": "[임신 초기] 입덧이 심해서 Ginger(생강) 캡슐을 복용해도 될까요?", "a": "네" },
  { "q": "[임신 중기] 철분 보충을 위해 의사가 Ferrous Sulfate(황산철)을 처방했어요. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 초기] Folic Acid(엽산) 보충제를 복용하려 합니다. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 말기] 의사가 진통 시 Acetaminophen(해열진통제)을 권했습니다. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 중기] 지인이 준 생약제인 감초 추출물이 들어간 보조제를 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 초기] 간헐적인 속쓰림에 알루미늄 제산제를 복용하려고 합니다. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 말기] 코막힘 해소를 위해 pseudoephedrine 성분을 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 중기] 변비 완화를 위해 의사가 Lactulose를 권했습니다. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 초기] 유산 방지를 위해 의사가 Dydrogesterone(황체호르몬)을 처방했어요. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 중기] 의사의 권고 없이 Ibuprofen을 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 말기] 피로 회복을 위해 타우린 음료를 마셔도 될까요?", "a": "아니요" },
  { "q": "[임신 초기] 입덧이 심해 메스꺼움을 완화시키는 Doxylamine 성분 약물을 복용해도 될까요?", "a": "네" },
  { "q": "[임신 말기] 출산 전 감기 증상으로 Clonidine을 복용하려 합니다. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 초기] 비타민 C 500mg 보충제를 매일 먹고 있어요. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 중기] 과일 주스를 많이 마시는 게 태아에게 좋은가요?", "a": "네" },
  { "q": "[임신 말기] 복통 완화를 위해 의사 처방 없이 Belladonna를 복용하려 합니다. 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 중기] 피부 건조로 처방받은 Urea 크림을 바르려고 합니다. 사용해도 될까요?", "a": "네" },
  { "q": "[임신 초기] 과도한 오메가3 보충제를 섭취해도 될까요?", "a": "아니요" },
  { "q": "[임신 말기] 소화불량에 제산제와 소화제를 병용하려 합니다. 복용해도 될까요?", "a": "네" },
  { "q": "[임신 중기] 불안감 때문에 Valproic Acid를 처방 없이 복용해도 될까요?", "a": "아니요" },
  { "q": "[임신 초기] 평소 복용하던 종합비타민을 계속 먹어도 될까요?", "a": "네" }
];


ox_data = [
    {"q": "Abiraterone은 임산부 금기 의약품이다.", "a": "O"},
    {"q": "Abacavir는 1등급 금기 약물이다.", "a": "X"},
    {"q": "(Micronized)Progesterone은 임산부가 복용해도 안전하다.", "a": "X"}
]

grade_data = [
    {"q": "Abiraterone", "a": "1등급"},
    {"q": "Abacavir", "a": "2등급"},
    {"q": "3'-Deoxy-3'-Fluorothymidine(18F)", "a": "2등급"}
]

st.set_page_config(page_title="임산부 금기 의약품 게임", layout="centered")

st.title("💊 임산부 금기 의약품 게임")

menu = st.radio("게임을 선택하세요", ["🧪 상황 시뮬레이션", "⭕ OX 퀴즈", "📊 등급 분류 게임"])

# 상황 시뮬레이션 게임
# 상황 시뮬레이션 게임
if menu == "🧪 상황 시뮬레이션":
    st.header("🧪 상황 시뮬레이션 게임")

    if "sim_index" not in st.session_state:
        st.session_state.sim_questions = random.sample(sim_data_full, 5)
        st.session_state.sim_index = 0
        st.session_state.sim_score = 0
        st.session_state.sim_feedback = ""

    if st.session_state.sim_index < len(st.session_state.sim_questions):
        q = st.session_state.sim_questions[st.session_state.sim_index]
        st.write(q["q"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("네"):
                st.session_state.user_ans = "네"
        with col2:
            if st.button("아니요"):
                st.session_state.user_ans = "아니요"

        if "user_ans" in st.session_state:
            if st.session_state.user_ans == q["a"]:
                st.session_state.sim_score += 1
                st.session_state.sim_feedback = "✅ 정답입니다!"
            else:
                st.session_state.sim_feedback = f"❌ 오답입니다! 정답은 {q['a']}입니다."

            del st.session_state.user_ans
            st.session_state.sim_index += 1
            st.rerun()

    else:
        st.info(f"🎯 최종 점수: {st.session_state.sim_score} / {len(st.session_state.sim_questions)}")
        if st.button("다시 시작"):
            for key in ["sim_index", "sim_questions", "sim_score", "sim_feedback"]:
                if key in st.session_state:
                    del st.session_state[key]

    if "sim_feedback" in st.session_state and st.session_state.sim_feedback:
        st.markdown(f"**{st.session_state.sim_feedback}**")
        st.session_state.sim_feedback = ""  # 다음 질문엔 초기화

# OX 퀴즈
elif menu == "⭕ OX 퀴즈":
    st.header("⭕ OX 퀴즈")

    if "ox_index" not in st.session_state:
        st.session_state.ox_index = 0
        st.session_state.ox_score = 0

    if st.session_state.ox_index < len(ox_data):
        q = ox_data[st.session_state.ox_index]
        st.write(q["q"])
        if st.button("⭕ O"):
            user_ans = "O"
        elif st.button("❌ X"):
            user_ans = "X"
        else:
            user_ans = None

        if user_ans:
            if user_ans == q["a"]:
                st.success("✅ 정답입니다!")
                st.session_state.ox_score += 1
            else:
                st.error("❌ 오답입니다!")
            st.session_state.ox_index += 1
            st.rerun()
    else:
        st.info(f"🎯 최종 점수: {st.session_state.ox_score} / {len(ox_data)}")
        if st.button("다시 시작"):
            del st.session_state.ox_index

# 등급 분류 게임
elif menu == "📊 등급 분류 게임":
    st.header("📊 등급 분류 게임")

    if "grade_index" not in st.session_state:
        st.session_state.grade_index = 0
        st.session_state.grade_score = 0

    if st.session_state.grade_index < len(grade_data):
        q = grade_data[st.session_state.grade_index]
        st.write(f"{q['q']}의 임부금기 등급은?")
        if st.button("1등급"):
            user_ans = "1등급"
        elif st.button("2등급"):
            user_ans = "2등급"
        else:
            user_ans = None

        if user_ans:
            if user_ans == q["a"]:
                st.success("✅ 정답입니다!")
                st.session_state.grade_score += 1
            else:
                st.error("❌ 오답입니다!")
            st.session_state.grade_index += 1
            st.rerun()
    else:
        st.info(f"🎯 최종 점수: {st.session_state.grade_score} / {len(grade_data)}")
        if st.button("다시 시작"):
            del st.session_state.grade_index
