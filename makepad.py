def makepad(string, totalspace, left=True, character=chr(0)):
    ##(String to resize, what size to resize to, add chars on the left?, what char to use default: null)
    if len(character) >1:
        print ("error the character has to be exactly 1 char long")
        quit()
    output=""
    if totalspace-len(string)>0:
        totalspace-=len(string)
        for x in range(0,totalspace):
            output+=character
        if(left==True):
            output+=string
        else:
            output=string+output
    else:
        for x in range(0,totalspace):
            output+=string[x]
    return output
print(makepad("Demo string",12,False,"O"))
