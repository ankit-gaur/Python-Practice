import sys

if(len(sys.argv)!=4):
	print 'four arguments required'

file = open(str(sys.argv[1]), "rb")
outFile = open(str(sys.argv[2]), "w")
key  = str(sys.argv[3]) # string of any size


try:
    byte = file.read(1)
    count = 0
    while byte != "":
    	if(count == len(key)):
    		count = 0
    	keychar = ord(key[count])	
        newByte = ord(byte) ^ keychar
        outFile.write(chr(newByte))
        byte = file.read(1)
        count += 1
finally:
    file.close()

outFile.close()
