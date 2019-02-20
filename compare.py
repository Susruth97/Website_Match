import cv2
import glob
from PIL import Image
import math
from PIL import ImageChops

def match_images(source1, source2, destination) :

    try :
        img_list1 = [cv2.imread(file) for file in glob.glob(source1 + '/*.png')]
        img_list2 = [cv2.imread(file) for file in glob.glob(source2 + '/*.png')]
    except Exception as e :
        print("Reading .png files :",e)
    img_num = 1

    try :
        for (img1, img2) in zip(img_list1, img_list2):

            img1 = cv2.resize(img1, (828, 644), fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
            img2 = cv2.resize(img2, (828, 644), fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

            cv2.imwrite(source1 + '/img_' + str(img_num) + '.png', img1)
            cv2.imwrite(source2 + '/img_' + str(img_num) + '.png', img2)

            draw_counters(img1, img2)

            pil_img1 = Image.open(source1 + '/img_' + str(img_num) + '.png')
            pil_img2 = Image.open(source2 + '/img_' + str(img_num) + '.png')
            diff_per = rms_diff(pil_img1, pil_img2)

            score = int((100 - diff_per)/10)
            draw_score(img1, score)

            if score == 10 :
                cv2.imwrite(destination + '/result_matching_img' + str(img_num) + '.png', img1)
            else:
                cv2.imwrite(destination + '/result_different_img' + str(img_num) + '.png', img1)

            img_num = img_num + 1
    except Exception as e :
        print(e)

    print('Images Processed :', img_num - 1)
    print('Completed!')

def draw_counters(img1, img2) :

    try :
        img1_temp = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_temp = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        delta_frame = cv2.absdiff(img1_temp, img2_temp)
        delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

        (cnts, _) = cv2.findContours(delta_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for countour in cnts:
            (x, y, w, h) = cv2.boundingRect(countour)
            cv2.rectangle(img1, (x, y), (x + w, y + h), (71, 99, 255), 1)
    except Exception as e :
        print(e)


def rms_diff(img1, img2):

    try :
        diff = ImageChops.difference(img1, img2)
        h = diff.histogram()
        sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares / float(img1.size[0] * img1.size[1]))
        return rms
    except Exception as e :
        print(e)

def draw_score(img, score) :

    try :
        font = cv2.FONT_HERSHEY_SIMPLEX
        if score != 10 :
            text = '  ' + str(score) + '\n ___ \n \n \n \n 10'
        else :
            text = ' ' + str(score) + '\n ___ \n \n \n \n 10'

        y0, dy = 470, 8
        for i, line in enumerate(text.split('\n')):
            y = y0 + i * dy
            cv2.putText(img, line, (40, y), font, 1, (71, 99, 255), 2, cv2.LINE_AA)

        cv2.circle(img, (80, 476), 50, (71, 99, 255), 2)
    except Exception as e :
        print('Drawing score :',e)

