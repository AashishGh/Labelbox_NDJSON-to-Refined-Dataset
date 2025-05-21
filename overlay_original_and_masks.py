import cv2
import os

# Input folders
image_folder = 'images'
mask_folder = 'color_coded_masks_from_combined'
output_folder = 'overlays'
os.makedirs(output_folder, exist_ok=True)

# Loop through all masks
for mask_file in os.listdir(mask_folder):
    if not mask_file.endswith('.png'):
        continue

    base_name = mask_file.replace('_mask_color.png', '')
    image_path = os.path.join(image_folder, f'{base_name}.bmp')
    mask_path = os.path.join(mask_folder, mask_file)

    if not os.path.exists(image_path):
        print(f"Image not found for: {base_name}")
        continue

    # Read grayscale X-ray and color-coded mask
    xray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    color_mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)

    # Resize mask to match image if needed
    if xray.shape[:2] != color_mask.shape[:2]:
        color_mask = cv2.resize(color_mask, (xray.shape[1], xray.shape[0]), interpolation=cv2.INTER_NEAREST)

    # Convert grayscale X-ray to 3-channel for blending
    xray_3ch = cv2.cvtColor(xray, cv2.COLOR_GRAY2BGR)

    # Blend images: adjust alpha/beta for transparency
    blended = cv2.addWeighted(xray_3ch, 0.7, color_mask, 0.3, 0)

    # Save the result
    output_path = os.path.join(output_folder, f'{base_name}_overlay.png')
    cv2.imwrite(output_path, blended)
    print(f"Overlay saved: {output_path}")
