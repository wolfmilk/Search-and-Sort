class BinaryStringList:
 def add(string):
        liststring = string.split()
        return liststring   
 def binarySearch(list, item): #here I used a different binary methode a simple (if item in the list), because I couldn't compare a string (<,>)
                            
    found = False
    if item in list:
        found = True
        print(item, "founded")
    return found            
stringlist ="one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
liststr=BinaryStringList.add(stringlist)
print(BinaryStringList.binarySearch(liststr,'three'))
print(BinaryStringList.binarySearch(liststr,'zero'))
import timeit
print("The timeit for this program is: ",timeit.timeit("BinaryStringList", globals=globals(), number=5))
 
