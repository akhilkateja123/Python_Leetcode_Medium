import collections

class Solution:
    def deckRevealedIncreasing(self, deck):
        if not deck:
            return None
        
        deck.sort(reverse=True)
        queue= collections.deque()
        
        for card in deck:
            if len(queue)!=0:
                queue.appendleft(queue.pop())
            queue.appendleft(card)  
        
        
        return list(queue)
            
        
        
