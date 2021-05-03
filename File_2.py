import cv2
from matplotlib import pyplot as plt


def f2():
    img = cv2.imread("D:\\cancer_cells.jpg")
    img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

    plt.figure("Original")
    plt.imshow(img_color)

    plt.figure("Grayscale")
    plt.imshow(gray, cmap="gray")

    plt.figure("Binary")
    plt.imshow(thresh, cmap="gray")
    plt.show()
