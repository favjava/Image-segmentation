import numpy as np
import cv2


def f4():
    img = cv2.imread('D:\\cancer_cells.jpg')
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply KMeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape(img.shape)
    cv2.imshow('res2', res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
