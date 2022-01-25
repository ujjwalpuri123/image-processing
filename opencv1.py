import cv2

img=cv2.imread("Lighthouse.jpg",0)

print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("lighthouse",resized_image)
cv2.imwrite("lighthouse.jpeg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()