#!/usr/bin/python
# Script to clean and orgnize files on a Mac
# Author: Troy Wilson
# Date: 06-08-17
#
import os

count_mp3 = 0
count_doc = 0
count_pdf = 0
count_md = 0
count_jpg = 0
count_png = 0
count_jpeg = 0


junk = '/Users/troywilson/testing/junk'
Desktop = '/Users/troywilson/Desktop'
Documents = '/Users/troywilson/Documents'
Downloads = '/Users/troywilson/Downloads'
Movies = '/Users/troywilson/Movies'
Music = '/Users/troywilson/Music'
Pictures = '/Users/troywilson/Pictures'

dirs = [junk, Desktop, Documents, Downloads, Movies, Music, Pictures]

for dir in dirs:
    for root, dirs, files in os.walk(dir):
        for file in files:

            # Music Files
            if file.endswith(".mp3"):
                count_mp3 += 1
                print(os.path.join(root, file))

            # Word Documents
            if file.endswith(".doc"):
                count_doc += 1
                print(os.path.join(root, file))

            # Markup/PDF Documents
            if file.endswith(".pdf"):
                count_pdf += 1
                print(os.path.join(root,file))
            if file.endswith(".md"):
                count_md += 1
                print(os.path.join(root,file))
            
            # Photos
            if file.endswith(".jpg"):
                count_jpg += 1
                print(os.path.join(root,file))
            if file.endswith(".jpeg"):
                count_jpeg += 1
                print(os.path.join(root,file))
            if file.endswith(".png"):
                count_png += 1
                print(os.path.join(root,file))

#print '\n'            
print "Number of *.mp3:", count_mp3
print "Number of *.doc:", count_doc
print "Number of *.pdf:", count_pdf
print "Number of *.md:", count_md
print "Number of *.jpg:", count_jpg
print "Number of *.png:", count_png
print "Number of *.jpeg:", count_jpeg


#move = ""
#print "Would you like to move these files? [y/n]", move








