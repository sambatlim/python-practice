class Solution:
  def reverseWords(self, str):
    arrayofword = str.split()
    c = ''
    for i in arrayofword:
        d= ''
        for j in range(len(list(i))-1,-1,-1):
            d = d + list(i)[j]
        c = c + ' ' + d    
    return c

print(Solution().reverseWords("The cat in the hat"))