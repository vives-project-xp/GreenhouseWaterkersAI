import labelbox as lb
import urllib.request
from PIL import Image
import time
import json

# Creat a new client
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbTIzMDl0bTAwNHU0MDd5NzZxYWNmOXJyIiwib3JnYW5pemF0aW9uSWQiOiJjbTIzMDl0bGowNHUzMDd5N2hzZXI4OXYxIiwiYXBpS2V5SWQiOiJjbTJkY2xsZ2UwZGc5MDd3bzJiOTBoN2kyIiwic2VjcmV0IjoiZjdhOGVkZjRmYWVmNGExYTlkZmE3NWFhOGIzYzM5NWIiLCJpYXQiOjE3MjkxNzIzOTgsImV4cCI6MjM2MDMyNDM5OH0.SMpeYzwJRLb5lJLGZ6JnOzbGpl-eumI0nHhNT7IHWAM'
client = lb.Client(API_KEY)

# Insert the project id
PROJECT_ID = 'cm23kaijl09t107ymbvqjgqx4'
project = client.get_project(PROJECT_ID)

# Export params to include/export certain fields
export_params = {
    "attachments": True,
    "metadata_fields": True,
    # "embeddings": True,
    "data_row_details": True,
    "project_details": True,
    "label_details": True,
    "performance_details": True,
    # "interpolated_frames": True,    
}

# Filters to filter the data rows
# Note: Filters follow AND logic
filters = {
    # "last_activity_at": ["2000-01-01 00:00:00", "2050-01-01 00:00:00"],
    # "label_created_at": ["2000-01-01 00:00:00", "2050-01-01 00:00:00"],
    # "global_keys": ["<global_key>", "<global_key>"],
    # "data_row_ids": ["<data_row_id>", "<data_row_id>"],
    # "batch_ids": ["<batch_id>", "<batch_id>"],
    "workflow_status": "Done"
}

# Export the data rows
export_task = project.export_v2(params=export_params, filters=filters)
export_task.wait_until_done()

if export_task.errors:
    print(export_task.errors)

export_json = export_task.result
print("Result: ", export_json)

# Function to handle the JSON stream
def json_stream_handler(output: lb.BufferedJsonConverterOutput):
    print(output.json)


if export_task.has_errors():
    export_task.get_buffered_stream(stream_type=lb.StreamType.ERRORS).start(
        stream_handler=lambda error: print(error))

if export_task.has_result():
    export_json = export_task.get_buffered_stream(
        stream_type=lb.StreamType.RESULT).start(
            stream_handler=json_stream_handler)

print(
    "file size: ",
    export_task.get_total_file_size(stream_type=lb.StreamType.RESULT),
)
print(
    "line count: ",
    export_task.get_total_lines(stream_type=lb.StreamType.RESULT),
)

# Convert the JSON to a dictionary
if export_task.errors:
    with open('Python scripts/JSONFileErrors.txt', 'w') as error_file:
        json.dump(export_task.errors, error_file, indent=4)
    print("Errors saved to errors.txt")
else:
    print("No errors found.")

# Check if the export task has results and save them to result.txt
if export_task.has_result():
    export_json = export_task.result
    with open('Python scripts/JSONFileResults.txt', 'w') as result_file:
        json.dump(export_json, result_file, indent=4)
    print("Results saved to result.txt")
else:
    print("No results found.")
