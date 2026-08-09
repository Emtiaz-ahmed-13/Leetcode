class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = collections.deque([(beginWord, 1)])
        
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word, dist + 1))
                        wordSet.remove(next_word)
        return 0