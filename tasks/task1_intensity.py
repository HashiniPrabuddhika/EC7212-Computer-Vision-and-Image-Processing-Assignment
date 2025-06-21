import numpy as np

def reduce_intensity_levels(gray_image, levels):
    if not (levels & (levels - 1) == 0 and 2 <= levels <= 256):
        raise ValueError("Levels must be a power of 2 between 2 and 256.")
    factor = 256 // levels
    new_value_multiplier = 255 // (levels - 1)
    reduced_image = (gray_image // factor) * new_value_multiplier
    return reduced_image.astype(np.uint8)