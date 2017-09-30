from os import path
from base64 import decodebytes


class Chunk(object):
    '''
    Contains all the chunk info.

    Attributes:
        chunk_number
        chunk_data
        chunk_name
        chunk_path

    chunk_name is (repo_dict['file_id'] + '.' +
                   resumable_dict['resumableChunkNumber'])
    '''

    def __init__(self, chunk_dict):
        self.chunk_number = chunk_dict['chunk_number']
        self.chunk_data = chunk_dict['chunk_data']
        self.chunk_name = chunk_dict['chunk_name']
        self.chunk_path = chunk_dict['chunk_path']

    def save(self):
        '''
        This writes chunk data to disk, while decoding it.
        '''
        self.chunk_data = self.chunk_data.encode()
        chunk_file = open(path.join(self.chunk_path, self.chunk_name))
        chunk_file.write(decodebytes(self.chunk_data))

    def exists(self):
        '''
        This checks if chunk already exists or not.
        '''
        return path.exists(path.join(self.chunk_path, self.chunk_name))


class FlaskChunk(Chunk):
    def save(self):
        '''
        This writes flask file object to disk.
        '''
        self.chunk_data.save(path.join(self.chunk_path, self.chunk_name))
