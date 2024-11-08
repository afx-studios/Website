import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

# Authenticate using the service account key
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'service_account.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

# File metadata
file_metadata = {
    'name': 'website.zip',
    # Replace 'YOUR_FOLDER_ID' with your actual folder ID
    'parents': [https://drive.google.com/drive/folders/1SVkt3dApccibTbPINYla0hcZ9d7sxhX_]
}

media = MediaFileUpload('website.zip', mimetype='application/zip')

# Upload the file
file = drive_service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()

print(f"File ID: {file.get('id')}")
