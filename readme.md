# Data Preparation from Labelbox json file Pipeline

A complete Python pipeline for downloading, processing, and visualizing dental pathology segmentation masks from Labelbox-annotated panoramic X-rays.

## Project Structure
- `annotations.ndjson` — Place your ndjson file contents here obtained from labelbox after completion of annotation.
- `download_masks_with_classes.py` — Download per-class masks from Labelbox with class labels in filenames.
- `merging_masks.py` — Merge multiple masks into a single multi-class mask per image.
- `color_coded_visualization.py` — Visualize masks with distinct colors for Caries, PARL, and Impacted Tooth.
- `overlay_original_and_masks.py` — Overlay color-coded masks onto original grayscale X-rays.
- `confirm_annotations.py` — Analyze and plot pixel distribution per class.
- `config.py` — Global paths and label settings.
- `.env_Sample` — Sample environment file for storing Labelbox API key.
- `.gitignore` — Ignore Python cache, environment files, etc.


## ✅ Pipeline Summary
1. Authenticate with Labelbox and download instance masks
2. Merge masks into multi-class PNGs
3. Smooth masks with Gaussian blur
4. Color-code masks for visual inspection
5. Overlay masks on original images for anatomical alignment

## Author
**Aashish Ghimire**

---

