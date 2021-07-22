import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = dropbox.files.WriteMode.overwrite)

def Main():
    access_token = 'GDjunTEVJscAAAAAAAAAAYvEtwAcOlVPxi2kvsMglvU2AoNvCtAO6cQdN81Mrx22'
    transferData = TransferData(access_token)
    fileFrom = str(input('Enter the file path you wish to transfer: '))
    fileTo = input('Enter the path how you want to upload on dropbox: ')
    transferData.upload_file(fileFrom, fileTo)
    print('Your file has been moved to dropbox!')

Main()