class Solution:

  def isZerosEqualOnes(self, s):
    zerosCounter = 0
    onesCounter = 0

    for char in s:
      if char == '0':
        zerosCounter += 1
      else:
        onesCounter += 1

    return zerosCounter == onesCounter

  def isSeparatedConsecutively(self, s):
    firstChar = s[0]
    isFirstPartEnded = False

    isSeparatedCorrectly = True

    for char in s[1:]:
      if char == firstChar and isFirstPartEnded == True:
        isSeparatedCorrectly = False

      if char != firstChar and isFirstPartEnded == False:
        isFirstPartEnded = True

    return isSeparatedCorrectly

  def countBinarySubstrings(self, s: str) -> int:

    counter = 0

    for startIndex in range(len(s) - 1):
      for endIndex in range(startIndex + 1, len(s) + 1):
        checkStr = s[startIndex:endIndex]
        # print('checkStr %s' % checkStr)

        if self.isSeparatedConsecutively(checkStr) and self.isZerosEqualOnes(
            checkStr):
          counter += 1
          # print(checkStr)

    return counter


my = Solution()
n = '00110011'
trueAns = 6
ans = my.countBinarySubstrings(n)
print("ans", ans, ans == trueAns)
