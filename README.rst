================
Python-resumable
================

Well, in order to explain what is Python-resumable we have to explain what is ResumableJS. ResumableJS is a JavaScript library providing multiple simultaneous, stable and resumable uploads via the HTML5 File API. And python-resumable is a universal hookup for resumablejs. We'd like to create an interface that works regardless of which framework you use.

It has a universal hookup, that takes chunks as base64 strings, and currently it has a Flask-specific hookup that takes Flask file objects. We'd like to add Pyramid and Django hooks.

======
Usage
======

It's rather simple to use. It has to take 5 Resumable headers, your upload and tmp directory and file data as well.

Here's a simple Flask example.

```python

from flask import Flask, request, jsonify
from python_resumable import FlaskUploader


app = Flask(__name__)

@app.route('/uploads', methods=['GET'])
def check_status():
    """This route works with get checks from resumable"""

    request = flask.request

    resumable_dict = {
        'resumableIdentifier': request.form.get('resumableIdentifier'),
        'resumableFilename': request.form.get('resumableFilename'),
        'resumableTotalSize': request.form.get('resumableTotalSize'),
        'resumableTotalChunks': request.form.get('resumableTotalChunks'),
        'resumableChunkNumber': request.form.get('resumableChunkNumber')
    }

    resumable = FlaskUploader(resumable_dict,
                              settings.UPLOAD_FOLDER_PROJECTS,
                              settings.UPLOAD_FOLDER_TMP,
                              flask.request.files['file'])

    if resumable.chunk.exists() is True:
        return jsonify({"chunkUploadStatus": True})

    return jsonify({"chunkUploadStatus": False})


@app.route('/uploads', methods=['POST'])
def upload_file():
    request = flask.request

    resumable_dict = {
        'resumableIdentifier': request.form.get('resumableIdentifier'),
        'resumableFilename': request.form.get('resumableFilename'),
        'resumableTotalSize': request.form.get('resumableTotalSize'),
        'resumableTotalChunks': request.form.get('resumableTotalChunks'),
        'resumableChunkNumber': request.form.get('resumableChunkNumber')
    }

    resumable = FlaskUploader(resumable_dict,
                              '/home/user/uploads',
                              '/home/user/tmp',
                              flask.request.files['file'])

    resumable.upload_chunk()
    
    if resumable.check_status() is True:
        resumable.assemble_chunks()
        return jsonify({"fileUploadStatus": True,
                        "resumableIdentifier": resumable.repo.file_id})

    return jsonify({"chunkUploadStatus": True,
                    "resumableIdentifier": resumable.repo.file_id})
```

Well... As simple as it could actually get with Resumable.

==============
Mini-reference
==============

This package provides you with two usable classes -- Uploader and FlaskUploader. They are essentially identical, except for the type of chunk-data they take.

Arguments on creation:

* ```resumable_dict```: contains Resumable data in a dictionary form, namely: ```'resumableIdentifier', 'resumableFilename', 'resumableTotalSize', 'resumableTotalChunks', 'resumableChunkNumber'```
* ```upload_dir```: contains path to your final directory where the file will be assembled.
* ```tmp_dir```: contains path to temporary directory, where it will store the chunks.
* ```chunk_data```: contains data transfered with the chunk. Uploader takes generic b64 strings, FlaskUploader takes Flask file objects.

Attributes:

* ```Chunk```: Stores chunk-related data. For full inforamtion -- refer to the full reference.
* ```Repository```: Stores data related to the end file. For full inforamtion -- refer to the full reference.

Methods:

* ```upload_chunk```: If chunk already exists returns False, else saves chunk to ```tmp_dir/resumableId/chunk_name``` and returns True.
* ```check_status```: If all chunks are in tmp returns True, else returns False.
* ```assemble_chunks```: Assembles all of the chunks in your ```upload_dir```. If filename is not specified uses resumableFilename.
* ```cleanup```: Deletes all the data from ```tmp_dir/resumableId```.


Full reference can be found in docstrings.

=====
Links
=====

.. _a ResumableJS: http://www.resumablejs.com/