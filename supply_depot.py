import streamlit as st
from PIL import Image

st.title('직무캠프 참여기업 데이터 베이스')
st.header('Made by CJ')

# 이미지 열기 및 표시
main_screen_image = Image.open('relative/path/to/main screen.png')
st.image(main_screen_image, caption='Main Screen', use_column_width=True)

# Sidebar에 로그인 섹션 추가
st.sidebar.header('Log in')
user_id = st.sidebar.text_input('아이디 입력', value='', max_chars=15)
user_password = st.sidebar.text_input('패스워드 입력', value='', type='password')

if user_id == 'pass' and user_password == '1234':
    st.sidebar.header('Cj Portfolio')

    menu = st.sidebar.radio('회사 선택', [
        "㈜골드넥스",
        "㈜구하다",
        "㈜글로랑",
        "㈜넷앤드",
        "㈜다트미디어",
        "대원씨티에스㈜",
        "㈜더에스엠씨그룹",
        "델타일렉트로닉스코리아㈜",
        "레오버넷㈜",
        "㈜마쉬코리아보험중개",
        "메드트로닉코리아(유)",
        "㈜모비데이즈",
        "㈜알파브라더스",
        "앨리슨하이퍼앰㈜",
        "㈜에이치에너지",
        "엔시큐어㈜",
        "㈜엘리스그룹",
        "㈜엠비씨아트",
        "㈜엣지랭크",
        "오티스엘리베이터코리아(유)",
        "㈜오픈놀",
        "위즈코어㈜",
        "유한킴벌리㈜",
        "㈜이엠텍아이엔씨",
        "㈜중고나라",
        "㈜칸타코리아",
        "㈜티몬",
        "㈜포시에스",
        "㈜피알원",
        "㈜하이랜드푸드",
        "해줌"
    ])

    if menu:
        st.sidebar.write(f'선택한 회사: {menu}')
        # 여기에 선택한 회사에 따른 추가적인 작업을 수행할 수 있음
    else:
        st.sidebar.warning('메뉴를 선택해주세요')
else:
    st.sidebar.warning('잘못된 아이디 또는 패스워드입니다.')

    
