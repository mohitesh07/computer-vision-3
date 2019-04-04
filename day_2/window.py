import cv2

img = cv2.imread('RandomColor.png')
cv2.imshow('OUTPUT IMAGE',img)
cv2.waitKey()
cv2.destroyAllWindows()
