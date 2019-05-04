# FilePatternCopy
Sample python project to copy files of specific pattern with * wild char from a folder to a given destination path

## Introduction:
  This sample python project can be used for copying files using wild character from a source folder to a given destination folder.
## Points to remember:
1. the program accepts three input string parameters *src_path,destination_path,pattern*
2. the *pattern* should always contain a "*" (wild char) 
3. the program will copy files only when there is necessary permissions for the user to copy it else it will error out with reason.
4. the files will be copied as is from the source folder.

## Usage:
```
usage: filepatterncopy.py [-h] [-s SRC] [-d DST] [-p PATTERN]

optional arguments:
  -h, --help            show this help message and exit
  -s SRC, --src SRC     provide the src folder path
  -d DST, --dst DST     provide the destination folder path
  -p PATTERN, --pattern PATTERN
                        pattern to be searched needs to be provided
```
#### Example:
```
python filepatterncopy.py -s '/src/folder/path' -d '/dst/folder/path' -p '*.txt'
```
## Tech stack details:
python 2.7 +
