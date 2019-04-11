
numberList=[1,2,3,4,5]
searchValue=2

def linearSearch():
  counter=0
  for each in numberList:
    counter+=1
    if each==searchValue:
      print("{0} found at position {1} in list.".format(searchValue,counter))
    else:
      print("")

def binarySearch():
  found=False
  counter=0
  listLength=len(numberList)
  halfList=listLength//2
  halfList+=1
  while found!=True:
    counter+=1
    if searchValue==numberList[halfList]:
      print("It took {0} iterations to find {1} at position {2} in the list.".format(counter,searchValue,halfList))
      found=True
    elif searchValue<numberList[halfList]:
      halfList=halfList+(halfList//2)
    elif searchValue>numberList[halfList]:
      halfList=halfList-(halfList//2)
    
if __name__ == "__main__":
  linearSearch()
