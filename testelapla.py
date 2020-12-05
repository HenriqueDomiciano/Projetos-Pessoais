import cv2 
image=cv2.imread(r'C:\Users\Dell\Downloads\imagens\pensando.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY,cv2.CV_8U)
new_image=cv2.Laplacian(image,ksize=3,ddepth=cv2.CV_8U)
cv2.imshow('val',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

