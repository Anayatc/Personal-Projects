import os

def rename_files():
    file_list = os.listdir(r'/Users/Anayat/Desktop/l')
    os.chdir(r'/Users/Anayat/Desktop/l')
    for file_name in file_list:
        renamed = ''.join([i for i in file_name if not i.isdigit()])
        os.rename(file_name,renamed)





rename_files()


'''
this program will remove numbers from file names, by renaming the files to remove numbers if present
'''