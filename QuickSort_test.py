class QuickSortList:
    def add(string):
        liststring = string.split()
        return liststring
    def quickSort(alist):
        QuickSortList.quickSortHelper(alist,0,len(alist)-1)
    def quickSortHelper(alist,first,last):
       if first<last:

          splitpoint = QuickSortList.partition(alist,first,last)

          QuickSortList.quickSortHelper(alist,first,splitpoint-1)
          QuickSortList.quickSortHelper(alist,splitpoint+1,last)
    def partition(alist,first,last):
                  pivotvalue = alist[first]

                  leftmark = first+1
                  rightmark = last

                  done = False
                  while not done:

                        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                              leftmark = leftmark + 1

                        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                             rightmark = rightmark -1

                        if rightmark < leftmark:
                           done = True
                        else:
                             temp = alist[leftmark]
                             alist[leftmark] = alist[rightmark]
                             alist[rightmark] = temp

                  temp = alist[first]
                  alist[first] = alist[rightmark]
                  alist[rightmark] = temp
                  return rightmark
string="54 26 93 17 77 31 44 55 20"
liststring=QuickSortList.add(string)
QuickSortList.quickSort(liststring)
print("The stringlist entred is: ",string)
print("The stringlist sorted is: ",liststring)
import timeit
print("The timeit for this program is: ",timeit.timeit("QuickSortList", globals=globals(), number=5))
