import os
# potential advantage compared to Pathlib rglob is that
# rglob can fail completely if a single file name is
# too long on windows.
# Using os.walk, you could probably use 'try' to just
# omit that single file and continue listing the
# other file names.

target = 'C:\\Users\\wiebe\\Pictures\\printen Lotte'

file = open('list_of_file_names.txt', 'w')
for root, dirname, files in os.walk(target):
    for x in files:
        file.write(root + '\\' + x + '\n')

file.close()