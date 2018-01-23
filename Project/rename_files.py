import os
import re

current_dir = os.getcwd()
file_list = os.listdir('./renameFiles')
print(current_dir)
print(file_list)
os.chdir('./renameFiles')
for file_name in file_list:
    print(file_name)
    print(re.sub(r'([\d]+)','',file_name))
    os.rename(file_name,re.sub(r'([\d]+)','',file_name))
os.chdir(current_dir)
