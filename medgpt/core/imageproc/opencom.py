import cv2 as cv


def loader(path):
    img = cv.imread(path)
    return img


def show(img):
    cv.imshow('showtime', img)
    cv.waitKey(0)
    cv.destroyAllWindows()  # Close all OpenCV windows after a key is pressed


image_path = ("J:\\Xite development\\MedGPT\\medgpt\\media\\chat\\images\\rosof97990@jucatyo.com\\Screenshot "
              "2024-02-17 214638_ozXKm6q.png")
img = loader(image_path)
show(img)
