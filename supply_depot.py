import streamlit as st
from streamlit_folium import folium_static

# Folium 지도 생성 코드 가져오기
from folium_map import create_map

st.title('Company Map')

# Folium 지도 생성 함수 호출
depart = create_map()

# Folium 지도를 Streamlit 앱에 표시
folium_static(depart)
