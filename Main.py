import random
import time

def player1(total,rounds,P1score,P2score):
  decision=input("P1 = Do you want to Attack or Defend ")
  if decision == "Attack" or decision == "attack":
    attackscore=int(input("P1 = What is the attack score? "))
    defendscore=random.randint(10,100)
    print ("Player 2's score = "+str(defendscore))
    if attackscore>defendscore:
      print ("Player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif defendscore>attackscore:
      print ("player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
  if decision == "Defend" or decision == "defend":
    defendscore=int(input("P1 = What is the defend score? "))
    attackscore=random.randint(10,100)
    print ("Player 2's score = "+str(attackscore))
    if defendscore>attackscore:
      print ("Player 1 wins")
      P1score=int(P1score)+1
      print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif attackscore>defendscore:
      print ("player 2 wins")
      P2score=int(P2score)+1
      print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
  else:
    print ("Player 1's round forfieted")
    print ("+1 point to Player 2")
    P2score=int(P2score)+1
    print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
    return (total,rounds,P1score,P2score)
  return (total,rounds,P1score,P2score)

def player2(total,rounds,P1score,P2score):
  decision=random.randint(1,2)
  if decision == 1:
    attackscore=random.randint(10,100)
    defendscore=int(input("P1 = What is the defend score? "))
    print ("Player 2's score = "+str(attackscore))
    if attackscore>defendscore:
      print ("Player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif defendscore>attackscore:
      print ("player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
  if decision == 2:
    defendscore=random.randint(10,100)
    attackscore=int(input("P1 = What is the attack score? "))
    print ("Player 2's score = "+str(defendscore))
    if defendscore>attackscore:
      print ("Player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif attackscore>defendscore:
      print ("player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
  else:
    print ("Player 2's round forfieted")
    print ("+1 point to Player 1")
    P1score=int(P1score)+1
    print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
    return (total,rounds,P1score,P2score)
  return (total,rounds,P1score,P2score)


def P1turn(total,rounds,P1score,P2score):
  decision=input("P1 = Do you want to Attack or Defend ")
  if decision == "Attack" or decision == "attack":
    attackscore=int(input("P1 = What is the attack score? "))
    defendscore=int(input("P2 = What is the defend score? "))
    if attackscore>defendscore:
      print ("Player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif defendscore>attackscore:
      print ("player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
  if decision == "Defend" or decision == "defend":
    defendscore=int(input("P1 = What is the defend score? "))
    attackscore=int(input("P2 = What is the attack score? "))
    if defendscore>attackscore:
      print ("Player 1 wins")
      P1score=int(P1score)+1
      print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif attackscore>defendscore:
      print ("player 2 wins")
      P2score=int(P2score)+1
      print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
  else:
    print ("Player 1's round forfieted")
    print ("+1 point to Player 2")
    P2score=int(P2score)+1
    print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
    return (total,rounds,P1score,P2score)
  return (total,rounds,P1score,P2score)


def P2turn(total,rounds,P1score,P2score):
  decision=input("P2 = Do you want to Attack or Defend ")
  if decision == "Attack" or decision == "attack":
    attackscore=int(input("P2 = What is the attack score? "))
    defendscore=int(input("P1 = What is the defend score? "))
    if attackscore>defendscore:
      print ("Player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif defendscore>attackscore:
      print ("player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
  if decision == "Defend" or decision == "defend":
    defendscore=int(input("P2 = What is the defend score? "))
    attackscore=int(input("P1 = What is the attack score? "))
    if defendscore>attackscore:
      print ("Player 2 wins")
      P2score=int(P2score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    elif attackscore>defendscore:
      print ("player 1 wins")
      P1score=int(P1score)+1
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
      return (total,rounds,P1score,P2score)
    else:
      print ("draw")
      print ("PLayer 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
  else:
    print ("Player 2's round forfieted")
    print ("+1 point to Player 1")
    P1score=int(P1score)+1
    print ("Player 1 has "+str(P1score)+" and Player 2 has "+str(P2score))
    return (total,rounds,P1score,P2score)
  return (total,rounds,P1score,P2score)



#main code
total=0
rounds=0
P1score=0
P2score=0
ValidInput=False
while ValidInput==False:
    print ("Do you want to play single player or two player?")
    gamemode=input("Enter 1P or 2P ")
    if gamemode=="1P" or gamemode=="2P":
        ValidInput=True
    else:
        ValidInput=False
        print ("Invalid input. Please enter 1P or 2P")
        time.sleep(1)

if gamemode=="1P":
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player2(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player2(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player2(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player2(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player2(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=player1(total,rounds,P1score,P2score)
  print (                                                         )

if gamemode=="2P":
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P2turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P2turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P2turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P2turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P2turn(total,rounds,P1score,P2score)
  print (                                                         )
  total,rounds,P1score,P2score=P1turn(total,rounds,P1score,P2score)
  print (                                                         )

if (P1score>0 and P2score>0):
    if P1score>P2score:
      print ("player 1 wins with a score of "+str(P1score)+"-"+str(P2score))
    elif P2score>P1score:
      print ("player 2 wins with a score of "+str(P2score)+"-"+str(P1score))
    elif P1score==P2score:
      print ("It's a draw")
    else:
      print ("ERROR")