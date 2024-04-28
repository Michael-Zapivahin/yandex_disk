from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Drive:
    def __int__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.folder_id = 'YOUR_FOLDER_ID'

    def connect(self):
        self.drive = GoogleDrive(self.gauth)

    def get_list_files(self, folder_id):
        self.folder_id = folder_id
        self.file_list = self.drive.ListFile({'q': f"'{self.folder_id}' in parents and trashed=false"}).GetList()
        files = []
        for file in self.file_list:
            files.append(
                {
                    'title': file['title'],
                    'id': file['id'],
                }
            )
        return files


