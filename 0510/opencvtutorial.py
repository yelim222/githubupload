import cv2
print(cv2.__version__)
from matplotlib import pyplot as plt
image = cv2.imread("./images/lena.jpg", cv2.IMREAD_UNCHANGED)
# image_b=image[:,:,0]
# image_g=image[:,:,1]
# image_r=image[:,:,2]

#plt.imsave('6.png', image_b)
#plt.imsave('7.png', image_g)
#plt.imsave('8.png', image_r)
#cv2.imshow("Moon", image)
(h,w) = image.shape[:2]
center=(w/2,h/2)
for i in range(1,360,10):
    M= cv2.getRotationMatrix2D(center, i, 1.0)
    img90=cv2.warpAffine(image,M,(h,w))
    plt.imsave('1r'+str(i)+'.png',img90)
print("완료")
cv2.waitKey(0)
cv2.destroyAllWindows()