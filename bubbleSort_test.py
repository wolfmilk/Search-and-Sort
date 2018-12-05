class BubbleStringList:
    def add(string):
        liststring = string.split()
        return liststring
    def bubbleSort(list):
        for pass_n in range(len(list) -1, 0, -1):
            for i in range (pass_n):
                if list[i] > list[i + 1]:
                    temp = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp
        return liststring
string ="54 26 93 17 77 31 44 55 20"
liststring=BubbleStringList.add(string)
b=BubbleStringList.bubbleSort(liststring)
print("The string entred: " ,  string)
print("The string sorted is " , b)
import timeit
print("The timeit for this program is: ",timeit.timeit("BubbleStringList", globals=globals(), number=5))
