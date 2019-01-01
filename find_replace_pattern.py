class Solution:
    def findAndReplacePattern(self, words, pattern):
         return [word for word in words if len(set(pattern)) == len(set(word)) == len(set(list(zip(word, pattern))))]
