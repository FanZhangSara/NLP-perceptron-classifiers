import sys
import re
file1 = sys.argv[2]

import json
with open(sys.argv[1],"r") as f:
    data = f.read()
    model = data.split('\n')
    vaweightTrueOrFake = json.loads(model[0])
    vaweightPosOrNeg = json.loads(model[1])
    listchara = json.loads(model[2])
# dict =model[0]
# dictletter = model[1]
# listchara = model[2]
array = listchara['arrayb']
#print("dictdictdict")

def deal(word):
    for x in range(3,len(word)):
        rule = re.compile(r'[^a-zA-z]')
        word[x] = rule.sub("",word[x])
        word[x] = word[x].lower()

def countnumfunc(word):
    countword = {}
    for x in range(1,len(word)):
        if word[x] in countword:
            countword[word[x]]+=1
        else:
            countword[word[x]]=1
    return countword


file=open("percepoutput.txt","w")
# with open("dev-text.txt") as f:
with open(file1) as f:
    content = f.readlines();
    for x in content:
        x = x.strip('\n')
        word = x.split(" ")
        deal(word)
        countword = countnumfunc(word)
        value = 0
        value1 = 0
        value += array[0]
        value1 += array[1]
        file.write(word[0])
        file.write(" ")
        for x in countword:
            if x in vaweightTrueOrFake:
                value += vaweightTrueOrFake[x]*countword[x]
            if x in vaweightPosOrNeg:
                value1 += vaweightPosOrNeg[x]*countword[x]
        if value > 0:
            file.write("True")
        else:
            file.write("Fake")

        file.write(" ")

        if value1 > 0:
            file.write("Pos")
        else:
            file.write("Neg")
        file.write('\n')


file.close()