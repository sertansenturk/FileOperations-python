# fileoperations-python
A repository fo simple I/O operations

Currently it only consists of a single function, which recursively gets all the names of the files below a directory. 

Usage
=======

```python
from fileoperations.fileoperations import getFileNamesIndDir

fullnames, folders, names = getFileNamesInDir(dir_name, keyword='*.mp3', skip_foldername='', 
                                              matchCase=True, verbose=False)

# Inputs:
# dir_name          : the foldername
# keyword	          :	the keyword to search
# skip_foldername   : an optional foldername to skip searching
# match_case        : flag for case matching
# verbose           : verbose flag

# Outputs:
# fullnames         : list of the fullpaths of the files found
# folder            : list of the folders of the files
# names             : list of the filenames without the foldername
```

Authors
=======

Sertan Şentürk	contact@sertansenturk.com
