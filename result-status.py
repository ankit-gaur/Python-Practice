import urllib
import urllib2 as url
import os




page = ""
while True:
	#req = url.Request("http://cbseresults.nic.in/");
	req = url.Request("http://upsee.nic.in/publicinfo/public/home.aspx");
	response = url.urlopen(req)
	data = str(response.read())
	print data
	if page != data and len(page)!=0:
		print len(data) - len(page)
		page = data
		print page
		os.popen2("cvlc /home/ankit/Desktop/twentyonepilots/heavydirtysoul.mp3 --play-and-exit")
	
	if len(page) == 0 :
		page = data	
		print page		


			
