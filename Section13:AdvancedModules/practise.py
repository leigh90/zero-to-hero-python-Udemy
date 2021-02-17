'This is a test string'

# SHELL UTILITY(shutil) MODULE AND OS MODULE

# # OPENING AND CLOSING FILES
# f = open('practise.txt','w+')
# f.write('This is a test stringoo')
# f.close()



# # OS Module
import os

# # list my current working directory
# print(os.getcwd())
# # list files and folders in my current directory
# print(os.listdir())
# # list files and folders in a specific directory
# print(os.listdir('/home/leigh'))
# # deletes a file at the path you provide
# os.unlink(path)
# # deletes an empty folder at the specified path
# os.rmdir(path)
# # deletes all files and folder in a specified path
# os.rmtree(path)
# # please note that all these methods are permanent and should only b used if you are absolutely sure otherise use send2trash (install via pip)



# SHUTIL Module
# import shutil
# shutil.move('practise.txt','/home/leigh/Udemy/Zero-To-Hero-Python')
# shutil.move('/home/leigh/Udemy/Zero-To-Hero-Python/practise.txt',os.getcwd())


# import send2trash
# send2trash.send2trash('/home/leigh/Udemy/Zero-To-Hero-Python/practise.txt')

file_path = '/home/leigh/Udemy/Zero-To-Hero-Python'

for folder, sub_folders, files in os.walk(file_path):
    print(f'Currently looking at {folder}')
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f'\t Subfolder: {sub_fold}')
        print('\n')
        print('the files are: ')
        for f in files:
            print(f'\t File: {f}')
            print('\n')




