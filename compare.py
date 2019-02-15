import cv2
import glob
from skimage.measure import compare_ssim
import math

def match_images(source1, source2, destination) :

    img_list1 = [cv2.imread(file) for file in glob.glob(source1 + '/*.png')]
    img_list2 = [cv2.imread(file) for file in glob.glob(source2 + '/*.png')]
    img_num = 1

    for (img1, img2) in zip(img_list1, img_list2):

        img1 = cv2.resize(img1, (828, 644), fx = 1, fy = 1, interpolation = cv2.INTER_CUBIC)
        img2 = cv2.resize(img2, (828, 644), fx = 1, fy = 1, interpolation = cv2.INTER_CUBIC)

        cv2.imwrite(source1 + '/img_' + str(img_num) + '.png', img1)
        cv2.imwrite(source2 + '/img_' + str(img_num) + '.png', img2)

        img1_temp = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(img1_temp, img2, full=True)

        delta_frame = cv2.absdiff(img1_temp, img2)
        delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

        (cnts, _)  = cv2.findContours(delta_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for countour in cnts:
            (x, y, w, h) = cv2.boundingRect(countour)
            cv2.rectangle(img1, (x, y), (x + w, y + h), (71, 99, 255), 1)

        percentage = str(round(score * 100, 2))
        font = cv2.FONT_HERSHEY_SIMPLEX

        text = str(percentage) + '\n ____ \n \n \n \n 100'
        y0, dy = 520, 8
        for i, line in enumerate(text.split('\n')):
            y = y0 + i * dy
            cv2.putText(img1, line, (20, y), font, 1, (71 ,99 , 255), 2, cv2.LINE_AA)

        cv2.circle(img1, (66, 526), 60, (71, 99, 255), 2)

        if int(score) == 100 :
            cv2.imwrite(destination + '/result_matching_img' + str(img_num) + '.png', img1)
        else :
            cv2.imwrite(destination + '/result_different_img' + str(img_num) + '.png', img1)


        img_num = img_num + 1

    print('Images Processed :', img_num - 1)
    print('Completed!')
