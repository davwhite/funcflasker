import sys
import json
numargs = len(sys.argv)
arglist = str(sys.argv)
# print(arglist.split())
filename = sys.argv[1]

class funcs: 
    def __init__(self, name, params): 
        self.name = name 
        self.params = params

# flist = []
jlist = []

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
no_punct = ""

qbfile = open(filename, "r")
Lines = qbfile.readlines()
count = 0
for line in Lines:
    l = Lines[count].strip()
    pos = l.find("def ")
    if pos >= 0:
        no_punct = ""
        for char in l:
            if char not in punctuations:
                no_punct = no_punct + char        
            else:
                no_punct = no_punct + " "
        fname = no_punct.split()[1]
        fparam = []
        i = 2
        while i < len(no_punct.split(" ")):
            p = no_punct.split(" ")[i]
            if (len(p) > 0):
                fparam.append(p)
            i += 1
        j = { "FunctionName": fname, "Parameters": fparam}
        jlist.append(j)
    count += 1
print(json.dumps(jlist))
qbfile.close()