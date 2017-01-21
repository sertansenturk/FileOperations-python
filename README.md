# fileoperations_python
A repository fo simple I/O operations

Usage
=======
Currently, it only consists of a two functions:

```python
from fileoperations.fileoperations import get_filenames_in_dir

# recursively gets all the names of the files below a directory
fullnames, folders, names = get_filenames_in_dir(
    dir_name, keyword='*.mp3', skip_foldername='', match_case=True, 
    verbose=False)

# Inputs:
# dir_name          : the foldername
# keyword           : the keyword to search
# skip_foldername   : an optional foldername to skip searching
# match_case        : flag for case matching
# verbose           : verbose flag

# Outputs:
# fullnames         : list of the fullpaths of the files found
# folder            : list of the folders of the files
# names             : list of the filenames without the foldername
```

Installation
=======

You can easily install the package using pip. In terminal:

    cd path/to/fileoperations-python
    pip install .
    
Don't forget to change the folder path with the correct path in your machine.

If you want to be able to edit files and have the changes be reflected, then install the repository like this instead:

    cd path/to/fileoperations-python
    pip install -e .

Authors
=======

Sertan Şentürk	contact@sertansenturk.com
