import unittest
from unittest import TestCase

from algorithms.dataStructures.graph import graph
from algorithms.graphs.breadthFirstSearch import breadthFirstSearch
from algorithms.graphs.breadthFirstSearch import shortestDistance

class bfsTest(TestCase):
    
    def setUp(self):
        arcList = [[1,2],
                   [2,1], [2,3], [2,4],
                   [3,2],[3,4],
                   [4,2], [4,3], [4,5], [4,6],
                   [5,4],
                   [6,4]]
        self.G = graph(arcList)
        
    def test_bfs_searches_every_reachable_node(self):
        s = 1
        
        search = breadthFirstSearch(self.G,s)
        explored = {1: True,
                    2: True,
                    3: True,
                    4: True,
                    5: True,
                    6: True}        
        
        self.assertEqual(search,explored)
        
    def test_shortestDistance(self):
        shortest_paths = shortestDistance(self.G,1)
        levels = {1: 0,
                  2: 1,
                  3: 2,
                  4: 2,
                  5: 3,
                  6: 3}
                  
        self.assertEqual(shortest_paths, levels)
        

if __name__ == '__main__':
    unittest.main()