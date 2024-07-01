##leftpad with loop
def makepad(string, totalspace, left=True, padder=chr(0)):
    ##(String to resize, what size to resize to, add chars on the left?, what string to use as padding default: null)
    output=""
    if totalspace-len(string)>0:
        totalspace-=len(string)
        for x in range(1,totalspace,len(character)):
            output+=character
        for x in range(0,totalspace%len(character)):
            output+=character[x]
        if(left==True):
            output+=string
        else:
            output=string+output
    else:
        for x in range(0,totalspace):
            output+=string[x]
    return output
print(makepad("abecadlo",120,False,"O"))
