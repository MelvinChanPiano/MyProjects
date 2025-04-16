#open the command file. Get the commands(direction) and the steps.
# global arr

def GetHead(Array):
    for i in range (0,500):
       for j in range (0,500):
          if Array[i][j].Head == "H":
             Headrow = i
             Headcolumn = j
           
             return Headrow,Headcolumn

def GetTail(Array):
    for i in range (0,500):
       for j in range (0,500):
          if Array[i][j].Tail == "T":
             Tailrow = i
             Tailcolumn = j

             return Tailrow,Tailcolumn
   

def moveRight(Array,step):
 
  for i in range(step):
     
     Headrow, HeadColumn = GetHead(Array)  #finding the position of the head and tail
     Tailrow, TailColumn = GetTail(Array)
     #print (Headrow,HeadColumn,Tailrow,TailColumn)
   
     Array[Headrow][HeadColumn].Head = " "
     HeadColumn += 1                 #removing head
     Array[Headrow][HeadColumn].Head = "H"   #moving head to the right
   
     if Headrow == Tailrow and TailColumn == HeadColumn-1 :  
        pass
       
     elif Headrow == Tailrow and TailColumn == HeadColumn-2 :
       Array[Tailrow][TailColumn].Tail = " "
       TailColumn += 1
       Array[Tailrow][TailColumn].Tail = "T"   #move right together with the head
       Array[Tailrow][TailColumn].value = True

   
     elif TailColumn == (HeadColumn - 2) and Tailrow < Headrow:          # if above
        Array[Tailrow][TailColumn].Tail = " " #removing tail
        TailColumn += 1       #moving diagonally down right
        Tailrow += 1
        Array[Tailrow][TailColumn].value = True
        Array[Tailrow][TailColumn].Tail = "T"

   
     elif TailColumn == (HeadColumn - 2) and Tailrow > Headrow: #if below
          Array[Tailrow][TailColumn].Tail = " "
          TailColumn += 1
          Tailrow -= 1
          Array[Tailrow][TailColumn].Tail = "T"
          Array[Tailrow][TailColumn].value = True
       
     
     #output (Array)
 



def moveLeft(Array,step):
  #just opposite to moveright
    for i in range(step):
       Headrow, HeadColumn = GetHead(Array)  #finding the position of the head and tail
       Tailrow, TailColumn = GetTail(Array)
       #print (Headrow,HeadColumn,Tailrow,TailColumn)

       Array[Headrow][HeadColumn].Head = " "
       HeadColumn -= 1                 #removing head
       Array[Headrow][HeadColumn].Head = "H" #Head moving left
       if Headrow == Tailrow and TailColumn == HeadColumn+1 :      #same position
        pass

       elif Headrow == Tailrow and TailColumn == HeadColumn+2 :
          Array[Tailrow][TailColumn].Tail = " "
          TailColumn -= 1
          Array[Tailrow][TailColumn].Tail = "T"
          Array[Tailrow][TailColumn].value = True
         
       elif TailColumn == (HeadColumn + 2) and Tailrow < Headrow:          # if above right
         Array[Tailrow][TailColumn].Tail = " "
         TailColumn -= 1
         Tailrow += 1
         Array[Tailrow][TailColumn].Tail = "T"   #move left together with the head
         Array[Tailrow][TailColumn].value = True

       elif TailColumn == (HeadColumn + 2) and Tailrow > Headrow: #if below
         Array[Tailrow][TailColumn].Tail = " "
         TailColumn -= 1
         Tailrow -= 1
         Array[Tailrow][TailColumn].Tail = "T"
         Array[Tailrow][TailColumn].value = True
         
       #output (Array)




