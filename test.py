while True:
  num = input("Input Number 1 to 9, exit: 0:")
  if(num.isdigit()):
    num = int(num)
    if(num >= 1 and num <= 9):
      for j in range(1,10):
        print ("%d * %d = %d" % (num, j, num*j))
    elif(num == 0):
      print ("Good bye")
      break
    else:
      print ("Please input 0 to 9 number")
  else:
    print ("Please input only 0 to 9 number")