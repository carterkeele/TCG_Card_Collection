import cv2
import numpy as np
from PIL import Image

import card_search
import card_list
import utility

def compute_phash(img):
    if img is None:
        print(f'Error: Image not found')
        return None
    
    phash = cv2.img_hash.PHash_create()

    return phash.compute(img)

def compare(hash1, hash2, threshold=10):
    if hash1 is not None and hash2 is not None:
        ham_dist = cv2.norm(hash1, hash2, cv2.NORM_HAMMING)

        if ham_dist < threshold:
            print(f'Hamming Distance: {ham_dist}')

    return ham_dist < threshold

def process():
    card_list.create_card_list()

    height = utility.getCardHeight()
    width = utility.getCardWidth()

    scan = cv2.imread(r'C:\Users\carte\Desktop\HackED 2025\testing\elsa - snow queen.jpg')
    scan = cv2.resize(scan, (width, height), interpolation=cv2.INTER_AREA)
    scan = cv2.cvtColor(scan, cv2.COLOR_BGR2GRAY)
    scan = cv2.GaussianBlur(scan, (3,3), 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    scan = clahe.apply(scan)

    if scan is None:
        print('Error: Image not found.')
        exit()

    hash_scan = compute_phash(scan)

    imgs = card_list.getImages()

    for i in range(len(imgs)):
        search_img = imgs[i]
        search_img = cv2.resize(search_img, (width, height),interpolation=cv2.INTER_AREA)
        search_img = cv2.GaussianBlur(search_img, (3,3), 0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        search_img = clahe.apply(search_img)
        hash_search = compute_phash(search_img)

        if compare(hash_scan, hash_search):
            print(f'Match Found: {card_list.names[i]}')
            #cv2.imshow('Input', scan)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #cv2.imshow(f'{cards[i]['Name']}', search_img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

process()
    
    
    

