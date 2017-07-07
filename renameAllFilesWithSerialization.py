import glob, os

def rename(dirPath,count, file_name):
    for f in  glob.glob(dirPath+"*"):
        title, ext = os.path.splitext(os.path.basename(f))
        #print title
        #print file_name
        if file_name in title:
        	print file_name + title
        	os.rename(f, os.path.join(dirPath, str(count)+". " +os.path.basename(f)))
                   


dirPath = '/home/ankit/aawork/video lecture/python practical machine learning/'
name_file = open('list')
ln = 0
data = ""
count  = 0
for line in name_file:
	ln+=1
	if(ln%4!=1):
		continue;
	count+=1;	
	data = data+line.rstrip()
	rename(dirPath,count,line.rstrip())	
	

