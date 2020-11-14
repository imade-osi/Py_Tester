#5
def minNum(samDaily, kellyDaily, difference):
    if kellyDaily == samDaily: return -1
    
    x = difference / (kellyDaily - samDaily) 
    if x < 0: return -1

    return int(x+1)

#6
def deviceNamesSystem(devicenames):
    names_hash={}
    unique_names =[]

    for item in devicenames:
        if item in names_hash.keys():
            names_hash[item]+=1
            unique_names.append(f'{item}{names_hash[item]}')
        else:
            names_hash[item]=0
            unique_names.append(f'{item}')
                    
    return unique_names

#7 
def funWithAnagrams(text):
    result_array = []
    anagram_hash = {}
    
    for word in text: 
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_hash:
            result_array.append(word)   
            anagram_hash[sorted_word] = True
               
    return sorted(result_array)