# Python 3.5.7
# Author: Mathew Perrow
# Desciption: Sorting lists in Python Drill
#             49 of 68 LMS
#
#

li = [67,45,2,13,1,998]
li2 =[89,23,33,45,10,12,45,45,45]

def mysorter (li):
   for i in range(1,len(li)):
        vnow = li[i]    #setting vnow to the value in list in index i
        inow = i        #need i to have a seperate variable to increment
        while inow > 0  and li[inow-1] > vnow:    #While index is more than 0 and value in previous index is larger than value of current index
            li[inow]=li[inow-1]   #Make previous value equal to current value         
            inow -= 1           #decrease the index value by 1 to iterate
        li[inow] = vnow         #swap value in previous index for the current index
        #while statement iterates for len(li)
mysorter(li)
mysorter(li2)
print(li,li2) 
            
            
            
        
    
