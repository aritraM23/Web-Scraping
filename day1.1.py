#create a file
"""
#open a file
#give name + extension
#run

fo=open("C:\\Example\\exm.txt",'a')
fo.write("jfuehqfuwhfuewhfuesah\n")

#createa list of items you want to write
line_list=["hello\n","jkra\n","harkhkf\n","sgyfaagu\n"]
#writelines() is for mutitple lines
fo.writelines(line_list)

#one file has data for starting 15 days of a month
#other file has data for next 15 days of a month
#you want to udate the data in the older file.

#open the first file in a mode
#open the second file in r mode
#read data from second file
#append the read data in the first file
#close both of the files

ff=open("C:\\Users\\Aritra Marik\\Desktop\\newtxtfile.txt",'a')
sf=open("C:\\Example\\exm.txt",'r')
info=sf.read()
ff.write(info)
ff.close()
sf.close()"""

#moving a file
# change the location of a file
#make new directory=> os.mkdir("new_directory_path")

import os
import shutil

#os.mkdir("C:\\NewDir\\")
#shutil.move("C:\\Example","C:\\NewDir\\")

#shutil.copy("C:\\NewDir\\exm.txt","C:\\NewDir\\Example\\")

# copy multiple files
# for every file copy it.
"""
file_list=["C:\\Users\\Aritra Marik\\Dropbox\\Screenshots\\Screenshot 2020-05-12 14.38.04.png","C:\\Users\\Aritra Marik\\Dropbox\\Screenshots\\Screenshot 2020-05-13 12.46.06.png"]
for file in file_list:
	shutil.copy(file,"C:\\NewDir\\Example\\")
"""
#os.rename("C:\\Users\\Aritra Marik\\Dropbox\\Screenshots\\Screenshot 2020-05-12 14.38.04.png","C:\\Users\\Aritra Marik\\Dropbox\\Screenshots\\Marcelo Bielsa.png")
os.remove("C:\\NewDir\\Example\\Screenshot 2020-05-12 14.38.04.png")
