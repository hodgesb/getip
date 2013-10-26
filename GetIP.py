# --- GetIP.py by Bob Hodges - October 2013 ---

import urllib2
import re

# Open up website and save HTML to rawHTML variable
#wSite = urllib2.urlopen('http://checkip.org')
#rawHTML = wSite.read()

def FindIP():
	
   try:
	# Open up website and save HTML to rawHTML variable
	global wSite
	wSite = urllib2.urlopen('http://checkip.org')

	global rawHTML 
	rawHTML = wSite.read()

	# Find the IP address entries and save them to ipList
	ipList = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',rawHTML)
	
	# Populate ipAddress with the first IP found on the page.
	ipAddress =  ipList.group(0)
	return ipAddress

   except:

	# Error handler
	print '[-] An error occured, please check your internet connection.'
	exit(0)

def FindCity():

	cityList = re.search('City: \w{0,40}',rawHTML)
	cityName = cityList.group(0)
	return cityName
 
def Main():

   myIP = FindIP()
   myCity = FindCity()
   print '[+] Your public IP address is ' + myIP
   print '[+] ' + myCity

if __name__ == "__main__":

   Main()

