#!/bin/env python

infile = "stuff.txt"
outfile = "out.txt"

fin = open(infile)
fout = open(outfile, "w+")
delete = False
for line in fin:
    if "Edited by" in line:
        line = ""
    if "[<a " in line:
        line = ""
    if "nike roshe" in line:
        line = ""
    if "This post was edited by" in line or "poke poke poke" in line:
        line = ""
        
    fout.write(line)
fin.close()
fout.close()
