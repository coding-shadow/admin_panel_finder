#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import requests

url = raw_input("Enter the website (eg:www.someurl.com) : ")


def main():
	global link
	f = open('link.txt',"r")
	f = f.readlines()
	welcome()
	print("[*] Website : {}".format(url))
	print "[*] Loaded {} links".format(len(f))
	print("[*] Finding admin panel.......\n")
	for link in f:
		link = link.replace("\n","")
		attack(url,link)


def welcome():
	info = """
       +=========================================+
       |..........   Facebook Crack   ...........|
       +-----------------------------------------+
       |        			               		 | 
       |	      #Author: Coding Shadow 	     |
       |	                                     |
       +=========================================+
       |..........  Facebook Cracker  ...........|
       +-----------------------------------------+\n\n
"""
	print info

def attack(url,link):
	urls = 'http://' + url + '/' + link
	req = requests.get(urls,headers = {"User-agent":"Firefox"})
	if req.ok == True:
		print("\n[*] Link Found = {}".format(urls))

if __name__ == '__main__':
	main()
