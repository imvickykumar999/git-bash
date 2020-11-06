import os
import requests

from morse import solve as s
print('\n>>>\t', s(''))

print('\n1). git init')
os.system('git init')

print('\n2). git add .')
os.system('git add .')

file = input('\nWrite "selected" to upload selected files (or, Press ENTER to Upload All...) : ')
if file == 'selected':
    file = open('to_upload.txt', 'r').read()[:-1]

print('\n3). git commit -m "Adding files"')
os.system('git commit '+ file +' -m "Adding files"')

print('\n4). git remote add origin https://github.com/...')
username = input("Enter the github Username : ")
# if username == '':
#     usename = 'imvickykumar999'

reponame = input('Enter Existing Repository : ')
# if reponame == '':
#     reponame = 'git-bash'
os.system('git remote add origin https://github.com/'+username+'/'+reponame+'.git')

print('\n5). git pull origin master')
os.system('git pull origin master')

print('\n6). git push origin master')
return_force = os.system('git push --force origin master')

if not return_force:
    os.system('index.html')
