import random

class ships:
   def __init__(self,name):
      self.length = -1
      self.alive = True
      self.symbol = ""
      self.name = name

   def hit(self):
      self.length -= 1  

   def getalive(self):
      return self.alive

   def getsym(self):
      return self.symbol
   
   def check(self):
      if self.length == 0:
         print(("My {} has sunk.").format(self.name))

class cruiser(ships):
   def __init__(self):
      super().__init__("cruiser")
      self.length = 3
      self.symbol = "r"
     
class destroyer(ships):
   def __init__(self):
      super().__init__("destroyer")
      self.length = 2
      self.symbol = "d"

class submarine(ships):
   def __init__(self):
      super().__init__("submarine")
      self.length = 3
      self.symbol = "s"

class battleship(ships):
   def __init__(self):
      super().__init__("battleship")
      self.length = 4
      self.symbol = "b"

class carrier(ships):
   def __init__(self):
      super().__init__("carrier")
      self.length = 5
      self.symbol = "a"

class Board:
   def __init__(self):
      self.grid = '''  1 2 3 4 5 6 7 8 9 10 11
A - - - - - - - - - - -
B - - - - - - - - - - -
C - - - - - - - - - - -
D - - - - - - - - - - -
E - - - - - - - - - - -
F - - - - - - - - - - -
G - - - - - - - - - - -
H - - - - - - - - - - -
I - - - - - - - - - - -
J - - - - - - - - - - -
K - - - - - - - - - - -'''

   def outputBoard(self):
      print(self.grid)

   def getcor(self, num):
      return self.grid[num]  
   
   def getposition(self, ans):
      Letter = ans[0]
      Num = ans[1:]
      match Letter:
         case "A":
            Val = 26
         case "B":
            Val = 50
         case "C":
            Val = 50 + 24*1
         case "D":
            Val = 50 + 24*2
         case "E":
            Val = 50 + 24*3
         case "F":
            Val = 50 + 24*4
         case "G":
            Val = 50 + 24*5
         case "H":
            Val = 50 + 24*6
         case "I":
            Val = 50 + 24*7
         case "J":
            Val = 50 + 24*8
         case "K":
            Val = 50 + 24*9
      Val = Val + 2*int(Num)
      return Val

class Player:
   def __init__(self):
      self.start = ""
      self.end = ""
      self.board = Board()
   
   def getBoard(self):
       return self.board

   def starting(self):
      displayme()
      self.start = self.board.getposition(input("Place a cruiser (3) in the form as [A-K][1-11]: "))
      self.end = self.board.getposition(input("To "))
      setup(self.start, self.end, "r")
      self.start = self.board.getposition(input("Please place a destroyer (2) in the form as [A-K][1-11]: "))
      self.end = self.board.getposition(input("To "))
      setup(self.start, self.end, "d")
      start = self.board.getposition(input("Please place a submarine (3) in the form as [A-K][1-11]: "))
      end = self.board.getposition(input("To "))
      setup(start, end, "s")
      self.start = self.board.getposition(input("Please place a battleship (4) in the form as [A-K][1-11]: "))
      self.end = self.board.getposition(input("To "))
      setup(self.start, self.end, "b")
      self.start = self.board.getposition(input("Please place a carrier (5) in the form as [A-K][1-11]: "))
      self.end = self.board.getposition(input("To "))
      setup(self.start, self.end, "a")
      Ans = input("Enter Y if you want to start first, or N for not.")
      if Ans == "Y":    
         loopP()              
      else:
         loopAI()

def place(pos, item, board):
   board.grid = board.grid[:pos] + item + board.grid[pos+1:]

def FillIn(start, end, item):
   global me
   if abs(end-start) < 10 and abs(end-start) != 0:
      if end > start:
         while start < end:
            start += 2
            place(start, item, me.getBoard())
      elif end < start:
         while end > start:
            end += 2
            place(end, item, me.getBoard())
   elif abs(end-start) > 10 and abs(end-start) != 0:
      if end > start:
         while start < end:
            start += 24
            place(start, item, me.getBoard())
      elif end < start:
         while start > end:
            end += 24
            place(end, item, me.getBoard())
   displayme()

def setup(start, end, item):
   global me
   place(start, item, me.getBoard())
   place(end, item, me.getBoard())
   FillIn(start, end, item)

def AIturn():
   global me
   C = False
   next = False
   print('''          ⚠️⚠️⚠️ AI INCOMING ⚠️⚠️⚠️         ''')
   while C is False:
      pos = (random.randint(14, 144))*2
      C = checkpos(pos, me.getBoard())
      if C:
       mark = me.getBoard().grid[pos]
       checkhit(PList, mark)
       place(pos, "x", me.getBoard())
       displayme()
      if checkdie(PList) is False:
         next = True
      else:
         print("~~~~~__---^^^---~~~~~~TITANIC__---^^^---~~~~~~~~~               ")
   return next

def Yourturn():
   global me
   print('''         😁😁😁YOUR TURN 😁😁😁             ''')
   next = False
   pos = me.getBoard().getposition(input("Which position (eg A1) would you like to attack?"))
   checkcross(pos)
   mark = AIboard.grid[pos]
   checkhit(AIList, mark)
   place(pos, "x", AIboard)
   displayAI()
   if checkdie(AIList) is False:
      next = True
   else:
      print("               !!!VICTORY!!!                     ")
      print("~~~~~__---^^^---~~~~~~TITANIC__---^^^---~~~~~~~~~              ")    
   return next

def loopAI():
   if AIturn():
      loopP()

def loopP():
   if Yourturn():
      loopAI()      

def checkdie(List):
   for i in List:
      i.check()  
   if List[0].getalive() or List[1].getalive() or List[2].getalive() or List[3].getalive() or List[4].getalive():
      return False
   else:
      return True

