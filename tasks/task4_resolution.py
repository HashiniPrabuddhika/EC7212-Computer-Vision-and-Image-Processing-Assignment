import cv2
import numpy as np

def reduce_spatial_resolution(image, block_size):
    h, w = image.shape[:2]
    output = image.copy()
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            roi = image[y:y+block_size, x:x+block_size]
            color = roi.mean(axis=(0, 1)).astype(int)
            output[y:y+block_size, x:x+block_size] = color
    return output