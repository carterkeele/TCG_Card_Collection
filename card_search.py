import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

def fetch_card_data():
    card_api_url = f'https://api.lorcana-api.com/cards/all'
    response = requests.get(card_api_url)
    response.raise_for_status()

    try:
        card_data = response.json()

        if card_data:
            return card_data
        else:
            print("No Data Found")
            return None
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def img_from_url(url):
    response = requests.get(url)
    response.raise_for_status()

    img_arr = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_GRAYSCALE)
    return img
    
