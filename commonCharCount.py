def commonCharacterCount(s1, s2):
    count_s1 = {}
    count_s2 = {}
    
    for i in s1:
        if i in count_s1:
            count_s1[i] += 1
        else:
            count_s1[i] = 1 
    
    for i in s2:
        if i in count_s2:
            count_s2[i] += 1
        else:
            count_s2[i] = 1
    
    commons_count = 0
    for key in count_s1:
        if key in count_s2:
            commons_count += min(count_s1[key],count_s2[key])
    
    return commons_count
    
    
  # previous
  
    count_s1 = {}
    count_s2 = {}
    
    for i in s1:
        if i in count_s1:
            count_s1[i] += 1
        else:
            count_s1[i] = 1
   
    for i in s2:
        if i in count_s2:
            count_s2[i] += 1
        else:
            count_s2[i] = 1

    summed = 0
    for letter in count_s1:
        if letter in count_s2:
            summed = summed + min(count_s1[letter],count_s2[letter])
    
    return summed
    
    
 # alternative
 
 def commonCharacterCount(s1, s2):
    commons = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(commons)