def moveUp(Array,step):  
       #same as left but rotated
       for i in range(step):
          Headrow, HeadColumn = GetHead(Array)  #finding the position of the head and tail
          Tailrow, TailColumn = GetTail(Array)
          # print (Headrow,HeadColumn,Tailrow,TailColumn)
          Array[Headrow][HeadColumn].Head = " "
          Headrow -= 1                 # moving up
          Array[Headrow][HeadColumn].Head = "H"

          if HeadColumn == TailColumn and Tailrow == Headrow + 1:
             pass
           
          elif HeadColumn == TailColumn and Tailrow == Headrow+2 :
            Array[Tailrow][TailColumn].Tail = " "
            Tailrow -= 1
            Array[Tailrow][TailColumn].Tail = "T"
            Array[Tailrow][TailColumn].value = True
         
          elif Tailrow == (Headrow + 2) and TailColumn < HeadColumn:          # if down left
             Array[Tailrow][TailColumn].Tail = " "
             Tailrow -= 1
             TailColumn += 1
             Array[Tailrow][TailColumn].Tail = "T"   #move left together with the head
             Array[Tailrow][TailColumn].value = True

          elif Tailrow == (Headrow + 2) and TailColumn > HeadColumn: #if down right
             Array[Tailrow][TailColumn].Tail = " "
             Tailrow -= 1
             TailColumn -= 1
             Array[Tailrow][TailColumn].Tail = "T"
             Array[Tailrow][TailColumn].value = True
         # output (Array)


def moveDown(Array,step):
  #same as right but rotated
  for i in range(step):
     Headrow, HeadColumn = GetHead(Array)  #finding the position of the head and tail
     Tailrow, TailColumn = GetTail(Array)
     # print (Headrow,HeadColumn,Tailrow,TailColumn)
   
     Array[Headrow][HeadColumn].Head = " "
     Headrow += 1                 #removing head
     Array[Headrow][HeadColumn].Head = "H"   #moving head down
   
     if HeadColumn == TailColumn and Tailrow == Headrow-1 :  
        pass
       
     elif HeadColumn == TailColumn and Tailrow == Headrow-2 :
       Array[Tailrow][TailColumn].Tail = " "
       Tailrow += 1
       Array[Tailrow][TailColumn].Tail = "T"  
       Array[Tailrow][TailColumn].value = True

   
     elif Tailrow == (Headrow - 2) and TailColumn < HeadColumn:          # if above
        Array[Tailrow][TailColumn].Tail = " " #removing tail
        Tailrow += 1       #moving diagonally down right
        TailColumn += 1
        Array[Tailrow][TailColumn].value = True
        Array[Tailrow][TailColumn].Tail = "T"

   
     elif Tailrow == (Headrow - 2) and TailColumn > HeadColumn: #if below
          Array[Tailrow][TailColumn].Tail = " "
          Tailrow += 1
          TailColumn -= 1
          Array[Tailrow][TailColumn].Tail = "T"
          Array[Tailrow][TailColumn].value = True
       
     
     # output (Array)
     pass



def output(Array):
   
    for i in range (0,500):
          for j in range (0,500):
             print([Array[i][j].Head,Array[i][j].Tail,Array[i][j].value] )


def Count(Array):
     Total = 0
     for i in range (0,500):
          for j in range (0,500):
            if Array[i][j].value == True:
              Total += 1
     print (Total)



def main():
#   #create a 2D array with records of head and tail
    class TBridge:
       def __init__(self) :
           self.value = False
           self.Head = " "
           self.Tail = " "
    row,col = (500,500)

   
    Array = [[TBridge() for i in range(col)] for j in range(row)]
    Array[250][250].Head = "H"
    Array[250][250].value = True
    Array[250][250].Tail = "T"
   
 
    f = open("command.txt","r")
    for i in range(2000):
      line = f.readline().strip().split(" ")
      command = line[0]
      step = int(line[1])
   
      match command:
         case "R" :
            moveRight(Array,step)
   
         case "L" :
            moveLeft(Array,step)
   
         case "U" :
            moveUp(Array,step)
   
         case "D" :
            moveDown(Array,step)
 
 
    Count(Array)

main()
