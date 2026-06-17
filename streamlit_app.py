import streamlit as st

# ====================================================
# 1. 페이지 기본 설정 및 타이틀
# ====================================================
st.set_page_config(page_title="초등 수학 단위 마스터", page_icon="📐", layout="centered")

st.title("🌈 눈으로 보고 조작하는 '수와 단위' 마스터!")
st.write("단순히 0의 개수만 외우지 말고, 숫자를 움직이며 자릿수의 비밀을 찾아보세요.")
st.write("---")

# ====================================================
# 2. 세션 상태(session_state) 초기화 확인
# ====================================================
if "user_name_input" not in st.session_state:
    st.session_state["user_name_input"] = ""

# ====================================================
# 3. 사용자 이름 입력창 (Key를 세션 상태와 연동)
# ====================================================
user_name = st.text_input(
    "👋 반갑습니다! 여러분의 이름을 입력해주세요:", 
    placeholder="예: 홍길동",
    key="user_name_input"
)

# 이름을 입력해야만 아래의 모든 학습 콘텐츠가 활성화됩니다.
if user_name:
    st.success(f"🎉 준비 완료! **{user_name}** 학생만을 위한 맞춤형 융합 수학 교실을 시작합니다.")
    
    # 상단 3단계 탭 구조 설정
    menu = st.tabs(["📋 [1단계] 실생활 속 단위 발견", "🔍 [2단계] 자릿수 추론 조작실", "✏️ [3단계] 최종 도전 퀴즈방"])
    
    # ----------------------------------------------------
    # [1단계: 실생활 속 단위 발견]
    # ----------------------------------------------------
    with menu[0]:
        st.header("📋 1단계: 우리 주변의 거리, 무게, 그리고 들이")
        st.write(f"**{user_name}**님, 우리 주변에서 다양한 단위가 쓰이는 상황을 먼저 살펴봐요!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("🛣️ 거리를 나타낼 때")
            st.info("🏃 **마라톤 코스의 길이**\n\n**42195 m**는 너무 길어서 보기가 힘들어요. 이럴 때 큰 단위인 **km**를 사용하면 편리합니다.")
            st.warning("⛰️ **한라산의 높이**\n\n한라산의 높이는 약 **1947 m**입니다. 이것을 km로 바꾸면 숫자가 어떻게 바뀔까요?")
            
        with col2:
            st.subheader("⚖️ 무게를 나타낼 때")
            st.info("🐋 **흰수염고래의 무게**\n\n지구상에서 가장 큰 동물은 약 **150000 kg**입니다. 단위를 **g**으로 쓰면 숫자가 너무 커지겠죠?")
            st.warning("🍎 **사과 한 개의 무게**\n\n보통 사과 한 개는 약 **250 g**입니다. 마트에서 사과를 많이 골라 담아 **kg** 단위가 되면 어떻게 변할지 알아봅시다.")

        with col3:
            st.subheader("🧪 들이를 나타낼 때")
            st.info("🐳 **욕조 가득 물의 양**\n\n우리가 매일 받는 **욕조 한 가득의 물**은 약 **300 L**나 됩니다. mL로 나타내면 자릿수가 어떻게 될까요?")
            st.warning("🍼 **우유 한 팩의 양**\n\n급식으로 먹는 작은 우유 한 팩은 **200 mL**입니다. 이것을 큰 단위인 **L**로 바꾸어 표현해 볼까요?")

    # ----------------------------------------------------
    # [2단계: 자릿수 추론 조작실]
    # ----------------------------------------------------
    with menu[1]:
        st.header("🔍 2단계: 손으로 움직이며 추론하는 조작실")
        st.write("슬라이더를 왼쪽, 오른쪽으로 직접 움직이면서 수의 크기와 단위가 어떻게 변하는지 눈으로 관찰해보세요.")
        
        unit_choice = st.selectbox("어떤 단위를 조작해볼까요?", ["거리 단위 (m ↔ km)", "무게 단위 (g ↔ kg)", "들이 단위 (mL ↔ L)"])
        
        if unit_choice == "거리 단위 (m ↔ km)":
            st.subheader("🛣️ 거리의 양방향 변화 관찰")
            km_slide = st.slider("👉 km 값을 움직이며 m 값이 어떻게 변하는지 보세요:", 0.0, 10.0, 3.5, step=0.5)
            m_calc = int(km_slide * 1000)
            st.metric(label="🗺️ 큰 단위 (km)", value=f"{km_slide} km")
            st.markdown("⬇️ **단위가 작아지면 수의 크기는 1000배가 됩니다! (소수점이 오른쪽으로 3칸 이동)**")
            st.metric(label="📍 작은 단위 (m)", value=f"{m_calc} m")
            st.write("---")
            st.markdown("💡 **반대로 생각하기 (m ➡️ km)**")
            st.write("작은 단위(m)에서 큰 단위(km)로 바뀔 때는 수의 크기가 **1/1000배**로 줄어듭니다. 소수점이 왼쪽으로 3칸 이동하는 규칙을 기억하세요!")

        elif unit_choice == "무게 단위 (g ↔ kg)":
            st.subheader("⚖️ 무게의 양방향 변화 관찰")
            kg_slide = st.slider("👉 kg 값을 움직이며 g 값이 어떻게 변하는지 보세요:", 0.0, 5.0, 1.2, step=0.1)
            g_calc = int(kg_slide * 1000)
            st.metric(label="🍏 큰 단위 (kg)", value=f"{kg_slide} kg")
            st.markdown("⬇️ **단위가 작아지면 수의 크기는 1000배가 됩니다! (자릿수가 위로 3칸 올라갑니다)**")
            st.metric(label="🍬 작은 단위 (g)", value=f"{g_calc} g")
            st.write("---")
            st.markdown("💡 **반대로 생각하기 (g ➡️ kg)**")
            st.write("작은 단위(g)에서 큰 단위(kg)로 바뀔 때는 수가 **1/1000배**로 작아지므로 자릿수가 아래로 3칸 내려가게 됩니다.")

        elif unit_choice == "들이 단위 (mL ↔ L)":
            st.subheader("🧪 들이의 양방향 변화 관찰")
            l_slide = st.slider("👉 L(리터) 값을 움직이며 mL(밀리리터) 값이 어떻게 변하는지 보세요:", 0.0, 5.0, 1.5, step=0.1)
            ml_calc = int(l_slide * 1000)
            st.metric(label="🥛 큰 단위 (L)", value=f"{l_slide} L")
            st.markdown("⬇️ **단위가 작아지면 수의 크기는 1000배가 됩니다! (자릿수가 오른쪽으로 3칸 이동)**")
            st.metric(label="💧 작은 단위 (mL)", value=f"{ml_calc} mL")
            st.write("---")
            st.markdown("💡 **반대로 생각하기 (mL ➡️ L)**")
            st.write("작은 단위(mL)에서 큰 단위(L)로 바뀔 때는 수의 크기가 **1/1000배**로 작아지므로 소수점이 왼쪽으로 3칸 이동합니다.")

    # ----------------------------------------------------
    # [3단계: 최종 도전 퀴즈방]
    # ----------------------------------------------------
    with menu[2]:
        st.header(f"✏️ 3단계: {user_name}이를 위한 양방향 도전 퀴즈!")
        st.write("자릿수 이동 원리를 차근차근 생각하며 정답을 맞춰보세요.")
        
        quiz_select = st.selectbox("풀고 싶은 퀴즈 유형을 선택하세요:", [
            "거리: km ➡️ m 변환하기", "거리: m ➡️ km 변환하기",
            "무게: kg ➡️ g 변환하기", "무게: g ➡️ kg 변환하기",
            "들이: L ➡️ mL 변환하기", "들이: mL ➡️ L 변환하기"
        ])
        
        st.write("---")
        
        # 퀴즈 1: km -> m
        if quiz_select == "거리: km ➡️ m 변환하기":
            st.subheader("🎯 거리 변환 퀴즈 (큰 단위 ➡️ 작은 단위)")
            st.write("🔍 **문제:** 지도에서 두 도시 사이의 거리가 **6.5 km**로 나와 있습니다.")
            ans_km_m = st.text_input("이 거리는 몇 m일까요? (숫자만 입력):", placeholder="여기에 정답을 입력하세요", key="input_km_m")
            
            if st.button("정답 확인하기", key="btn_km_m"):
                if ans_km_m.strip() == "6500":
                    st.success(f"🎉 대단해요, {user_name}님! 정답입니다! 수의 크기가 1000배가 되는 원리를 완벽히 적용했군요!")
                    st.balloons()
                else:
                    st.error("아쉬워요! 다시 생각해보세요. 큰 단위(km)에서 작은 단위(m)로 갈 때는 수의 크기가 1000배가 됩니다.")
                    
        # 퀴즈 2: m -> km
        elif quiz_select == "거리: m ➡️ km 변환하기":
            st.subheader("🎯 거리 변환 퀴즈 (작은 단위 ➡️ 큰 단위)")
            st.write("🔍 **문제:** 학교 운동장을 열심히 걸었더니 스마트폰에 **4500 m**를 이동했다고 기록되었습니다.")
            ans_m_km = st.text_input("이 거리는 몇 km일까요? (소수점을 정확히 찍어주세요):", placeholder="예: 4.5", key="input_m_km")
            
            if st.button("정답 확인하기", key="btn_m_km"):
                if ans_m_km.strip() == "4.5":
                    st.success(f"🎉 정답입니다, {user_name}님! 작은 단위에서 큰 단위로 갈 때 수의 크기가 1/1000배가 되어 자릿수가 알맞게 이동했네요!")
                    st.balloons()
                else:
                    st.error("오답입니다. m에서 km로 갈 때는 1000으로 나누어 자릿수를 왼쪽으로 3칸 옮겨야 합니다.")
                    
        # 퀴즈 3: kg -> g
        elif quiz_select == "무게: kg ➡️ g 변환하기":
            st.subheader("🎯 무게 변환 퀴즈 (큰 단위 ➡️ 작은 단위)")
            st.write("🔍 **문제:** 동물병원에서 귀여운 아기 고양이의 몸무게를 재어보니 **1.8 kg**이었습니다.")
            ans_kg_g = st.text_input("이 몸무게는 몇 g일까요? (숫자만 입력):", placeholder="여기에 정답을 입력하세요", key="input_kg_g")
            
            if st.button("정답 확인하기", key="btn_kg_g"):
                if ans_kg_g.strip() == "1800":
                    st.success(f"🎉 정답입니다! {user_name}님, kg 단위가 g 단위로 바뀌어 1000배 큰 수로 멋지게 변환했습니다!")
                    st.balloons()
                else:
                    st.error("다시 계산해보세요! kg 단위가 g 단위로 바뀌면 수의 크기는 1000배 커지며 소수점이 오른쪽으로 이동합니다.")
                    
        # 퀴즈 4: g -> kg
        elif quiz_select == "무게: g ➡️ kg 변환하기":
            st.subheader("🎯 무게 변환 퀴즈 (작은 단위 ➡️ 큰 단위)")
            st.write("🔍 **문제:** 집으로 배달된 택배 상자의 무게를 측정하니 **3200 g**이 나왔습니다.")
            ans_g_kg = st.text_input("이 상자는 몇 kg일까요? (소수점 포함 가능):", placeholder="여기에 정답을 입력하세요", key="input_g_kg")
            
            if st.button("정답 확인하기", key="btn_g_kg"):
                if ans_g_kg.strip() == "3.2":
                    st.success(f"🎉 완벽합니다! 자릿수 줄이기 마스터 성공! {user_name}님의 수학적 추론 능력이 빛나네요!")
                    st.balloons()
                else:
                    st.error("틀렸습니다. g에서 kg으로 바뀔 때는 수의 크기가 1/1000배가 되므로 자릿수가 아래로 내려갑니다.")

        # 퀴즈 5: L -> mL
        elif quiz_select == "들이: L ➡️ mL 변환하기":
            st.subheader("🎯 들이 변환 퀴즈 (큰 단위 ➡️ 작은 단위)")
            st.write("🔍 **문제:** 과학 실험실에서 모둠 실험을 위해 비커에 깨끗한 물 **2.4 L**를 채웠습니다.")
            ans_l_ml = st.text_input("이 물의 양은 몇 mL일까요? (숫자만 입력):", placeholder="여기에 정답을 입력하세요", key="input_l_ml")
            
            if st.button("정답 확인하기", key="btn_l_ml"):
                if ans_l_ml.strip() == "2400":
                    st.success(f"🎉 정답입니다, {user_name}님! 들이 단위도 1000배 커지는 자릿수 원리를 정확하게 적용하셨군요!")
                    st.balloons()
                else:
                    st.error("아쉬워요. L에서 mL로 갈 때도 수의 크기가 1000배가 되므로 소수점을 오른쪽으로 3칸 옮겨보세요.")

        # 퀴즈 6: mL -> L
        elif quiz_select == "들이: mL ➡️ L 변환하기":
            st.subheader("🎯 들이 변환 퀴즈 (작은 단위 ➡️ 큰 단위)")
            st.write("🔍 **문제:** 개인 텀블러에 시원하게 달인 보리차를 가득 채웠더니 양이 **750 mL**였습니다.")
            ans_ml_l = st.text_input("이 보리차의 양은 몇 L일까요? (소수점으로 표현해보세요):", placeholder="예: 0.75", key="input_ml_l")
            
            if st.button("정답 확인하기", key="btn_ml_l"):
                if ans_ml_l.strip() == "0.75":
                    st.success(f"🎉 축하합니다! 수의 크기가 1/1000배가 되어 소수점이 왼쪽으로 3칸 정상적으로 이동한 정답을 맞추셨습니다!")
                    st.balloons()
                else:
                    st.error("다시 신중하게 생각해보세요! 750에서 소수점을 왼쪽으로 3칸 옮기면 맨 앞에 0이 붙게 됩니다.")

        # ----------------------------------------------------
        # 4. 전체 화면 초기화 시스템
        # ----------------------------------------------------
        st.write("---")
        if st.button("🔄 전체 화면 초기화하기"):
            # 모든 세션 상태 초기화
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

else:
    # 사용자 이름을 적기 전, 가장 첫 진입 화면 레이아웃
    st.info("💡 위의 입력창에 이름을 입력하시면 풍성한 '수와 단위' 조작 교실이 시작됩니다!")