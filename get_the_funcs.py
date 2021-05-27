import glob
import sys
import json
import ntpath
import os
import jinja2

flaskdir = "flaskr"
funcdir = flaskdir + "/functions"

def get_file_funcs(filename):
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
            j = { "FunctionFile": ntpath.basename(os.path.splitext(filename)[0]), "FunctionName": fname, "Parameters": fparam}
            jlist.append(j)
        count += 1
    # print(json.dumps(jlist))
    qbfile.close()
    return jlist

def process_files(fileList):
    functionList = []
    # fileList = []
    numargs = len(sys.argv)
    a = 1
    while a < numargs:
        arg = sys.argv[a]
        if len(arg) > 0:
            fileList.append(arg)
        a += 1
    # print(fileList)

    numFiles = len(fileList)
    f = 0
    while f < numFiles:
        listOfFunctions = get_file_funcs(fileList[f])
        b = 0
        while b < len(listOfFunctions):
            functionList.append(listOfFunctions[b])
            b += 1
        f += 1
    # print(json.dumps(functionList))
    return functionList

funcfiles = glob.glob(funcdir + "/*.py")
i = 0
while i < len(funcfiles):
    # print(str(funcfiles[i]).strip())
    i += 1
x = process_files(funcfiles)
print(json.dumps(x, indent=2))

# print(x[0]['FunctionName'])

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
t = env.get_template("main.py.j2")
print(t.render(funcfiles=x))