def checkpos(pos, board):
   ready = True
   i = 0  
   while ready is True and i < 11:
      if pos == NumList[i] or board.grid[pos] != "-" or pos == ("A","B","C","D","E","F","G","H","I","J"):
         ready = False
      else:
         i += 1
   return ready        

def displayAI():
   print('            AI BOARD                                                                                                                  ')
   Board.outputBoard(Fboard)

def displayme():
   global me
   print('            Your BOARD                                                                                ')
   Board.outputBoard(me.getBoard())  

def checkhit(list, mark):
   for i in range(5):
      if mark == list[i].getsym():
         list[i].hit()

def checkcross(pos):
   if AIboard.grid[pos] == '-':
      place(pos, "x", Fboard)
   else:
      place(pos, "o", Fboard)

def remove(L1, L2):
   for i in range(len(L2)):
      if L2[i] in L1:
         L1.remove(L2[i])

def AItriple(sym):
   global temp
   NoList = []
   for i in range(len(NumList)):
      NoList.append(NumList[i]+2)
      NoList.append(NumList[i]-2)
   start = 28
   while start < 50:
      NoList.append(start)
      start += 2
   start = 268
   while start < 289:
      NoList.append(start)
      start += 2  
   temp = GridList
   remove(temp, NoList)
   l = len(temp)-1
   index = random.randint(0, l)
   C = temp[index]
   prep = False
   while not prep:
      diff = random.choice(DList)
      if diff == 2:
         if checkpos(C, AIboard) and checkpos(C + 2, AIboard) and checkpos(C - 2, AIboard):                      
            place(C, sym, AIboard)
            place(C + 2, sym, AIboard)
            place(C - 2, sym, AIboard)
            prep = True
      elif diff == 24:
         if checkpos(C, AIboard) and checkpos(C + 24, AIboard) and checkpos(C - 24, AIboard):       
            place(C, sym, AIboard)
            place(C + 24, sym, AIboard)
            place(C - 24, sym, AIboard)
            prep = True

def Op():
   NoList = []
   start = 78
   while start < 223:
      NoList.append(start)
      start += 24
   start = 94
   while start < 239:
      NoList.append(start)
      start += 24
   start = 54
   while start < 71:
      NoList.append(start)
      start += 2
   start = 246
   while start < 263:
      NoList.append(start)
      start += 2
   remove(temp, NoList)

def AIdouble():
   NoList = []
   for i in range(len(NumList)):
      NoList.append(NumList[i]+2)
      NoList.append(NumList[i]-2)
   start = 28
   while start < 50:
      NoList.append(start)
      start += 2
   start = 268
   while start < 289:
      NoList.append(start)
      start += 2
   temp1 = GridList
   remove(temp1, NoList)
   l = len(temp1)-1
   index = random.randint(0, l)
   C = temp1[index]
   prep = False
   while not prep:
      index = random.randint(0, l)
      C = temp1[index]
      diff = random.choice(Num2List)
      if checkpos(C, AIboard) and checkpos(C + diff, AIboard):
         place(C, "d", AIboard)
         place(C + diff, 'd', AIboard)
         prep = True        

def AIcar():
   Op()          
   l = len(temp)-1
   index = random.randint(0, l)
   C = temp[index]  
   prep = False
   while not prep:
      diff = random.choice(DList)    
      if diff == 2:
         if checkpos(C, AIboard) and checkpos(C + 2, AIboard) and checkpos(C - 2, AIboard):
            place(C, "a", AIboard)
            place(C + 2, "a", AIboard)
            place(C - 2, "a", AIboard)
            prep = True
      elif diff == 24:
         if checkpos(C, AIboard) and checkpos(C + 24, AIboard) and checkpos(C - 24, AIboard):
            place(C, "a", AIboard)
            place(C + 24, "a", AIboard)
            place(C - 24, "a", AIboard)
            prep = True

def AIbattle():
   Op()
   l = len(temp)-1
   index = random.randint(0, l)
   C = temp[index]
   prep = False
   while not prep:
      diff = random.choice(DList)
      if diff == 2:
         if checkpos(C, AIboard) and checkpos(C + 2, AIboard) and checkpos(C - 2, AIboard) and checkpos(C + 4, AIboard) and checkpos(C - 4, AIboard):
            d = random.choice(EList)
            place(C, 'b', AIboard)
            place(C + 2, 'b', AIboard)
            place(C - 2, 'b', AIboard)
            place(C + d, 'b', AIboard)
            prep = True
      elif diff == 24:
         if checkpos(C, AIboard) and checkpos(C + 24, AIboard) and checkpos(C - 24, AIboard) and checkpos(C - 48, AIboard) and checkpos(C + 48, AIboard):
            d = random.choice(FList)
            place(C, 'b', AIboard)
            place(C + 24, 'b', AIboard)
            place(C - 24, 'b', AIboard)
            place(C + d, 'b', AIboard)
            prep = True

PC = cruiser()
PB = battleship()
PA = carrier()
PS = submarine()
PD = destroyer()
AC = cruiser()
AB = battleship()
AA = carrier()
AS = submarine()
AD = destroyer()
AIboard = Board()
Fboard = Board()

GridList = []
s = 28
while s < 290:
   GridList.append(s)
   s += 2
PList = [PC, PD, PS, PB, PA]
AIList = [AC, AD, AS, AB, AA]
NumList = [26, 50, 74, 98, 122, 146, 170, 194, 218, 242, 266]
Num2List = [2, -2, 24, -24]
DList = (2, 24)
EList = [4, -4]
FList = [48, -48]
remove(GridList, NumList)
AItriple("r")
AItriple("s")
AIbattle()
AIcar()
AIdouble()
displayAI()

me = Player()
me.starting()
