import cv2
img = cv2.imread('oficina.png') # Replace with a valid image path
cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()