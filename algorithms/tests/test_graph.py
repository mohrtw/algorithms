import unittest
from unittest import TestCase
# from unittest import skip

from algorithms.dataStructures.graph import graph


class graphTest(TestCase):

    def setUp(self):
        arcList = [[1, 2], [1, 3], [1, 4],
                   [2, 1],
                   [3, 2], [3, 5],
                   [5, 1]]
        self.G = graph(arcList)

    def test_can_check_if_vertex_is_in_graph(self):
        # returns True if vertex is in graph
        truthy = self.G.check_vertex(1)
        self.assertTrue(truthy)
        truthy = self.G.check_vertex(2)
        self.assertTrue(truthy)
        truthy = self.G.check_vertex(3)
        self.assertTrue(truthy)
        truthy = self.G.check_vertex(4)
        self.assertTrue(truthy)
        truthy = self.G.check_vertex(5)
        self.assertTrue(truthy)

        # returns False if vertex is not in graph
        truthy = self.G.check_vertex(0)
        self.assertFalse(truthy)
        truthy = self.G.check_vertex(-2)
        self.assertFalse(truthy)
        truthy = self.G.check_vertex(6)
        self.assertFalse(truthy)
        truthy = self.G.check_vertex('a')
        self.assertFalse(truthy)

    def test_can_check_if_arc_in_graph(self):
        v, a = 1, 2
        truthy = self.G.check_arc(v, a)
        self.assertTrue(truthy)
        v, a = 3, 5
        truthy = self.G.check_arc(v, a)
        self.assertTrue(truthy)

        v, a = 1, 5
        truthy = self.G.check_arc(v, a)
        self.assertFalse(truthy, self.G.arcs)        
        v, a = 0, 2
        truthy = self.G.check_arc(v, a)
        self.assertFalse(truthy)

    def test_can_add_vertex_to_graph(self):
        v = 8
        truthy = self.G.check_vertex(v)
        self.assertFalse(truthy)

        self.G.add_vertex(v)
        truthy = self.G.check_vertex(v)
        self.assertTrue(truthy)

    def test_can_add_arc_to_existing_vertex(self):
        v, a = 1, 5
        truthy = self.G.check_vertex(v) and self.G.check_vertex(a)
        self.assertTrue(truthy)

        self.G.add_arc(v, a)
        truthy = self.G.check_arc(v, a)
        self.assertTrue(truthy)

    def test_remove_vertex(self):
        v = 1
        truthy = self.G.check_vertex(v)
        self.assertTrue(truthy)

        self.G.remove_vertex(v)
        truthy = self.G.check_vertex(v)
        self.assertFalse(truthy)

    def test_remove_arc(self):
        v, a = 1, 2
        truthy = self.G.check_arc(v, a)
        self.assertTrue(truthy)

        self.G.remove_arc(v, a)
        truthy = self.G.check_arc(v, a)
        self.assertFalse(truthy)

        truthy = self.G.check_vertex(v)
        self.assertTrue(truthy)
        truthy = self.G.check_vertex(a)
        self.assertTrue(truthy)

    def test_get_list_of_a_vertexs_arcs(self):
        v = 1
        vArcs = self.G.get_arcs(v)
        self.assertEqual(vArcs, [2, 3, 4])

if __name__ == '__main__':
    unittest.main()
