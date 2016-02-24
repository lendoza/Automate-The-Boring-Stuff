import os

for folderName, subfolders, filenames in os.walk('/Users/leonardlabita/Desktop'):
    print('The folder is ' + folderName)
    print('The subfolders in' + folderName + ' are:' + str(subfolders))
    print('The file names in ' + folderName + ' are:' + str(filenames))
    print

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print ('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.txt'):
            # os.remove()

# os.walk() allows us be specific with changing/removing/moving files
