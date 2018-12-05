class MergeSortList:
    def add(string):
        liststring = string.split()
        return liststring  

    def mergeSort(list):
        print("splitting",list)
        if len(list)>1:
            mid=len(list)//2
            lh=list[:mid]
            rh=list[mid:]
            MergeSortList.mergeSort(lh)
            MergeSortList.mergeSort(rh)
            i=0
            j=0
            k=0
            while i<len(lh) and j<len(rh):
                 if lh[i]<rh[j]:
                     list[k]=lh[i]
                     i=i+1
                 else:
                     list[k]=rh[j]
                     j=j+1
                 k=k+1
            while i<len(lh):
                  list[k]=lh[i]
                  i=i+1
                  k=k+1
            while j<len(rh):
                  list[k]=rh[j]
                  j=j+1
                  k=k+1
        return print("merging",list)
string="54 26 93 17 77 31 44 55 20"
liststring=MergeSortList.add(string)
b=MergeSortList.mergeSort(liststring)
import timeit
print("The timeit for this program is: ",timeit.timeit("MergeSortList", globals=globals(), number=5))
   
        

