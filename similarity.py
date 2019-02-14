import cv2
from skimage.measure import compare_ssim
import math

img1 = cv2.imread('src1/img_1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('src2/img_1.png', cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1, (828, 644), fx = 1, fy = 1, interpolation = cv2.INTER_CUBIC)
img2 = cv2.resize(img2, (828, 644), fx = 1, fy = 1, interpolation = cv2.INTER_CUBIC)

(score, diff) = compare_ssim(img1, img2, full=True)
diff = (diff * 255).astype("uint8")

percentage = str(math.floor(score*100))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1, percentage+'/100' , (10,450), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imwrite('text.jpg', img1)