import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.data import coins
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops


def f3():

    def show(img, cmap=None):
        cmap = cmap or plt.cm.gray
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        ax.imshow(img, cmap=cmap)
        ax.set_axis_off()
        plt.show()

    img = coins()
    show(img)
    threshold_otsu(img)
    show(img > 107)
    from ipywidgets import widgets

    @widgets.interact(t=(50, 240))
    def threshold(t):
        show(img > t)
        img_bin = clear_border(closing(img > 120, square(5)))
        show(img_bin)
        labels = label(img_bin)
        show(labels, cmap=plt.cm.rainbow)
        regions = regionprops(labels)
        boxes = np.array([label['BoundingBox']
                          for label in regions
                          if label['Area'] > 100])
        print(f"There are {len(boxes)} coins.")
