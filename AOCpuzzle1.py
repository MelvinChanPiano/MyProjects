def mid(s, offset, amount):
 return s[offset:offset+amount]

def left(s, amount):
 return s[:amount]
#the 1st row, 1st column, last row, last column are all counted, then -4, because of overlapping trees.
def OutTrees():
   RowCount = 0
   ColCount = 0
   
   for line in open("a.txt") :
       line = line.strip()
       for i in line:
        ColCount += 1
       RowCount += 1
   
   return ((RowCount+int(ColCount/RowCount))*2 - 4)

#Check for upper, lower, right and left number (row).
#Take all the right hand side of the character, make it an array.
def checkright(line,charpos,rownum) :
    R = True
    Right = []
    Current = line[rownum][charpos]
    for charpos in range(charpos,100):
   
      Right.append(mid(line[rownum],charpos+1, 1)) # extracting the right lines and then storing them into an array
      if Right[-1] == "" or Right[-1] == "\n":
         Right.pop()
   
    #print ("Right",Right)
   
    # for i in range(len(Right)):     # part 1
    #     if Right[i] >= Current :
    #        R = False
    #     elif Right == []:
    #        R = True
    # return R

    #part 2
    Total = Checkarray(Right,Current)
    #print ("Current : ",Current)
   
    return Total
             

 # 1st parameter from the readline statement. 2nd parameter from the loop statement, loop to rowcount - 1.

 # just opposite to the checkright function.

def checkleft(line,charpos,rownum) :
    L = True
    Left = []
   
    # for count in range(0,charpos):
    x = left(line[rownum],charpos)
    for i in x:
        Left.append(i)
    #   Left.append(mid(line[rownum],charpos-count, 1)) # extracting the left lines and then storing them into an array
        if Left[0] == "\n" or Left[0] == "":
         Left.remove(Left[0])
   
    # print("Left",Left)
    Current = line[rownum][charpos]
    # for i in range(len(Left)):     part 1
    #     if Current <= Left[i] :
    #        L = False
    #     elif Left == []:
    #        L = True
    # return L

    Left.reverse()
    #print (Left)
    Total = Checkarray(Left,Current)
    return Total
    #print ("Current : ",Current)
   
     
def checkupper(lines,charpos,rownum):
    Upper = True
    Up = []
    for i in range (0,rownum) :
       Up.append(lines[i][charpos])
       Current = lines[rownum][charpos]
   
    # for i in range(len(Up)):  part 1
    #     if Up[i] >= Current :
    #        Upper = False
    #     elif Up == []:
    #        Upper = True
       
    # return Upper
    Up.reverse()
    #print (Up)
    Total = Checkarray(Up,Current)
    return Total
   
    # print ("Current : ",Current)
   
def checklower(lines,charpos,rownum) :
   
    Lower = True
    Low = []
    for i in range(rownum , len(lines) ) :
        Low.append(lines[i][charpos])
   
    Current = lines[rownum][charpos]
   
    Low.remove(Low[0])
    # print ("Low",Low)
    # for i in range(len(Low)):
    #     if Low[i] >= Current :
    #        Lower = False
    #     elif Low == []:
    #        Lower = True
    # return Lower
   
    #print(Low)
    Total = Checkarray(Low,Current)
    #print ("Current : ",Current)
    return Total

#Collecting all the Booleans from all the directions. If all True, then increment count.
# def Calcount(R,L,U,D):       this is not needed
#     Count = OutTrees()
#     if R is True or L is True or U is True or D is True :
#        Count += 1
#     print (Count)

def Checkarray (Array, Current):
    Total = 0
    Stop = False
    i = 0
    while Stop is False :
      if i == len(Array):
         Stop = True
      elif Array[i] < Current:
       Total += 1
      elif Array[i] == Current:
         Total += 1
         Stop = True
      elif Array[i] >= Current :
         Stop = True
         Total += 1
      else :
         Stop = True
      i += 1
    return Total
 
def main():
    f = open ("c.txt","r")
    lines = f.readlines()
    Count = 0
    highest = 0
    for charpos in range (0,99):
       for rownum in range (0,99) :
       
         R = checkright(lines,charpos,rownum)
         L = checkleft(lines,charpos,rownum)
         U = checkupper(lines,charpos,rownum)
         D = checklower(lines,charpos,rownum)
         sum = R*L*U*D
         if sum > highest:
            highest = sum
    print (highest)
            # if (R is True) or (L is True) or (U is True) or (D is True) :    part 1
            #  Count += 1
            #  print (R,L,U,D,"\n")
    #print(Count)
main()
