import cv2
img = cv2.imread("C:\\Users\\hrtripathi\\Desktop\\DSCN4584.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_inv = 255 - gray
blur = cv2.GaussianBlur(gray_inv, ksize=(21, 21),sigmaX=0, sigmaY=0)
def dodge(image, mask):
  return cv2.divide(image, 255-mask, scale=256)
def burn(image, mask):
  x = cv2.divide(255-image, 255-mask, scale=256)
  return 255-x
blend1 = dodge(gray,blur)
blend = burn(gray, blur)
t = cv2.add(blend1,blend)
temp = cv2.resize(t,(0,0),fx=0.5,fy=0.5)
cv2.imshow("pencil sketch", temp)
cv2.waitKey(1000000)
