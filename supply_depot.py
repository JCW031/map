import streamlit as st
from PIL import Image
import requests
import importlib.util
import os

# 회사 딕셔너리 생성
companies = {
    "㈜골드넥스": 1,
    "㈜구하다": 2,
    "㈜글로랑": 3,
    "㈜넷앤드": 4,
    "㈜다트미디어": 5,
    "대원씨티에스㈜": 6,
    "㈜더에스엠씨그룹": 7,
    "델타일렉트로닉스코리아㈜": 8,
    "레오버넷㈜": 9,
    "㈜마쉬코리아보험중개": 10,
    "메드트로닉코리아(유)": 11,
    "㈜모비데이즈": 12,
    "㈜알파브라더스": 13,
    "앨리슨하이퍼앰㈜": 14,
    "㈜에이치에너지": 15,
    "엔시큐어㈜": 16,
    "㈜엘리스그룹": 17,
    "㈜엠비씨아트": 18,
    "㈜엣지랭크": 19,
    "오티스엘리베이터코리아(유)": 20,
    "㈜오픈놀": 21,
    "위즈코어㈜": 22,
    "유한킴벌리㈜": 23,
    "㈜이엠텍아이엔씨": 24,
    "㈜중고나라": 25,
    "㈜칸타코리아": 26,
    "㈜티몬": 27,
    "㈜포시에스": 28,
    "㈜피알원": 29,
    "㈜하이랜드푸드": 30,
    "해줌": 31
}

# CSS 스타일을 사용하여 subheader 오른쪽 정렬 설정
st.markdown(
    """
    <style>
    .subheader-right {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목과 이미지 출력
st.title('직무캠프 참여기업 데이터 베이스')

# 이미지 열기 및 표시
try:
    main_screen_image = Image.open('main screen.png')
    st.image(main_screen_image, caption='Main Screen', use_column_width=True)
except FileNotFoundError:
    st.error("메인 화면 이미지를 찾을 수 없습니다. 파일 경로를 확인해주세요.")

# 오른쪽 정렬된 subheader 출력
st.markdown('<h2 class="subheader-right">Made by CJ</h2>', unsafe_allow_html=True)

# Sidebar에 로그인 섹션 추가
st.sidebar.header('ID/ PASSWORD')
user_id = st.sidebar.text_input('아이디 입력', value='', max_chars=15)
user_password = st.sidebar.text_input('패스워드 입력', value='', type='password')
click = st.sidebar.button('sign in')  # 버튼을 사이드바에 배치하여 비밀번호 아래로 이동

if click:
    if user_id == 'pass' and user_password == '1234':
        # GitHub에서 data_crawling.py 파일 다운로드 및 실행
        url = "https://raw.githubusercontent.com/JCW031/map/main/data_crawling.py"
        response = requests.get(url)
        
        if response.status_code == 200:
            # 파일로 저장
            with open('data_crawling.py', 'w') as file:
                file.write(response.text)

            # 동적으로 모듈 로드
            spec = importlib.util.spec_from_file_location("data_crawling", "data_crawling.py")
            data_crawling = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(data_crawling)

            st.sidebar.header('가고 싶은 회사를 고르세요')
            menu = st.sidebar.radio('회사 선택', list(companies.keys()))

            if menu:
                st.sidebar.write(f'선택한 회사: {menu}, 회사 번호: {companies[menu]}')

                # 지도 생성 및 표시
                depart = data_crawling.create_map()
                depart.save('company_list.html')
                st.markdown(
                    f'<iframe src="company_list.html" width="100%" height="800"></iframe>',
                    unsafe_allow_html=True
                )
            else:
                st.sidebar.warning('메뉴를 선택해주세요')
        else:
            st.error('data_crawling.py 파일을 다운로드할 수 없습니다. URL을 확인하세요.')
    else:
        st.sidebar.error('아이디 또는 패스워드가 잘못되었습니다.')
