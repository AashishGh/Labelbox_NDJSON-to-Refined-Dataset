import numpy as np
import cv2
import os
import glob

input_folder = 'masks_with_classes'
output_folder = 'combined_masks'
os.makedirs(output_folder, exist_ok=True)

class_ids = {
    'caries': 1,
    'PARL': 2,
    'IT': 3
}

mask_files = glob.glob(os.path.join(input_folder, '*.png'))
image_bases = set('_'.join(os.path.basename(f).split('_')[:2]) for f in mask_files)

for image_base in image_bases:
    combined_mask = None

    relevant_masks = [f for f in mask_files if f.startswith(os.path.join(input_folder, image_base+'_'))]

    target_size = None  # To ensure all masks match the same size

    for mask_path in relevant_masks:
        mask_filename = os.path.basename(mask_path)
        defect_type = mask_filename.split('_')[-2]

        class_id = class_ids.get(defect_type, 0)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        if mask is None:
            print(f"Warning: Could not read mask {mask_filename}")
            continue

        # Set target_size based on the first mask
        if target_size is None:
            target_size = (mask.shape[1], mask.shape[0])  # width, height
            combined_mask = np.zeros((target_size[1], target_size[0]), dtype=np.uint8)
        
        # Resize mask if dimensions differ
        if (mask.shape[1], mask.shape[0]) != target_size:
            mask = cv2.resize(mask, target_size, interpolation=cv2.INTER_NEAREST)
            print(f"Resized mask {mask_filename} to match dimensions {target_size}")

        combined_mask[mask == 255] = class_id

    if combined_mask is not None:
        output_path = os.path.join(output_folder, f"{image_base}_mask.png")
        cv2.imwrite(output_path, combined_mask)
        print(f"Combined mask created: {output_path}")
