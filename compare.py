import cv2
import glob

def match_images(source1, source2) :

    img_list1 = [cv2.imread(file) for file in glob.glob(source1)]
    img_list2 = [cv2.imread(file) for file in glob.glob(source2)]
    img_num = 1
    match = False
    for (img1, img2) in zip(img_list1, img_list2):

        img1 = cv2.resize(img1, (480, 360))
        img2 = cv2.resize(img2, (480, 360))

        cv2.imwrite('src1/img_' + str(img_num) + '.png', img1)
        cv2.imwrite('src2/img_' + str(img_num) + '.png', img2)

        delta_frame = cv2.absdiff(img1, img2)
        b, g, r = cv2.split(delta_frame)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
            match = True
        else :
            match = False

        delta_frame = cv2.cvtColor(delta_frame, cv2.COLOR_BGR2GRAY)
        delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]



        (cnts, _) = cv2.findContours(delta_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for countour in cnts:
            (x, y, w, h) = cv2.boundingRect(countour)
            cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)

        if match == True :
            cv2.imwrite('dest/result_matching_img' + str(img_num) + '.png', img1)
        else :
            cv2.imwrite('dest/result_different_img' + str(img_num) + '.png', img1)

        img_num = img_num + 1

    print("Images Processed :", img_num - 1)
