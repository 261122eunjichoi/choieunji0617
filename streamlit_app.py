import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="초등 수학 단위 마스터", page_icon="📐", layout="centered")

st.title("🌈 눈으로 보고 조작하는 '수와 단위' 마스터!")
st.write("단순히 0의 개수만 외우지 말고, 숫자를 움직이며 자릿수의 비밀을 찾아보세요.")
st.write("---")

# 1. 사용자 이름 입력 (개인화 요소)
user_name = st.text_input("👋 반갑습니다! 여러분의 이름을 입력해주세요:", placeholder="예: 홍길동")

if user_name:
    st.success(f"🎉 준비 완료! **{user_name}** 학생만을 위한 맞춤형 융합 수학 교실을 시작합니다.")
    
    # 상단 탭 구성으로 콘텐츠를 더욱 풍성하게 분할
    menu = st.tabs(["📋 [1단계] 실생활 속 단위 발견", "🔍 [2단계] 자릿수 추론 조작실", "✏️ [3단계] 최종 도전 퀴즈방"])
    
    # ----------------------------------------------------
    # [1단계: 실생활 속 단위 발견]
    # ----------------------------------------------------
    with menu[0]:
        st.header("📋 1단계: 우리 주변의 거리와 무게")
        st.write(f"**{user_name}**님, 우리 주변에서 큰 수와 다양한 단위가 쓰이는 상황을 먼저 살펴봐요!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛣️ 거리를 나타낼 때")
            st.info("🏃 **마라톤 공식 코스의 길이**\n\n**42195 m**는 너무 길어서 보기가 힘들어요. 이럴 때 큰 단위인 **km**를 사용하면 편리합니다.")
            st.warning("⛰️ **한라산의 높이**\n\n한라산의 높이는 약 **1947 m**입니다. 이것을 km로 바꾸면 숫자가 어떻게 바뀔까요?")
            
        with col2:
            st.subheader("⚖️ 무게를 나타낼 때")
            st.info("🐋 **흰수염고래의 무게**\n\n지구상에서 가장 큰 동물은 약 **150000 kg**입니다. 너무 무거워서 단위를 **g**으로 쓰면 숫자가 너무 커지겠죠?")
            st.warning("🍎 **사과 한 개의 무게**\n\n보통 사과 한 개는 약 **250 g**입니다. 마트에서 사과를 많이 골라 담아 **kg** 단위가 되면 어떻게 변할지 알아봅시다.")

    # ----------------------------------------------------
    # [2단계: 자릿수 추론 조작실 (슬라이더 및 원리 추론)]
    # ----------------------------------------------------
    with menu[1]:
        st.header("🔍 2단계: 손으로 움직이며 추론하는 조작실")
        st.write("슬라이더를 왼쪽, 오른쪽으로 직접 움직이면서 수의 크기와 단위가 어떻게 변하는지 눈으로 관찰해보세요.")
        
        unit_choice = st.selectbox("어떤 단위를 조작해볼까요?", ["거리 단위 (m ↔ km)", "무게 단위 (g ↔ kg)"])
        
        if unit_choice == "거리 단위 (m ↔ km)":
            st.subheader("🛣️ 거리의 양방향 변화 관찰")
            
            # 슬라이더 조작을 통한 실시간 추론
            km_slide = st.slider("👉 km 값을 움직이며 m 값이 어떻게 변하는지 보세요:", 0.0, 10.0, 3.5, step=0.5)
            m_calc = int(km_slide * 1000)
            
            # 시각적 가이드 카드
            st.metric(label="🗺️ 큰 단위 (km)", value=f"{km_slide} km")
            st.markdown("⬇️ **단위가 작아지면 수의 크기는 1000배가 됩니다! (소수점이 오른쪽으로 3칸 이동)**")
            st.metric(label="📍 작은 단위 (m)", value=f"{m_calc} m")
            
            st.write("---")
            st.markdown("💡 **반대로 생각하기 (m ➡️ km)**")
            st.write("작은 단위(m)에서 큰 단위(km)로 바뀔 때는 수의 크기가 **1/1000배**로 줄어듭니다. 소수점이 왼쪽으로 3칸 이동하는 규칙을 기억하세요!")

        elif unit_choice == "무게 단위 (g ↔ kg)":
            st.subheader("⚖️ 무게의 양방향 변화 관찰")
            
            # 슬라이더 조작
            kg_slide = st.slider("👉 kg 값을 움직이며 g 값이 어떻게 변하는지 보세요:", 0.0, 5.0, 1.2, step=0.1)
            g_calc = int(kg_slide * 1000)
            
            st.metric(label="🍏 큰 단위 (kg)", value=f"{kg_slide} kg")
            st.markdown("⬇️ **단위가 작아지면 수의 크기는 1000배가 됩니다! (자릿수가 위로 3칸 올라갑니다)**")
            st.metric(label="🍬 작은 단위 (g)", value=f"{g_calc} g")
            
            st.write("---")
            st.markdown("💡 **반대로 생각하기 (g ➡️ kg)**")
            st.write("작은 단위(g)에서 큰 단위(kg)로 바뀔 때는 수가 **1/1000배**로 작아지므로 자릿수가 아래로 3칸 내려가게 됩니다.")

    # ----------------------------------------------------
    # [3단계: 최종 도전 퀴즈방]
    # ----------------------------------------------------
    with menu[2]:
        st.header(f"✏️ 3단계: {user_name}이를 위한 양방향 도전 퀴즈!")
        st.write("0의 개수를 외우지 않고, 자릿수 이동 원리를 생각하며 정답을 맞춰보세요.")
        
        quiz_select = st.selectbox("풀고 싶은 퀴즈 유형을 선택하세요:", [
            "거리: km ➡️ m 변환하기", 
            "거리: m ➡️ km 변환하기",
            "무게: kg ➡️ g 변환하기", 
            "무게: g ➡️ kg 변환하기"
        ])
        
        # 퀴즈 1: km -> m
        if quiz_select == "거리: km ➡️ m 변환하기":
            st.write("🔍 문제: 지도에서 두 도시 사이의 거리가 **6.5 km**로 나와 있습니다.")
            ans1 = st.text_input("이 거리는 몇 m일까요? (숫자만 입력):")
            if st.button("정답 확인", key="q1"):
                if ans1 == "6500":
                    st.success(f"🎉 정답입니다, {user_name}님! 수의 크기가 1000배가 되는 원리를 잘 적용했어요!")
                    st.balloons()
                else:
                    st.error("다시 한번 생각해보세요. 큰 단위에서 작은 단위로 갈 때는 수의 크기가 1000배가 됩니다.")
                    
        # 퀴즈 2: m -> km
        elif quiz_select == "거리: m ➡️ km 변환하기":
            st.write("🔍 문제: 학교 운동장을 20바퀴 돌았더니 **4500 m**를 걸었습니다.")
            ans2 = st.text_input("이 거리는 몇 km일까요? (소수점을 정확히 찍어주세요):")
            if st.button("정답 확인", key="q2"):
                if ans2 == "4.5":
                    st.success(f"🎉 정답입니다! 수의 크기가 1/1000배가 되어 자릿수가 왼쪽으로 이동했네요!")
                    st.balloons()
                else:
                    st.error("아쉬워요! m에서 km로 갈 때는 1000으로 나누어 자릿수를 옮겨야 합니다.")
                    
        # 퀴즈 3: kg -> g
        elif quiz_select == "무게: kg ➡️ g 변환하기":
            st.write("🔍 문제: 아기 고양이의 몸무게를 재어보니 **1.8 kg**이었습니다.")
            ans3 = st.text_input("이 몸무게는 몇 g일까요? (숫자만 입력):")
            if st.button("정답 확인", key="q3"):
                if ans3 == "1800":
                    st.success(f"🎉 정답입니다! 1000배 큰 수로 멋지게 변환했습니다!")
                    st.balloons()
                else:
                    st.error("틀렸습니다. kg 단위가 g 단위로 바뀌면 숫자는 1000배 커집니다.")
                    
        # 퀴즈 4: g -> kg
        elif quiz_select == "무게: g ➡️ kg 변환하기":
            st.write("🔍 문제: 택배로 보낼 상자의 무게가 **3200 g**이 나왔습니다.")
            ans4 = st.text_input("이 상자는 몇 kg일까요?")
            if st.button("정답 확인", key="q4"):
                if ans4 == "3.2":
                    st.success(f"🎉 대단해요, {user_name}님! 자릿수 줄이기 마스터 성공!")
                    st.balloons()
                else:
                    st.error("다시 계산해보세요. g에서 kg으로 바뀔 때는 수의 크기가 1/1000배가 됩니다.")

        # 초기화 안내 버튼
        st.write("---")
        if st.button("🔄 전체 화면 초기화하기"):
            st.rerun()

else:
    st.info("💡 위의 입력창에 이름을 입력하시면 풍성한 '수와 단위' 조작 교실이 시작됩니다!")