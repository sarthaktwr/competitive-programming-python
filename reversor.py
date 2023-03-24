import os
import math

class ReverSort:
    def __init__(self, array):
        self.array = array
        self.new_list = []
        self.cost = 0

    def reverseList(self):
        return self.array[::-1]
    
    def sort(self):
        for i in range(len(self.array)-1):

            # find minimum element from i to end
            m = min(self.array[i:])

            # find index of the minimum element
            m_index = self.array[i:].index(m)

            # reverse from i to m_index
            self.array[i:m_index+i+1] = self.array[i:m_index+i+1][::-1]

            # keep track of cost
            self.cost += len(self.array[i:m_index+i+1])
        return self.array