import os
import urllib.request
import json
import csv

# Map waar je de afbeeldingen wilt opslaan
output_dir = "./watercress_images"
os.makedirs(output_dir, exist_ok=True)

# Laad het JSON-bestand met data van de Labelbox-export
with open('result.txt', 'r') as file:
    data = json.load(file)

# CSV-bestand aanmaken om de koppelingen op te slaan
csv_file_path = "imageAnnotations.csv"
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    # Schrijf de headers naar het CSV-bestand
    csv_writer.writerow(["Image ID", "External ID", "Image URL", "Object Name", "Annotation Type", "Annotation Details"])

# Download de afbeeldingen en sla ze op
for item in data:
    data_row = item.get('data_row', {})
    row_data_url = data_row.get('row_data', 'N/A')
    external_id = data_row.get('external_id', 'N/A')
    image_id = data_row.get('id', 'N/A')

    # Bestandsnaam instellen voor het opslaan
    output_path = os.path.join(output_dir, external_id)

    # Download de afbeelding
    # try:
    #     urllib.request.urlretrieve(row_data_url, output_path)
    #     print(f"Afbeelding opgeslagen als: {output_path}")
    # except Exception as e:
    #     print(f"Fout bij het downloaden van {external_id}: {e}")

    # Verwerk de annotaties die bij deze afbeelding horen
    annotations = item.get('projects', {}).get('cm23kaijl09t107ymbvqjgqx4', {}).get('labels', [])
    for label in annotations:
        for obj in label.get('annotations', {}).get('objects', []):
            object_name = obj.get('name', 'N/A')
            annotation_kind = obj.get('annotation_kind', 'N/A')
            annotation_details = ""

            if annotation_kind == "ImageSegmentationMask":
                mask_url = obj.get('mask', {}).get('url', 'N/A')
                annotation_details = f"Mask URL: {mask_url}"
            elif annotation_kind == "ImageBoundingBox":
                bbox = obj.get('bounding_box', {})
                top = bbox.get('top', 'N/A')
                left = bbox.get('left', 'N/A')
                height = bbox.get('height', 'N/A')
                width = bbox.get('width', 'N/A')
                annotation_details = f"Top: {top}, Left: {left}, Height: {height}, Width: {width}"

            # Schrijf de gegevens naar het CSV-bestand
            with open(csv_file_path, mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                csv_writer.writerow([image_id, external_id, row_data_url, object_name, annotation_kind, annotation_details])

print(f"De annotatiegegevens zijn opgeslagen in {csv_file_path}")