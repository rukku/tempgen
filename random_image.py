import requests
from random import randrange
import streamlit as st


r = requests.get('https://api.data.phl-microsat.upd.edu.ph/scenes?limit=10000')
response = r.json()

data = response['data']

def randomizer(i):
    data_length = len(i)
    return randrange(data_length)

def get_image_url(data, index):
    image_url = data[index]['links']['thumbnail_url'] 
    return image_url


def random_image(data):
    index = randomizer(data)
    print(index)
    image_url = get_image_url(data, index)
    # print(image_url)
    return image_url


if st.button("Get random Diwata image", key=None, help=None):

    img = random_image(data)
    st.markdown(f"![Alt Text]({img})")
