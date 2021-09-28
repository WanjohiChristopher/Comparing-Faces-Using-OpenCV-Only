import cv2
img=cv2.imread('pexe3.jpg', cv2.IMREAD_GRAYSCALE)
threshold=120
img_binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]
print(img_binary)
#save image
cv2.imwrite('pexe-black-and-white.png',img_binary) 