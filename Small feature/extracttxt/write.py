# -*- coding:utf-8 -*-   
import os
import linecache
dirs = []
txt_list = []
index = 1
def readnumlines(num,fp):
	global index
	print index
	lines = ""
	print linecache.getline("./out.txt",1)
	for x in range(index,num+index):
		line = linecache.getline("./out.txt",x)
		txt_list.append(line)
	index += num
	print index
		
def mkFolder(paths):
    if not os.access(paths, os.R_OK):
        path_last= len(paths)-1;
        if paths[path_last] == '/' or paths[path_last] == '\\':
            paths= paths[0:path_last];
            mkFolder(os.path.dirname(paths))
        if not os.path.isfile(paths):
            os.mkdir(paths)
            
            	
if __name__ == "__main__":
	fp = open("./out.txt",'r')
	#
	config = open("./config.txt",'r')
	for line in config.readlines():
		#config
		num = line.split('#')[0]
		name = line.split('#')[1]
		print name
		
		#name
		length = len(name) -1
		name = name[0:length]

		dirs = name.split('/')
		path = ""
		for i in range(len(dirs)-1):
			path += dirs[i] + '/'
		mkFolder(path)
		print name.split('/')
		filename = open(name,'w')
		readnumlines(int(num),fp)
		filename.writelines(txt_list)
		filename.close()
		txt_list = []
	fp.close()
	