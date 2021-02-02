import cv2

imgnum = 1

for i in range(200):
    image = cv2.imread(str(imgnum)+".png")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(str(imgnum)+".png", gray_image)

    imgnum = imgnum + 1

# image = cv2.imread(str(imgnum)+".png")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imwrite(str(imgnum)+".png", gray_image)
