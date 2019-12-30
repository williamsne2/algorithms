from algorithms.ml.nearest_neighbor import (
    distance,
    nearest_neighbor
)

from algorithms.ml.linear_regression import (
    mean,
    std,
    variance,
    cov,
    corr,
    linear_regression,
    r_2
)

import unittest

class TestML(unittest.TestCase):
    def setUp(self):
        # train set for the AND-function
        self.trainSetAND = {(0,0) : 0, (0,1) :0, (1,0) : 0, (1,1) : 1} 

        # train set for light or dark colors
        self.trainSetLight = {(11, 98, 237) : 'L', (3, 39, 96) : 'D', (242, 226, 12) : 'L', (99, 93, 4) : 'D',
        (232, 62, 32) : 'L', (119, 28, 11) : 'D', (25, 214, 47) : 'L', (89, 136, 247) : 'L',
        (21, 34, 63) : 'D', (237, 99, 120) : 'L', (73, 33, 39) : 'D'}

    def test_nearest_neighbor(self):
        # AND-function
        self.assertEqual(nearest_neighbor((1,1), self.trainSetAND), 1)
        self.assertEqual(nearest_neighbor((0,1), self.trainSetAND), 0)

        # dark/light color test
        self.assertEqual(nearest_neighbor((31, 242, 164), self.trainSetLight), 'L')
        self.assertEqual(nearest_neighbor((13, 94, 64), self.trainSetLight), 'D')
        self.assertEqual(nearest_neighbor((230, 52, 239), self.trainSetLight), 'L')
    def test_distance(self):
        self.assertAlmostEqual(distance((1,2,3), (1,0,-1)), 4.47, 2)

    def test_coeffs(self):
        X = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        Y = [-6, 1, -2, 4, -1, 0, 0, 5, -1, 7, 10]
        self.assertEqual(mean(X), 0)
        self.assertAlmostEqual(mean(Y), 1.5455, 4)
        self.assertAlmostEqual(variance(Y), 20.6727, 4)
        self.assertAlmostEqual(std(X), 3.3166, 4)
        self.assertAlmostEqual(cov(X, Y), 11.00, 2)
        self.assertAlmostEqual(corr(X, Y), 0.7295, 4)
        self.assertAlmostEqual(r_2(X, Y), 0.5321, 4)

    def test_linear_reg(self):
        X = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        Y = [-6, 1, -2, 4, -1, 0, 0, 5, -1, 7, 10]
        Y_pred = linear_regression(X, Y)
        Y_hat = []
        err = 0
        for i in range(0, len(X)):
            Y_hat.append(X[i]+1.54545)
            err += Y_pred[i]-Y_hat[i]
        self.assertAlmostEqual(alpha(X, Y), 1.5454, 4)
        self.assertAlmostEqual(beta(X, Y), 1.0000, 2)
        #self.assertAlmostEqual(err, 0, 2)
        
if __name__ == "__main__":
    unittest.main()