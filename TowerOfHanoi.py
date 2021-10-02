def towerOfHanoi(numberOfDisk , startPeg = 1, endPeg = 3):
      if numberOfDisk:
            towerOfHanoi(numberOfDisk - 1,startPeg , 6 - startPeg - endPeg)
            print("Move disk %d from peg %d to peg %d"%(numberOfDisk , startPeg, endPeg))
            towerOfHanoi(numberOfDisk -1 , 6 - startPeg - endPeg, endPeg)


towerOfHanoi(2)
