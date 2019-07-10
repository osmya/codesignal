def makeArrayConsecutive2(statues):
    h = range(min(statues), max(statues))
    count = 0
    for i in h:
        if i not in statues:
            count += 1
    return count
    
 # alternative 1
 
 def makeArrayConsecutive2(statues):
     return sum([1 for i in range(min(statues), max(statues)) if i not in statues])
 

 # alternative 2
 def makeArrayConsecutive2(s):
    return max(s) - min(s) - len(s) + 1
 
