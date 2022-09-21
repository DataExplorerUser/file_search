from pathlib import Path

def tree(directory, search_term):

    print(f'\nSearching the search term {search_term} for all files in folder: {directory} ')
    for path in sorted(directory.rglob(f'*{search_term}*')):

        if path.is_file():
            print(f'{path}') # (len(str(path)))
    print('Search process finished.')

folder_str = Path(r'C:\')
search_term = 'Hello'
path = Path(folder_str)

tree(path, search_term)


# FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\Windows\\System32\\OpenSSH\\'
# That's cause by using python-32bit. Installing 64-bit python will solve the problem.
# Problem is caused by a path that is longer than 258 characters. As a result, the path name will skip
# 'normalization' and begin with \\?\
# Don’t stress about path normalization: just use pathlib.Path whenever you need to represent a file path.


# Normally, any path passed to a Windows API is (effectively) passed to the GetFullPathName function and normalized
# There is one important exception: a device path that begins with a question mark instead of a period.
# Unless the path starts exactly with \\?\ (note the use of the canonical backslash), it is normalized.
#
# Why would you want to skip normalization? There are three major reasons:
#
# To get access to paths that are normally unavailable but are legal. A file or directory called hidden.,
# for example, is impossible to access in any other way.
#
# To improve performance by skipping normalization if you've already normalized.
#
# On .NET Framework only, to skip the MAX_PATH check for path length to allow for paths that are greater
# than 259 characters. Most APIs allow this, with some exceptions.