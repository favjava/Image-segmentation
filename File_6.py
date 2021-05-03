# import the necessary packages
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import imutils
import cv2
# construct the argument parse and parse the arguments
# load the image and perform pyramid mean shift filtering
# to aid the thresholding step


def f6():
	image = cv2.imread("D:\\cancer_cells.jpg")
	shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
	cv2.imshow("Input", image)
	# convert the mean shift image to grayscale, then apply thresholding
	gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imshow("Thresh", thresh)
	D = ndimage.distance_transform_edt(thresh)
	local_max = peak_local_max(D, indices=False, min_distance=20, labels=thresh)
	# perform a connected component analysis on the local peaks,
	# using 8-connectivity, then apply the Watershed algorithm
	markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
	labels = watershed(-D, markers, mask=thresh)
	print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))
	for label in np.unique(labels):
		# if the label is zero, we are examining the 'background'
		# so simply ignore it
		if label == 0:
			continue
		# otherwise, allocate memory for the label region and draw
		# it on the mask
		mask = np.zeros(gray.shape, dtype="uint8")
		mask[labels == label] = 255
		# detect contours in the mask and grab the largest one
		cont = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cont = imutils.grab_contours(cont)
		c = max(cont, key=cv2.contourArea)
		# draw a circle enclosing the object
		((x, y), r) = cv2.minEnclosingCircle(c)
		cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
		cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	# show the output image
	cv2.imshow("Output", image)
	cv2.waitKey(0)
