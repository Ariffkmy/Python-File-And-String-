import os
import re

title = '<title>'
ref = 'Shared Content: <span>'
word = 'Shared Content: <span>Forsikringsnummer</span>'
word2 = 'Shared Content: <span>CPR-nummer</span>'

# Folder Path

path = r"C:\\Users\\bf7433\\OneDrive - Danske Bank A S\\Desktop\\CCMScrap"

# Change the directory

os.chdir(path)

 

# Read text File

def read_text_file(file_path):

    with open(file_path, 'r') as fp:

#       print(f.read())

            lines = fp.readlines()

           
            for line in lines:

        # check title

                if line.find(title) != -1:

                        result = re.search('<title>(.*)</title>', line)

                        print(result.group(1))

 

        # check ref number forsikrings

               

                if line.find(word) != -1:

                        #for line in lines:

                         #if line.find(word) != -1:

                         print('Forsikringsnummer:',lines.index(line))

 

        # check ref number cpr-nummer

               

                if line.find(word2) != -1:

                        #for line in lines:

                         #if line.find(word) != -1:

                         print('CPR-nummer:',lines.index(line))    

 

            print('-------------------------------------------')
            # iterate through all file

            for file in os.listdir():

        # Check whether file is in text format or not

             if file.endswith(".html"):

                file_path = f"{path}\{file}"

 

            # call read text file function

            read_text_file(file_path)

               

 

print('completed')

 