import cv2
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

#image_path = r'C:\Users\carte\Desktop\HackED 2025\testing\piplup2.jpg'
#image = Image.open(image_path)
#extracted_text = pytesseract.image_to_string(image)
#print(extracted_text)

img = cv2.imread(r'C:\Users\carte\Desktop\HackED 2025\testing\belle - hidden archer.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5),0)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)

processed = cv2.erode(dilation, rect_kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

file = open("recognized.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cropped = im2[y:y + h, x:x + w]

    file = open("recognized.txt", "a")

    text = pytesseract.image_to_string(cropped)

    file.write(text)
    file.write("\n")

    file.close()
