import unittest
from persistance import FPersistance

class TestPersistance(unittest.TestCase):
    def test_constructor(self):
        # Non-argument constructor is working
        saver = FPersistance()
        saver.save(cls = 'world', obj={"world": "Earth"}, outfile='test.tmp')
        
        with self.assertRaises(ValueError) as error:
            already_existing_file = saver.save(cls = 'world', obj={"world": "Mars"}, outfile='test.tmp')
        self.assertEqual(str(error.exception), "File already exist")
        
        w = saver.load(cls = 'world', infile='test.tmp')
        self.assertEqual(str(w), "Hello world!")
        
        saver.clean('test.tmp')
        
        with self.assertRaises(ValueError) as error:
            wrong_input = saver.save(cls = 'world', obj="Mars", outfile='test.tmp')
        self.assertEqual(str(error.exception), "Dictionary object expected")
        
        saver.save(cls = 'world', obj={"world": "Mars"}, outfile='test.tmp')
        w = saver.load(cls = 'world', infile='test.tmp')
        saver.clean('test.tmp')

if __name__ == '__main__':
	unittest.main()