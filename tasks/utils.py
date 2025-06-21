import cv2
import matplotlib.pyplot as plt

def load_image_cv(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    return image

def get_grayscale_image_cv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def show_images(images, titles, save_path=None):
    plt.figure(figsize=(15, 5))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i+1)
        if len(img.shape) == 2:
            plt.imshow(img, cmap='gray')
        else:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img_rgb)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()