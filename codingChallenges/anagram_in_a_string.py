import alphaPrime

def find_anagrams(s,t):

    multiString = 1
    for character in t:
        multiString = multiString * alphaPrime.AlphaPrime[character]

    array_of_s =[]
    for character_in_s in s:
        array_of_s.append(character_in_s)

    result = []
    for i in range(len(array_of_s)): 
        newMulti = 1
        for j in range(len(t)):

            if i + j >= len(array_of_s):
                break
            else:   
                newMulti = newMulti * alphaPrime.AlphaPrime[array_of_s[i+j]]
                if newMulti == multiString:
                    result.append(i)
    return(result)

print(find_anagrams("acdbacdacb","abcd"))

