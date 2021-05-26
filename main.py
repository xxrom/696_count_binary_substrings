class Solution:

  def countBinarySubstrings(self, s: str) -> int:
    ansCount = 0

    prevCount = 0
    prev = s[0]
    currentCount = 0
    current = s[0]

    for char in s:
      if char == current:
        currentCount += 1
      else:
        prevCount = currentCount
        prev = current

        current = char
        currentCount = 1

      if currentCount <= prevCount:
        ansCount += 1

    return ansCount


my = Solution()
n = '00110011'
trueAns = 6
ans = my.countBinarySubstrings(n)
print("ans", ans, ans == trueAns)
'''
prev
currentCount = 1
current = 0

0

currentCount = 2
current = 0 

00

001
prevC = 2
prev = 0
currentCount = 1
current = 1

if (currentCount <= prevC):
  +1

0011
prevC = 2
prev = 0
currentCount = 2
current = 1

if (currentCount <= prevC):
  +1

00110
prevC = 2
prev = 1
currentCount = 1
current = 0

if (currentCount <= prevC):
  +1

001100
prevC = 2
prev = 1
currentCount = 2
current = 0

if (currentCount <= prevC):
  +1
'''
