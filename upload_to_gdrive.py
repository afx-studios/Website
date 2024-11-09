import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

print("Starting Google Drive upload process...")

# Authenticate using the service account key
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'service_account.json'

try:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)
    print("Authenticated with Google Drive API successfully.")
except Exception as e:
    print(f"Failed to authenticate with Google Drive API: {e}")
    exit(1)

# File metadata
file_metadata = {
    'name': 'website.zip',
    'parents': ['YOUR_FOLDER_ID']  # Replace 'YOUR_FOLDER_ID' with the actual Google Drive folder ID
}

# Check if website.zip exists before upload
if not os.path.isfile('website.zip'):
    print("Error: website.zip does not exist.")
    exit(1)

media = MediaFileUpload('website.zip', mimetype='application/zip')

try:
    # Upload the file
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f"File uploaded successfully with ID: {file.get('id')}")
except Exception as e:
    print(f"Failed to upload file: {e}")
    exit(1)
