#!/usr/bin/env python3

name = input("Enter a file name:")

fobj = open(name)

print(fobj.read())

fobj.close()
