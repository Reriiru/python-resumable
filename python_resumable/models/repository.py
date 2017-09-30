from os import path, mkdir


class Repository(object):
    '''
    Contains all the file info needed.
    '''

    def __init__(self, repo_dict):

        self.tmp_dir = repo_dict['tmp_dir']
        self.upload_dir = repo_dict['upload_dir']
        self.total_chunks = repo_dict['total_chunks']
        self.file_id = repo_dict['file_id']
        self.filename = repo_dict['filename']
        self.total_size = repo_dict['total_size']

    def file_exists(self):
        '''
        This checks if file already exists in upload directory.
        '''
        return path.exists(path.join(self.upload_dir, self.file_id))

    def dir_exists(self):
        '''
        This checks if tmp-directory for your file already exists.
        '''
        return path.exists(path.join(self.tmp_dir, self.file_id))

    def mkdir(self):
        '''
        This creates tmp-directory.
        '''
        mkdir(path.join(self.tmp_dir, self.file_id), 0o755)
