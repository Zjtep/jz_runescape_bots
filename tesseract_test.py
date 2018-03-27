# coding: utf-8
# import pytesseract
# from PIL import Image, ImageEnhance, ImageFilter
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# im = Image.open("temp.jpg") # the second one
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
# text = pytesseract.image_to_string(Image.open('temp2.jpg'))
# print

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# im = Image.open("temp.jpg") # the second one
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
# text = pytesseract.image_to_string(Image.open('temp2.jpg'))
# print(text)



import numpy
# # image = Image.open("temp.jpg")
# # image = Image.open(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\ge_buy_sample.PNG")
#
# image = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\ge_history_sample02.PNG"))
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#
# # gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# # gray = cv2.medianBlur(gray, 3)
#
# # write the grayscale image to disk as a temporary file so we can
# # apply OCR to it
# gray = cv2.resize(image, (0,0), fx=2, fy=2)
# ret,gray = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY)
#
# gray = Image.fromarray(gray,'RGB')
# # filename = "{}.png".format(os.getpid())
# # cv2.imwrite(filename, gray)
#
# text = pytesseract.image_to_string(gray)
# # text = pytesseract.image_to_string(Image.open(filename))
# # os.remove(filename)
# print(text)
#
# # show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)
#
#https://github.com/tesseract-ocr/tesseract/wiki/Training-Tesseract

gray = numpy.array(cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\lib\reference\dimension_test\price_test\16.PNG"))
# gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (0,0), fx=5, fy=5)
# ret,gray = cv2.threshold(gray, 108, 255,cv2.THRESH_BINARY)
# ret,gray = cv2.threshold(gray, 85, 255,cv2.THRESH_BINARY)
# ret,gray = cv2.threshold(gray, 90, 255,cv2.THRESH_BINARY)
gray = cv2.threshold(gray, 90, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# gray = Image.fromarray(gray,'RGB')
text = pytesseract.image_to_string(gray)
# text = pytesseract.image_to_string(gray,config='outputbase digits')
# text = text.replace(",","")

text_list = list(text)
for i in range(len(text)):
    if text_list[i] ==':':
        text_list[i] =","
    elif text_list[i] ==u'“':
        text_list[i] ="4"
    elif text_list[i] =='k':
        text_list[i] ="4"
print("".join(text_list))

# print("\n"+text)
# cv2.imwrite("16r.png", gray)
cv2.imshow("Output", gray)

cv2.waitKey(0)