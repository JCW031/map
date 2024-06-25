import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import base64

def create_map():
    # 데이터프레임 로드
    df = pd.read_excel('geocode_company.xlsx')

    # 지도 생성
    depart = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()],
                        zoom_start=13, width=1000, height=800)

    for n, row in df.iterrows():
        # 이미지 파일 경로 (01.png ~ 31.png)
        image_number = str(n + 1).zfill(2)  # '01', '02', ..., '31'
        image_path = f"c_list_image/{image_number}.png"

        # 이미지를 base64로 인코딩
        try:
            with open(image_path, 'rb') as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            # HTML 팝업 내용 생성
            html = f'''
            <h4>{row['회사명']}</h4>
            <img src="data:image/png;base64,{encoded}" width="300">
            '''
        except FileNotFoundError:
            html = f'''
            <h4>{row['회사명']}</h4>
            <p>이미지 파일을 찾을 수 없습니다.</p>
            '''

        iframe = folium.IFrame(html, width=320, height=320)
        popup = folium.Popup(iframe, max_width=650)

        # 마커 추가
        folium.Marker(location=[row['Latitude'], row['Longitude']],
                      popup=popup,
                      tooltip=row['회사명'],
                      icon=folium.Icon(color='orange', icon='c', prefix='fa')).add_to(depart)

    return depart

st.title('Company Map')

# Folium 지도 생성 함수 호출
depart = create_map()

# Folium 지도를 Streamlit 앱에 표시
folium_static(depart)
