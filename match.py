import cv2
import numpy
import glob

img_list1 = [cv2.imread(file) for file in glob.glob('src1/*png')]
img_list2 = [cv2.imread(file) for file in glob.glob('src2/*png')]
i = 1

for (img1, img2) in zip(img_list1, img_list2) :

    img1 = cv2.resize(img1, (1920,1080))
    img2 = cv2.resize(img2, (1920,1080))

    img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    delta_frame = cv2.absdiff(img3,img2)

    delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    (cnts, _) = cv2.findContours(delta_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for countour in cnts:
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)

    cv2.imwrite('dest/result_img' +str(i) +'.jpg', img1)
    i = i + 1

#print("total images processed :",i-1)