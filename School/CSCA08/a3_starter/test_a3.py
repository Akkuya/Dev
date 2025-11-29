"""CSCA08: Fall 2025 -- Assignment 3: Social Media Data Analyst

Starter code for tests to test function get_quantile in
data_analyst.py.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 Dominik Luszczynski,
Jacqueline Smith, David Liu, and Anya Tafliovich

"""

import copy
import unittest
from data_analyst import get_quantile


class TestGetQuantile(unittest.TestCase):
    """Test the function get_quantile."""

    def setUp(self):
        self.unique_list = [5, 2, 1, 3, 4]

    
    def test_unique_list_p0_5(self):
        """Test that we obtain the median from a unique list
        when p = 0.5.
        """
        expected = 3
        actual = get_quantile(self.unique_list, 0.5)
        msg = message([self.unique_list, 0.5], expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_unique_list_p0_25(self):
        """Test that we obtain the first quartile from a unique list
        when p = 0.25.
        """
        expected = 2
        actual = get_quantile(self.unique_list, 0.25)
        msg = message([self.unique_list, 0.25], expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_unique_list_p0_75(self):
        """Test that we obtain the third quartile from a unique list
        when p = 0.75.
        """
        expected = 4
        actual = get_quantile(self.unique_list, 0.75)
        msg = message([self.unique_list, 0.75], expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_repeated_elements_p0_5(self):
        """Test that we obtain the median from a list with repeated
        elements when p = 0.5.
        """
        test_case = [1, 2, 2, 3, 4, 4, 5]
        expected = 3
        actual = get_quantile(test_case, 0.5)
        msg = message([test_case, 0.5], expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_repeated_elements_p0_25(self):
        """Test that we obtain the first quartile from a list with
        repeated elements when p = 0.25.
        """
        test_case = [1, 2, 2, 3, 4, 4, 5]
        expected = 2
        actual = get_quantile(test_case, 0.25)
        msg = message([test_case, 0.25], expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_unique_list_p1(self):
        """Test that we obtain the maximum from a unique list
        when p = 1.0.
        """
        expected = 5
        actual = get_quantile(self.unique_list, 1.0)
        msg = message([self.unique_list, 1.0], expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_unique_list_p1_5(self):
        """Test that we obtain -1 from a unique list
        when p > 1.0.
        """
        expected = -1
        actual = get_quantile(self.unique_list, 1.5)
        msg = message([self.unique_list, 1.5], expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_unique_list_p_neg_0_5(self):
        """Test that we obtain -1 from a unique list
        when p < 0.0.
        """
        expected = -1
        actual = get_quantile(self.unique_list, -0.5)
        msg = message([self.unique_list, -0.5], expected, actual)
        self.assertEqual(actual, expected, msg)
    
def message(test_case: list[list[int], float], expected: int, actual: object) -> str:
    """Return an error message saying the function call
    get_quantile(test_case) resulted in the value
    actual, when the correct value is expected.

    """

    return ("When we called get_quantile(" + str(test_case) +
            ") we expected " + str(expected) +
            ", but got " + str(actual))


if __name__ == '__main__':
    unittest.main(exit=False)
