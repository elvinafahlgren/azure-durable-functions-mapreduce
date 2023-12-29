import os
import tempfile
from azure.storage.blob import BlobServiceClient


def download_blob(blob_service_client, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        temp_filename = tmp_file.name
        download_stream = blob_client.download_blob()
        tmp_file.write(download_stream.readall())
    return temp_filename

def main(context):
    try:
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

        container_name = "blobstorecontainer"

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        container_client = blob_service_client.get_container_client(container_name)

        blob_list = container_client.list_blobs()
    
        input_data = []

        line_nr = 0

        for blob in blob_list:
            blob_name = blob.name
            file_path = download_blob(blob_service_client, container_name, blob_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    input_data.append((line_nr, line.strip()))
                    line_nr += 1

            os.remove(file_path)

        return input_data

    except Exception as e:
        print('Exception:')
        print(e)
