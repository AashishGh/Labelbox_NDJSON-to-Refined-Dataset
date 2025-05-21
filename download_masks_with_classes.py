import json
import requests
import os
from config import API_KEY

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

ndjson_file = 'annotations.ndjson'
mask_folder = 'masks_with_classes2'
os.makedirs(mask_folder, exist_ok=True)

# Map annotation "value" field to human-readable class names
class_mapping = {
    'caries': 'caries',
    'parl': 'PARL',
    'it': 'IT'
}

with open(ndjson_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    rec = json.loads(line)
    img_name = rec["data_row"]["external_id"].replace('.bmp', '')
    
    projects = rec.get("projects", {}).values()
    for project in projects:
        labels = project.get("labels", [])
        for label in labels:
            annotations = label.get("annotations", {}).get("objects", [])
            for idx, obj in enumerate(annotations):
                mask_url = obj["mask"]["url"]
                defect_type_raw = obj.get("value", "unknown").lower()
                defect_type = class_mapping.get(defect_type_raw, "unknown")
                
                # Generate filename clearly including defect type
                mask_filename = f"{img_name}_{defect_type}_{idx+1}.png"
                mask_path = os.path.join(mask_folder, mask_filename)

                # Download mask
                response = requests.get(mask_url, headers=headers)
                if response.status_code == 200:
                    with open(mask_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {mask_filename}")
                else:
                    print(f"Failed ({response.status_code}): {mask_filename}")
