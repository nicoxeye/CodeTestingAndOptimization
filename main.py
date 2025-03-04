import cv2

# reading an image
# ex. 1

# loading the image in color:
image = cv2.imread("img.jpg")
# image1 = cv2.imread("img1.jpg")
# [ WARN:0@0.096] global loadsave.cpp:268 cv::findDecoder imread_('img1.jpg'):
# can't open/read file: check file path/integrity

if image is None:
    print("error loading the image")
else:
    print("correctly read the image")

    # ex.2
    (h, w, c) = image.shape[:3]
    print(f'channels: {c}')  # channels : 3

    # loading the image in color:
    cv2.imshow("image in color", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# loading the image in gray scale:
image_gray = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

if image_gray is None:
    print("error loading the image")
else:
    print("correctly read the image")

    (h, w, c) = image.shape[:3]
    print(f'channels: {c}')  # channels : 3

    cv2.imshow("image in gray scale", image_gray)
    k = cv2.waitKey(0)

    # ex.4 saving image
    if k == ord("s"):
        cv2.imwrite("grey_scale_image.jpg", image_gray)

    cv2.destroyAllWindows()

# ex.5
cv2.imshow("image in color", image)

cv2.imshow("image in gray scale", image_gray)

cv2.waitKey(0)

# ex.6

cv2.imshow("image in color", image)



