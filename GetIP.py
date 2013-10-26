# --- GetIP.py by Bob Hodges - October 26th 2013 ---

import urllib2
import re

def FindIP():
	
   try:
	# Open up website and save HTML to rawHTML variable
	global wSite
	wSite = urllib2.urlopen('http://checkip.org')

	global rawHTML 
	rawHTML = wSite.read()

	# Find the IP address entries and save them to ipList
	ipList = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',rawHTML)
	
	# Populate ipAddress with the first IP in the ipList variable.
	ipAddress =  ipList.group(0)
	return ipAddress

   except:

	# Error handler
	print '[-] An error occured, please check your internet connection.'
	exit(0)

def Main():

   myIP = FindIP()
   print '[+] Your public IP address is ' + myIP

if __name__ == "__main__":

   Main()

