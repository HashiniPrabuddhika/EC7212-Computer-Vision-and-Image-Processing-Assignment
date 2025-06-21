import os

from tasks.utils import load_image_cv, get_grayscale_image_cv, show_images
from tasks.task1_intensity import reduce_intensity_levels
from tasks.task2_averaging import apply_average_filter_cv
from tasks.task3_rotation import rotate_image_cv
from tasks.task4_resolution import reduce_spatial_resolution

def run_all_tasks():
    print("Starting Image Processing Project...")

    image_path = 'input_image.jpg'
    results_dir = 'results_opencv'

    original_image_color = load_image_cv(image_path)
    if original_image_color is None:
        print(f"Error loading image from {image_path}")
        return

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    print("\nRunning Task 1: Intensity Level Reduction")
    original_gray = get_grayscale_image_cv(original_image_color)
    levels = [16, 4, 2]
    reduced = [reduce_intensity_levels(original_gray, k) for k in levels]
    show_images([original_gray] + reduced, 
                ['Original'] + [f'{k} Levels' for k in levels], 
                os.path.join(results_dir, 'task1_intensity.png'))

    print("\nRunning Task 2: Spatial Averaging")
    kernels = [3, 10, 20]
    blurred = [apply_average_filter_cv(original_image_color, k) for k in kernels]
    show_images([original_image_color] + blurred,
                ['Original'] + [f'{k}x{k}' for k in kernels],
                os.path.join(results_dir, 'task2_averaging.png'))

    print("\nRunning Task 3: Rotation")
    rot90 = rotate_image_cv(original_image_color, 90)
    rot45 = rotate_image_cv(original_image_color, 45)
    show_images([original_image_color, rot90, rot45],
                ['Original', 'Rotated 90°', 'Rotated 45°'],
                os.path.join(results_dir, 'task3_rotation.png'))

    print("\nRunning Task 4: Spatial Resolution Reduction")
    blocks = [3, 5, 7]
    pixelated = [reduce_spatial_resolution(original_image_color, b) for b in blocks]
    show_images([original_image_color] + pixelated,
                ['Original'] + [f'{b}x{b}' for b in blocks],
                os.path.join(results_dir, 'task4_resolution.png'))

    print(f"\nAll tasks complete. Results saved in '{results_dir}'.")

if __name__ == '__main__':
    run_all_tasks()