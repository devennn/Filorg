import unittest
from src.directory_process import check_rename_newname

class Check_Filename(unittest.TestCase):
    def test_check_rename_newname_1(self):
        input = "testfile>"
        result = check_rename_newname(input)
        self.assertEqual(result, -1)

    def test_check_rename_newname_2(self):
        input = "testfile"
        result = check_rename_newname(input)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
