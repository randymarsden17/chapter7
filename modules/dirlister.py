#!/usr/bin/python
import os

def run(**args):

	print "[*] In dirlister module."
	files = oslistdir(".")

	return str(files)
