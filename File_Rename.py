import os
import glob

path = 'C:/Users/Anayat/CloudStation/PycharmProjects/CodeWars'
os.chdir(path)

def renamer():
    for old_file in glob.glob('*.py'):
        new_name = old_file.replace(')','')
        os.renames(old_file,new_name)

renamer()
