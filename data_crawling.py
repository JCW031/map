import folium
import pandas as pd

def create_map():
    df = pd.read_excel(r'C:\Users\정우\Desktop\Base\0622\image_location_info.xlsx')

    depart = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()],
                        zoom_start=13, width=1000, height=800)

    for n, row in df.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']],
                      popup=row['회사명'],
                      tooltip=row['회사명'],
                      icon=folium.Icon(color='orange', icon='c', prefix='fa')).add_to(depart)

    return depart

depart = create_map()
depart.save('company_list.html')
