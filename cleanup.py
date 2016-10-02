#!/bin/env python

infile = "7chan.txt"
outfile = "7out.txt"

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
    if "This post was edited by" in line or "poke poke poke" in line or "......" in line or "http://" in line or "#" in line or "https://" in line:
        line = ""

        
    fout.write(line)
fin.close()
fout.close()
