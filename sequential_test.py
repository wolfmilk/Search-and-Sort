class SequentialStringList:
    def add(string):
        liststring = string.split()
        return liststring

    def sequatialSearch (list,sce, item):
        found = False
        count = 0
        while count < len(liststr) and not found:
            if liststr[count] == item:
                found = True
                print("found", item )
            else:
                count = count + 1
        return found
stringlist ="one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty "
print("The Original String: ",stringlist)
liststr=SequentialStringList.add(stringlist)
print("The Stringlist: ",liststr)
sequatialSearchstr1 = "three"
sequatialSearchstr2 = "ziro"
print(SequentialStringList().sequatialSearch(liststr, sequatialSearchstr1))
print(SequentialStringList().sequatialSearch(liststr, sequatialSearchstr2))
import timeit
print("The timeit for this program is: ",timeit.timeit("SequentialStringList()", globals=globals(), number=5))

