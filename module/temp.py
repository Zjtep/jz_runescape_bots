# import numpy as np
# import cv2
#
# img = cv2.imread('messi5.jpg',0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()
#
# import cv2
# import numpy as np
#



# import cv2
# import numpy as np
# img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_window3.JPG')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\bank_booth.JPG',0)
# # print template
#
# w, h = template.shape[::-1]
# print w,h
#
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.50
# loc = np.where( res >= threshold)
#
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#
# cv2.imwrite('asdf.png',img_rgb)
# cv2.imshow('Detected',img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# im = cv2.imread(r"C:\Users\PPC\git\RS_BOT_2.0\library\reference\full_window2.JPG")
# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("plank", gray)
# cv2.waitKey()
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# _, bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
# bin = cv2.dilate(bin, None)  # fill some holes
# bin = cv2.dilate(bin, None)
# bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
# bin = cv2.erode(bin, None)
# bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
# rc = cv2.minAreaRect(contours[0])
# box = cv2.boxPoints(rc)
# for p in box:
#     pt = (p[0],p[1])
#     print pt
#     cv2.circle(im,pt,5,(200,0,0),2)
# # cv2.imshow("plank", im)
# # cv2.waitKey()


import cv2
import numpy as np
img_path = r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\window_01.png'
img = cv2.imread(img_path, 0)
img_edges = cv2.Canny(img, 100, 100)
cv2.imshow("img", img)
cv2.imshow("img_edges", img_edges)
cv2.waitKey()
