import cv2
import numpy as np
import os

# Paths to your mask folder and output folder
mask_folder = 'combined_masks'
visualization_folder = 'color_coded_masks_from_combined'
os.makedirs(visualization_folder, exist_ok=True)

# Define your custom HEX colors (converted to BGR for OpenCV)
colors = {
    0: [0, 0, 0],                  # Background (black)
    1: [255, 243, 28],             # Caries (#1cf3ff -> BGR)
    2: [255, 52, 255],             # PARL (#FF34FF -> BGR)
    3: [70, 74, 255]               # IT (#FF4A46 -> BGR)
}

for mask_file in os.listdir(mask_folder):
    if mask_file.endswith('.png'):
        mask_path = os.path.join(mask_folder, mask_file)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # Create an empty color visualization image
        visual_mask = np.zeros((*mask.shape, 3), dtype=np.uint8)

        # Apply the color mapping
        for class_id, color in colors.items():
            visual_mask[mask == class_id] = color

        # Save the color-coded mask
        output_path = os.path.join(visualization_folder, mask_file.replace('.png', '_color.png'))
        cv2.imwrite(output_path, visual_mask)

        print(f"Color-coded mask saved: {output_path}")
