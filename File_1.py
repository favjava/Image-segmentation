import cv2
import matplotlib.pyplot as plt


def f1():
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    len(flags)
    img = cv2.imread('D:\\Orange.jpg')
    plt.imshow(img)
    plt.show()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    light_orange = (1, 190, 200)
    dark_orange = (18, 255, 255)
    mask = cv2.inRange(hsv_img, light_orange, dark_orange)
    result = cv2.bitwise_and(img, img, mask=mask)
    plt.subplot(1, 2, 1)
    plt.imshow(mask, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.show()
    light_white = (0, 0, 200)
    dark_white = (145, 60, 255)
    mask_white = cv2.inRange(hsv_img, light_white, dark_white)
    result_white = cv2.bitwise_and(img, img, mask=mask_white)
    plt.subplot(1, 2, 1)
    plt.imshow(mask_white, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(result_white)
    plt.show()

    final_mask = mask + mask_white
    final_result = cv2.bitwise_and(img, img, mask=final_mask)
    plt.subplot(1, 2, 1)
    plt.imshow(final_mask, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(final_result)
    plt.show()
    blur = cv2.GaussianBlur(final_result, (7, 7), 0)
    plt.imshow(blur)
    plt.show()
