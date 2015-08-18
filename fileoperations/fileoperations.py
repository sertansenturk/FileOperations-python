import os

def getFileNamesInDir(dir_name, audio_ext = '.mp3', skip_foldername = ''):
	names = []
	folders = []
	fullnames = []
	print dir_name

	if not os.path.isdir(dir_name):
		print 'Directory doesn\'t exist!'
		return [], [], []
	dir_name = dir_name[:-1] if dir_name[-1] == '/' else dir_name
	for (path, dirs, files) in os.walk(dir_name):
		for f in files:
			if f.lower()[-len(audio_ext):] == audio_ext:
				if skip_foldername not in path.split(os.sep)[1:]:
					folders.append(unicode(path, 'utf-8'))
					names.append(unicode(f,'utf-8'))
					fullnames.append(os.path.join(path,f))

	print "> Found " + str(len(names)) + " files."
	return fullnames, folders, names
