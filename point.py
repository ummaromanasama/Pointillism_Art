import cv2

#Read image
myImage = cv2.imread('wreck.jpg')

#Display image
cv2.imshow('Wreck-It Ralph', myImage)

#Close window by pressing any key
cv2.waitKey(0)