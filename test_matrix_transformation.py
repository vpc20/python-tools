from unittest import TestCase

from matrix_transformation import transpose


class Test(TestCase):
    def test_transpose(self):
        m1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
        m2 = [[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1]]
        m2 = [[1]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1, 2]]
        m2 = [[1],
              [2]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1],
              [2]]
        m2 = [[1, 2]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1, 2],
              [3, 4]]
        m2 = [[1, 3],
              [2, 4]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1, 2, 3],
              [4, 5, 6]]
        m2 = [[1, 4],
              [2, 5],
              [3, 6]]
        self.assertEqual(m2, transpose(m1))

        m1 = [[1, 2],
              [3, 4],
              [5, 6]]
        m2 = [[1, 3, 5],
              [2, 4, 6]]
        self.assertEqual(m2, transpose(m1))

        # m1 = [[1, 2]]
        # for e in transpose(m1):
        # print(e)
