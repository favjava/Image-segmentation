import cv2
from matplotlib import pyplot as plt


def f5():
    img = cv2.imread('D:\\Can.jpg', 0)
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Image')
    plt.xticks([]), plt.yticks([])
    plt.show()
