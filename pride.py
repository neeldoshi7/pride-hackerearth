import cv2
import pytesseract
import numpy as np

import pandas as pd
dataset = pd.read_csv('test.csv')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

text = []

for i in range(239):
    x = dataset['Filename'][i]
    print(x)
    img = cv2.imread(x)
    #print(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.bitwise_not(img)
    img = cv2.medianBlur(img,5)
    
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    kernel = np.ones((5,5),np.uint8)
    
    out_below = pytesseract.image_to_string(img)
    print("OUTPUT:", out_below)
    text.append(out_below)  

from spellchecker import SpellChecker
spell = SpellChecker()

text
df = pd.DataFrame(text)
df.to_csv(r'quotes3.csv')


'''img = cv2.imread('Test1001.jpg')
print(img)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.bitwise_not(gray)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(img)
print("OUTPUT:", out_below)'''

'''for i in range(239):
    x = dataset['Filename'][i]
    print(x)
    img = cv2.imread(x)
    #print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.bitwise_not(gray)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    kernel = np.ones((5,5),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    out_below = pytesseract.image_to_string(img)
    print("OUTPUT:", out_below)
    text.append(out_below)'''




