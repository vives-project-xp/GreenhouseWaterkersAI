import labelbox as lb
import urllib.request
from PIL import Image
import time
import json
import os
import csv

# Creat a new client
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbTIzMDl0bTAwNHU0MDd5NzZxYWNmOXJyIiwib3JnYW5pemF0aW9uSWQiOiJjbTIzMDl0bGowNHUzMDd5N2hzZXI4OXYxIiwiYXBpS2V5SWQiOiJjbTJkY2xsZ2UwZGc5MDd3bzJiOTBoN2kyIiwic2VjcmV0IjoiZjdhOGVkZjRmYWVmNGExYTlkZmE3NWFhOGIzYzM5NWIiLCJpYXQiOjE3MjkxNzIzOTgsImV4cCI6MjM2MDMyNDM5OH0.SMpeYzwJRLb5lJLGZ6JnOzbGpl-eumI0nHhNT7IHWAM'
client = lb.Client(API_KEY)

# Insert the project id
PROJECT_ID = 'cm2ogxkej00pz07xyagvu7u0n'
project = client.get_project(PROJECT_ID)

# Export params to include/export certain fields
export_params = {
    "attachments": True,
    "metadata_fields": True,
    "data_row_details": True,
    "project_details": True,
    "label_details": True,
    "performance_details": True,
    "interpolated_frames": True,    
}

filters = {

    "workflow_status": "Done"
}

# Export the data rows
export_task = project.export_v2(params=export_params, filters=filters)
export_task.wait_until_done()

if export_task.errors:
    print(export_task.errors)
    
# Find the repo root, assuming script is inside the repo
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ensure JSON and image paths are relative to repo root
json_file_path = os.path.join(repo_root, 'LabelboxScripts', 'output_labelbox.json')
output_dir = os.path.join(repo_root, 'LabelboxScripts', 'watercress_images')

export_json = export_task.result
# print("Result: ", export_json)
# save the JSON to a file
with open(json_file_path, 'w') as json_file:
    json.dump(export_json, json_file, indent=4)

# Create a directory to save the images
os.makedirs(output_dir, exist_ok=True)

# Prpare the COCO dataset structure
coco_format = {
    "info": {
        "description": "Labelbox Export",
        "url": "https://labelbox.com",
        "version": "1.0",
        "contributor": "Labelbox",
        "date_created": time.strftime("%Y-%m-%d %H:%M:%S")
    },
    "categories": [
        {"id": 1, "name": "BoundingBox"},
    ],
    "images": [],
    "annotations": []
}

image_id_counter = 0
annotation_id_counter = 0

# process each item in the JSON data to create the COCO dataset
for item in export_json:
    data_row = item.get('data_row', {})
    image_name = data_row.get('external_id', 'N/A')
    media_attributes = item.get('media_attributes', {})
    image_width = media_attributes.get('width', 0)
    image_height = media_attributes.get('height', 0)
    image_id_counter += 1

    # Add the image to the COCO dataset
    coco_format["images"].append({
        "id": image_id_counter,
        "file_name": image_name,
        "width": image_width,
        "height": image_height
    })

    # Process the labelbox annotations for this image
    annotations = item.get('projects', {}).get(PROJECT_ID, {}).get('labels', [])
    for label in annotations:
        for object in label.get('annotations', {}).get('objects', []):
            if object.get('annotation_kind', 'N/A') == "ImageBoundingBox":
                annotation_id_counter += 1
                bounding_box = object.get('bounding_box', {})
                x_min = bounding_box.get('left', 0)
                y_min = bounding_box.get('top', 0)
                bbox_width = bounding_box.get('width', 0)
                bbox_height = bounding_box.get('height', 0)

                # Add the annotation data to the COCO dataset
                coco_format["annotations"].append({
                    "id": annotation_id_counter,
                    "image_id": image_id_counter,
                    "category_id": 1,  # Assuming BoundingBox category ID is 1
                    "bbox": [x_min, y_min, bbox_width, bbox_height],
                })
    # # Download the image
    # try:
    #     urllib.request.urlretrieve(row_data_url, output_path)
    #     print(f"Image saved as: {output_path}")
    # except Exception as e:
    #     print(f"Error downloading {external_id}: {e}")

# Save the COCO dataset to a JSON file
coco_json_path = os.path.join(output_dir, 'labels.coco.json')
with open(coco_json_path, 'w') as coco_json_file:
    json.dump(coco_format, coco_json_file, indent=4)

print("COCO JSON file saved as labels.coco.json")