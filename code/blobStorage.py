from code import app
import os
import json
from flask import request
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService, PublicAccess
from code.subject import Subject

class BlobStorage(Subject):
    def __init__(self):
        self.accountName = "expressiveblob"
        self.accountKey = "F2G8lu/eZ6PduDIJFksWvuItZdhf+GONR2wgwgSsJMUO4s0mMdFI6PiC7K7ypcMSOH6m5kPhn2C9ketBRQiyKA=="
        super().__init__()
        
    def connect(self):
        return BlockBlobService(account_name=self.accountName, account_key=self.accountKey)

@app.route("/getBlobImages")

def getBlobImages():
    blobStorage = BlobStorage()
    block_blob_service = blobStorage.connection
    generator = block_blob_service.list_blobs('images')
    blobList = []
    for blob in generator:
        blobList.append(blob.name)
    return json.dumps(blobList)

@app.route("/getBlobVideos")

def getBlobVideos():
    blobStorage = BlobStorage()
    block_blob_service = blobStorage.connection
    generator = block_blob_service.list_blobs('videos')
    blobList = []
    for blob in generator:
        blobList.append(blob.name)
    return json.dumps(blobList)

@app.route("/uploadBlobImage", methods=['GET', 'POST'])

def uploadBlobImage():
    if request.method == 'POST':
        try:
            file = request.files['imageFile']
            if file:
                filename = secure_filename(file.filename)
                blobStorage = BlobStorage()
                block_blob_service = blobStorage.connection
                container = 'images'
                block_blob_service.create_blob_from_stream(container, filename, file)
                return "Success"
            else:
                return "Invalid File"
        except Exception as e:
            return e
    else:
        return "Error"

@app.route("/uploadBlobVideo", methods=['GET', 'POST'])

def uploadBlobVideo():
    if request.method == 'POST':
        try:
            file = request.files['videoFile']
            if file:
                filename = secure_filename(file.filename)
                blobStorage = BlobStorage()
                block_blob_service = blobStorage.connection
                container = 'videos'
                block_blob_service.create_blob_from_stream(container, filename, file)
                return "Success"
            else:
                return "Invalid File"
        except Exception as e:
            return e
    else:
        return "Error"
    
