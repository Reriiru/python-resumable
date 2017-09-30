from os import path, listdir
from glob import glob
from python_resumable.models import Repository, Chunk, FlaskChunk
from shutil import copyfileobj, rmtree

from natsort import natsorted


class Uploader(object):
    def __init__(self, resumable_dict, upload_dir, tmp_dir, chunk_data):
        '''
        This class takes:
        resumable data, namely:
                              resumableFilename
                              resumableIdentifier
                              resumableTotalSize
                              resumableTotalChunks
                              resumableChunkNumber

        Takes it as a dict.

        It also takes upload and tmp directories. These are self-explanatory.

        It takes a base64 string, as that is universal for form data.
        '''

        repo_dict = {
            'file_id': resumable_dict['resumableIdentifier'],
            'filename': resumable_dict['resumableFilename'],
            'tmp_dir': tmp_dir,
            'upload_dir': upload_dir,
            'total_size': resumable_dict['resumableTotalSize'],
            'total_chunks': resumable_dict['resumableTotalChunks']
        }

        chunk_name = (repo_dict['file_id'] + '.' +
                      resumable_dict['resumableChunkNumber'])

        chunk_dict = {
            'chunk_number': resumable_dict['resumableChunkNumber'],
            'chunk_data': chunk_data,
            'chunk_name': chunk_name,
            'chunk_path': path.join(tmp_dir, repo_dict['file_id'])
        }

        # repo data
        self._repo = None
        self.repo = repo_dict
        # chunk data
        self._chunk = None
        self.chunk = chunk_dict

        if path.exists(self.chunk.chunk_path) is False:
            self.repo.mkdir()

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, value):
        self._repo = Repository(value)

    @property
    def chunk(self):
        return self._chunk

    @chunk.setter
    def chunk(self, value):
        self._chunk = Chunk(value)

    def upload_chunk(self):
        '''
        This tries to save chunk data.

        If chunk already exists returns False as the indication,
        otherwise returns True.
        '''
        if self.chunk.exists() is True:
            return False

        self.chunk.save()
        return True

    def check_status(self):
        '''
        This returns True if all the chunks are uploaded.
        '''
        if int(self.repo.total_chunks) > len(listdir(self.chunk.chunk_path)):
            return False
        else:
            return True

    def assemble_chunks(self, filename=None):
        '''
        This puts the file all into one thing. Then it puts it into upload dir.

        By default resulting filename will be resumableFilename. If you wanna
        change it for some random hash-based name or whatevs -- use filename
        positional argument.
        '''
        if filename is None:
            destination = path.join(self.repo.upload_dir, self.repo.filename)
        else:
            destination = path.join(self.repo.upload_dir, filename)

        destination = open(destination, 'wb')

        tmp_list = glob(path.join(self.chunk.chunk_path, '*'))
        tmp_list = natsorted(tmp_list, reverse=False)

        for self.repo.filename in tmp_list:
            copyfileobj(open(self.repo.filename, 'rb'), destination)

        destination.close()

    def cleanup(self):
        '''
        Deletes all the data from tmp_dir.
        '''
        rmtree(self.chunk.chunk_path)


class UploaderFlask(Uploader):
    '''
    This one takes flask file object instead of form data.

    Everything else is same as Uploader.
    '''
    @property
    def chunk(self):
        return self._chunk

    @chunk.setter
    def chunk(self, value):
        self._chunk = FlaskChunk(value)
