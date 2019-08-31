import unittest
import connect4
import numpy as np
import numpy.testing as npt

class Connect4Test(unittest.TestCase):

    def test_board_init(self):
        expectedBoard = np.zeros((6,7))
        result = connect4.create_board()
        npt.assert_allclose(result, expectedBoard)

if __name__ == '__main__':
    unittest.main()