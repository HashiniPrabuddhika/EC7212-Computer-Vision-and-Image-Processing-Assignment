import cv2

def apply_average_filter_cv(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))