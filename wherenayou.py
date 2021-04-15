from mapbox import Static, StaticStyle
from pathlib import Path
import streamlit as st
import base64
import requests

service = StaticStyle(access_token="pk.eyJ1IjoicnVra3UiLCJhIjoiZEJocE9tSSJ9.tWSIxlu5AHgccim4JMuWLQ")

r = requests.get('https://api.orbit-v2.phl-microsat.upd.edu.ph/point/43678/')
response = r.json()

data = response['data']
lon = data['coordinates'][0]
lat = data['coordinates'][1]

response = service.image(username="rukku", style_id='cknitcds20see17pafmuxoxvf',lon=lon, lat=lat, zoom=7.62,bearing=39, width=600, height=500)

with open('map2.png', 'wb') as output:
    _ = output.write(response.content)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.write("Where na you, Diwata-2?")
header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
    img_to_bytes("map2.png")
)
st.markdown(
    header_html, unsafe_allow_html=True,
)

st.write(f"{round(lon, 2)}, {round(lat, 2)}")