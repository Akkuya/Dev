"""A simple checker for style errors and types of functions in
encryption.py.

"""

import unittest
import checker
import encryption
from typing import Type


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test00IsValidRow(self):
        """Function is_valid_matrix."""

        self._check_simple_type(encryption.is_valid_matrix,
                                     [[[1, 2], [2, 1]]],
                                     bool)

    def test01CombineRows(self):
        """Function combine_rows."""

        self._check_simple_type(encryption.combine_rows,
                                [[[1, 2], [2, 1]], [[1], [1]]],
                                type(None))

    def test02InvertBinaryValues(self):
        """Function invert_binary_values"""

        self._check_simple_type(encryption.invert_binary_values,
                                [[[1, 2], [2, 1]]],
                                type(None))

    def test03ConvertBinaryToStr(self):
        """Function convert_binary_to_str"""

        self._check_simple_type(encryption.convert_binary_to_str,
                                     [[[1, 1], [1, 1]]],
                                     type(None))

    def test04ConvertStrToBinary(self):
        """Function convert_str_to_binary"""

        self._check_simple_type(encryption.convert_str_to_binary,
                                     [[['a', 'b'], ['b', 'a']]],
                                     type(None))

    def test05EncryptOrDecrypt(self):
        """ Function encrypt_or_decrypt"""

        self._check_simple_type(encryption.encrypt_or_decrypt,
                                     [[['a', 'a'], ['a', 'b']], 5, True],
                                     type(None))

    def test06RotateMatrix_int(self):
        """Function rotate_matrix"""

        self._returns_n_list_of_m_int_or_str(encryption.rotate_matrix,
                                           [[[1, 0], [0, 1], [0, 1]]], 2, 3, int)
        
    def test06RotateMatrix_str(self):
        """Function rotate_matrix"""

        self._returns_n_list_of_m_int_or_str(encryption.rotate_matrix,
                                           [[['a', 'a', 'a'], ['a', 'a', 'a']]], 3, 2, str)
        
    def test07FlipPhrase_int(self):
        """Function flip_matrix"""

        self._returns_n_list_of_m_int_or_str(encryption.flip_matrix,
                                           [[[1, 0], [0, 1], [0, 1]], True],
                                             3, 2, int)
        
    def test07FlipPhrase_str(self):
        """Function flip_matrix"""

        self._returns_n_list_of_m_int_or_str(encryption.flip_matrix,
                                           [[['b', 'a', 'a'], ['a', 'a', 'b']], True],
                                             2, 3, str)
        
    def test08SolveMysteryPhrase(self):
        """Function solve_mystery_phrase"""

        
        A_HASH = "4c713750846571d7000c821f5f320f8103181e005792cf37aa8adef94d29c5c9"

        A_ENCRYPTED = [
            ["{", "x", "n", "c", "h", "e", "{", "{", "q", "e", "i"],
            ["t", "i", "f", "b", "f", "e", "v", "y", "{", "o", "l"],
            ["n", "e", "p", "e", "v", "l", "d", "j", "o", "r", "d"],
            ["t", "s", "f", "n", "o", "b", "o", "f", "e", "g", "r"],
            ["o", "s", "b", "b", "p", "p", "f", "j", "w", "r", "w"],
            ["n", "h", "{", "c", "s", "s", "x", "k", "m", "h", "x"],
            ["i", "i", "c", "d", "i", "o", "i", "k", "d", "w", "e"],
            ["h", "h", "z", "o", "c", "{", "o", "e", "h", "{", "u"],
            ["h", "w", "n", "z", "s", "g", "h", "w", "d", "r", "{"],
        ]


        self._returns_n_list_of_m_int_or_str(encryption.solve_mystery_phrase,
                                           [A_ENCRYPTED, A_HASH, 20],
                                             11, 9, int)

    
    def _returns_list_of_n_ints(self, func: callable, args: list, n: int):
        """Check that func(args) returns a list of n ints."""

        print(f'\nChecking {func.__name__}...')
        result = checker.returns_list_of(func, args, int)
        self.assertTrue(result[0], result[1])

        msg = checker.type_error_message(
            func.__name__, f'list of {n} ints', result[1])

        self.assertTrue(len(result[1]) == n, msg)
        for i in range(n):
            self.assertTrue(isinstance(result[1][i], int), msg)
        print('  check complete')

    def _returns_n_list_of_m_int_or_str(self, func: callable, args: list, n: int, m: int, t: Type):
        """Check that func(args) returns a list of n nested lists. of m ints"""

        print(f'\nChecking {func.__name__}...')
        result = checker.type_check_simple(func, args, list)
        self.assertTrue(result[0], result[1])

        msg = checker.type_error_message(
            func.__name__, f'list of {n} lists', result[1])
        
        self.assertTrue(all(isinstance(item, list) for item in result[1]), msg)

        self.assertTrue(len(result[1]) == n, msg)
        print(f'\n\tChecking {func.__name__} nested lists...')
        for i in range(n):
            self.assertTrue(len(result[1][i])==m, msg)
            for j in range(m):
                self.assertTrue(isinstance(result[1][i][j], t), msg)
        print('  check complete')


    def _check_simple_type(self, func: callable, args: list,
                           expected: type) -> None:
        """Check that func called with arguments args returns a value of type
        expected. Display the progress and the result of the check.

        """

        print(f'\nChecking {func.__name__}...')
        result = checker.type_check_simple(func, args, expected)
        self.assertTrue(result[0], result[1])
        print('  check complete')


checker.ensure_no_io('encryption')
TARGET_LEN = 79
print(''.center(TARGET_LEN, "="))
print(' Start: checking coding style '.center(TARGET_LEN, "="))
checker.run_pyta('encryption.py', 'a2_pyta.txt')
print(' End checking coding style '.center(TARGET_LEN, "="))

print(' Start: checking type contracts '.center(TARGET_LEN, "="))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, "="))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
