import os
import subprocess

#Put svn_dir_path as main directory path where you have all you subversion checkedout directories
svn_dir_path ='/Users/ashutosh.kumar/Documents/dev/workspace'
folders = list(filter(lambda x: os.path.isdir(os.path.join(svn_dir_path, x)), os.listdir(svn_dir_path)))
print(folders)

for folder in folders:
    svn_path = svn_dir_path+'/' + folder
    print("Working on " + folder + " directory")
    subprocess.run(["svn", "update", svn_path])

