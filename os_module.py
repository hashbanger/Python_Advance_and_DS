#Learning the OS module
import os
'''
#To get the list of all accessible functions of the modules 
print(dir(os))

#To get the current directory
print(os.getcwd())
#To change the directory
os.chdir('C:/Users/prash/Desktop')
print(os.getcwd())

#To list content of directory
print(os.listdir())

#To make a directory 
os.mkdir('C:/Users/prash/Desktop/Hell') #Puts out error if find an unexisting directory in path
os.makedirs('C:/Users/prash/Desktop/Hel/lo') #Creates the subdirectories even if not existing

os.rmdir('C:/Users/prash/Desktop/Hel/lo') #Does not remove intermediate sub directories
os.removedirs('C:/Users/prash/Desktop/Hel/lo') #removes intermediate directories

#To rename a file
os.rename('C:/Users/prash/Desktop/Hel/lo/x.txt', 'C:/Users/prash/Desktop/Hel/xx.txt')

#To get the details of a file
print(os.stat('C:/Users/prash/Desktop/Hello/adam.py'))
#Can also ask for specific details like modification time 
print(os.stat('C:/Users/prash/Desktop/Hello/adam.py').st_mtime)
#To convert the gibberish numbers into readable format
from datetime import datetime
filetime = os.stat('C:/Users/prash/Desktop/Hello/adam.py').st_mtime
print(datetime.fromtimestamp(filetime))


#We use os.walk which return a three values tuple
for dirpath, dirnames, filenames in os.walk('C:/Users/prash/Desktop/'):
    print('Dirpath: ',dirpath)
    print('Dirnames: ',dirnames)
    print('Filename: ', filenames)
    print()

#We can get our system's environmental variables using
print(os.environ.get('HOMEPATH')) 

#We can join two paths using the os.path.join
#that way we don't require to keep guess the slashes
print(os.path.join(os.environ.get('HOMEPATH'),'f.txt'))
#We can use it to create a file or something like that'''

#To get the base element of a path
print(os.path.basename(r'C:\Users\prash\X.txt'))
#To get the directory name of a  file
print(os.path.dirname(r'C:\Users\prash\X.txt'))    
#To get both
print(os.path.split(r'C:\Users\prash\X.txt'))
#To check the existence of a file
print(os.path.exists(r'C:\Users\prash\X.txt'))
#To check whether a file or directory
print(os.path.isdir(r'C:\Users\prash\X.txt'))
print(os.path.isfile(r'C:\Users\prash\Desktop\hello\adam.py'))
#To split the file and it s extension
print(os.path.splitext(r'C:\Users\prash\Desktop\hello\adam.py'))