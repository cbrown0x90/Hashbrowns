infile = "stuff.txt"
outfile = "out.txt"

fin = open(infile)
fout = open(outfile, "w+")
delete = False
for line in fin:
    if ("</a>]" in line and delete):
        delete = False
        line = ""
    if ("[<a " in line or delete):
        delete = True
        line = ""
    if ("This post was edited by" in line):
        line = ""
        
    fout.write(line)
fin.close()
fout.close()
