class funcs: 
    def __init__(self, name, params): 
        self.name = name 
        self.params = params

flist = []

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
no_punct = ""

qbfile = open("flaskr/functions/funcalc.py", "r")
Lines = qbfile.readlines()
count = 0
for line in Lines:
    l = Lines[count].strip()
    pos = l.find("def ")
    if pos >= 0:
        print(l)        
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
        flist.append( funcs(fname,fparam))
        # print(no_punct.split())
        # print (flist[0].name)
        # print (flist[0].params)
    count += 1

f = 0
while f < len(flist):
    print (flist[f].name)
    print (flist[f].params)
    f += 1

qbfile.close()