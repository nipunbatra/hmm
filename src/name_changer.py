import os

dir_name = "images/backtracking_gif"

files = os.listdir(dir_name)

files.sort()

for cnt,i in enumerate(files):
		file_name = os.path.join(dir_name,i)
		os.rename(file_name,os.path.join(dir_name,str(cnt+1)+".pdf"))